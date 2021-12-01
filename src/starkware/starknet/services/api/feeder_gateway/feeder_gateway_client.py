import json
from typing import Any, Dict, List, Optional, Union

from services.everest.api.feeder_gateway.feeder_gateway_client import EverestFeederGatewayClient
from starkware.starknet.definitions import fields
from starkware.starknet.services.api.gateway.transaction import InvokeFunction
from starkware.starkware_utils.validated_fields import RangeValidatedField

CastableToHash = Union[int, str]
JsonObject = Dict[str, Any]


class FeederGatewayClient(EverestFeederGatewayClient):
    """
    A client class for the StarkNet FeederGateway.
    """

    async def get_contract_addresses(self) -> Dict[str, str]:
        raw_response = await self._send_request(send_method="GET", uri=f"/get_contract_addresses")
        return json.loads(raw_response)

    async def call_contract(
        self,
        invoke_tx: InvokeFunction,
        block_hash: Optional[CastableToHash] = None,
        block_number: Optional[int] = None,
    ) -> Dict[str, List[str]]:

        raw_response = await self._send_request(
            send_method="POST",
            uri=(
                "/call_contract?"
                f"{block_identifier(block_hash=block_hash, block_number=block_number)}"
            ),
            data=invoke_tx.dumps(),
        )
        return json.loads(raw_response)

    async def get_block(
        self,
        block_hash: Optional[CastableToHash] = None,
        block_number: Optional[int] = None,
    ) -> JsonObject:
        raw_response = await self._send_request(
            send_method="GET",
            uri=f"/get_block?{block_identifier(block_hash=block_hash, block_number=block_number)}",
        )
        return json.loads(raw_response)

    async def get_code(
        self,
        contract_address: int,
        block_hash: Optional[CastableToHash] = None,
        block_number: Optional[int] = None,
    ) -> List[str]:
        uri = (
            f"/get_code?contractAddress={hex(contract_address)}&"
            f"{block_identifier(block_hash=block_hash, block_number=block_number)}"
        )
        raw_response = await self._send_request(send_method="GET", uri=uri)
        return json.loads(raw_response)

    async def get_storage_at(
        self,
        contract_address: int,
        key: int,
        block_hash: Optional[CastableToHash] = None,
        block_number: Optional[int] = None,
    ) -> str:
        uri = (
            f"/get_storage_at?contractAddress={hex(contract_address)}&key={key}&"
            f"{block_identifier(block_hash=block_hash, block_number=block_number)}"
        )
        raw_response = await self._send_request(send_method="GET", uri=uri)
        return json.loads(raw_response)

    async def get_transaction_status(
        self, tx_hash: Optional[CastableToHash], tx_id: Optional[int] = None
    ) -> JsonObject:
        raw_response = await self._send_request(
            send_method="GET",
            uri=f"/get_transaction_status?{tx_identifier(tx_hash=tx_hash, tx_id=tx_id)}",
        )
        return json.loads(raw_response)

    async def get_transaction(
        self, tx_hash: Optional[CastableToHash], tx_id: Optional[int] = None
    ) -> JsonObject:
        raw_response = await self._send_request(
            send_method="GET", uri=f"/get_transaction?{tx_identifier(tx_hash=tx_hash, tx_id=tx_id)}"
        )
        return json.loads(raw_response)

    async def get_transaction_receipt(
        self, tx_hash: Optional[CastableToHash], tx_id: Optional[int] = None
    ) -> JsonObject:
        raw_response = await self._send_request(
            send_method="GET",
            uri=f"/get_transaction_receipt?{tx_identifier(tx_hash=tx_hash, tx_id=tx_id)}",
        )
        return json.loads(raw_response)

    async def get_block_hash_by_id(self, block_id: int) -> str:
        raw_response = await self._send_request(
            send_method="GET",
            uri=f"/get_block_hash_by_id?blockId={block_id}",
        )
        return json.loads(raw_response)

    async def get_block_id_by_hash(self, block_hash: CastableToHash) -> int:
        raw_response = await self._send_request(
            send_method="GET",
            uri=(
                "/get_block_id_by_hash?"
                f"blockHash={format_hash(hash_value=block_hash, hash_field=fields.BlockHashField)}"
            ),
        )
        return json.loads(raw_response)


def format_hash(hash_value: CastableToHash, hash_field: RangeValidatedField) -> str:
    if isinstance(hash_value, int):
        return hash_field.format(hash_value)

    assert isinstance(hash_value, str)
    return hash_value


def tx_identifier(tx_hash: Optional[CastableToHash], tx_id: Optional[int]) -> str:
    if tx_hash is None:
        return f"transactionId={json.dumps(tx_id)}"
    else:
        hash_str = format_hash(hash_value=tx_hash, hash_field=fields.TransactionHashField)
        return f"transactionHash={hash_str}"


def block_identifier(block_hash: Optional[CastableToHash], block_number: Optional[int]) -> str:
    if block_hash is None:
        return f"blockNumber={json.dumps(block_number)}"
    else:
        return f"blockHash={format_hash(hash_value=block_hash, hash_field=fields.BlockHashField)}"
