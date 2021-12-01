import dataclasses
from typing import Any, List, Tuple

from starkware.cairo.lang.vm.cairo_pie import ExecutionResources
from starkware.starknet.business_logic.internal_transaction_interface import (
    ContractCall,
    L2ToL1MessageInfo,
    TransactionExecutionInfo,
)
from starkware.starkware_utils.validated_dataclass import ValidatedDataclass


@dataclasses.dataclass(frozen=True)
class StarknetContractCall(ValidatedDataclass):
    """
    A lean version of ContractCall class, containing merely the information relevant for the user.
    """

    from_address: int  # The caller contract address.
    to_address: int  # The called contract address.
    calldata: List[int]
    signature: List[int]
    cairo_usage: ExecutionResources
    @classmethod
    def from_internal_version(cls, contract_call: ContractCall) -> "StarknetContractCall":
        return cls(
            from_address=contract_call.from_address,
            to_address=contract_call.to_address,
            calldata=contract_call.calldata,
            signature=contract_call.signature,
            cairo_usage=contract_call.cairo_usage,
        )


@dataclasses.dataclass(frozen=True)
class StarknetTransactionExecutionInfo(ValidatedDataclass):
    """
    A lean version of TransactionExecutionInfo class, containing merely the information relevant
    for the user.
    """

    result: Tuple[Any, ...]
    l2_to_l1_messages: List[L2ToL1MessageInfo]
    call_info: StarknetContractCall
    internal_calls: List[StarknetContractCall]

    @classmethod
    def from_internal(
        cls, tx_execution_info: TransactionExecutionInfo, result: Tuple[Any, ...]
    ) -> "StarknetTransactionExecutionInfo":
        return cls(
            result=result,
            l2_to_l1_messages=tx_execution_info.l2_to_l1_messages,
            call_info=StarknetContractCall.from_internal_version(
                contract_call=tx_execution_info.call_info
            ),
            internal_calls=[
                StarknetContractCall.from_internal_version(contract_call=contract_call)
                for contract_call in tx_execution_info.internal_calls
            ],
        )
