from typing import List, Optional, Union

from starkware.starknet.compiler.compile import compile_starknet_files
from starkware.starknet.definitions.general_config import StarknetGeneralConfig
from starkware.starknet.services.api.contract_definition import ContractDefinition, EntryPointType
from starkware.starknet.services.api.messages import StarknetMessage
from starkware.starknet.testing.contract import StarknetContract
from starkware.starknet.testing.state import CastableToAddress, CastableToAddressSalt, StarknetState


class Starknet:
    """
    A high level interface to a StarkNet state object.
    Example:
      starknet = await Starknet.empty()
      contract = await starknet.deploy('contract.cairo')
      await contract.foo(a=1, b=[2, 3]).invoke()
    """

    def __init__(self, state: StarknetState):
        self.state = state

    @classmethod
    async def empty(cls, general_config: Optional[StarknetGeneralConfig] = None) -> "Starknet":
        return Starknet(state=await StarknetState.empty(general_config=general_config))

    async def deploy(
        self,
        source: Optional[str] = None,
        contract_def: Optional[ContractDefinition] = None,
        contract_address_salt: Optional[CastableToAddressSalt] = None,
        cairo_path: Optional[List[str]] = None,
        constructor_calldata: Optional[List[int]] = None,
    ) -> StarknetContract:
        assert (source is None) != (
            contract_def is None
        ), "Exactly one of source, contract_def should be supplied."
        if contract_def is None:
            contract_def = compile_starknet_files(
                files=[source], debug_info=True, cairo_path=cairo_path
            )
            source = None
            cairo_path = None
        assert (
            cairo_path is None
        ), "The cairo_path argument can only be used with the source argument."
        assert contract_def is not None
        address = await self.state.deploy(
            contract_definition=contract_def,
            contract_address_salt=contract_address_salt,
            constructor_calldata=[] if constructor_calldata is None else constructor_calldata,
        )
        assert contract_def.abi is not None, "Missing ABI."
        return StarknetContract(state=self.state, abi=contract_def.abi, contract_address=address)

    def consume_message_from_l2(self, from_address: int, to_address: int, payload: List[int]):
        """
        Mocks the L1 contract function consumeMessageFromL2.
        """
        starknet_message = StarknetMessage.create_message_to_l1(
            from_address=from_address,
            to_address=to_address,
            payload=payload,
        )
        self.state.consume_message_hash(message_hash=starknet_message.get_hash())

    async def send_message_to_l2(
        self,
        from_address: int,
        to_address: CastableToAddress,
        selector: Union[int, str],
        payload: List[int],
    ):
        """
        Mocks the L1 contract function sendMessageToL2.
        """
        await self.state.invoke_raw(
            contract_address=to_address,
            selector=selector,
            calldata=[from_address, *payload],
            caller_address=0,
            entry_point_type=EntryPointType.L1_HANDLER,
        )
