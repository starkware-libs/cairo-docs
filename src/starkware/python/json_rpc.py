"""
Encodes and plays JSON-RPC calls.
"""

import json
from typing import Dict


class JsonRpcMethod:
    """
    Represents a JSON-RPC method that can be called to generate a JSON-RPC request.
    """

    def __init__(self, name: str):
        self.name = name

    def __call__(self, *args, **kwargs) -> str:
        # Make sure the call is positional nand named.
        empty, params = sorted((args, kwargs), key=len)
        assert len(empty) == 0, 'JSON RPC call cannot contain both positional and named arguments.'

        call_dict: Dict = {'jsonrpc': '2.0', 'method': self.name, 'id': None}
        if len(params) != 0:
            call_dict['params'] = params

        return json.dumps(call_dict)


class JsonRpcEncoder:
    """
    Generates JsonRpcMethods.
    """

    def __getattr__(self, name: str) -> JsonRpcMethod:
        return JsonRpcMethod(name=name)
