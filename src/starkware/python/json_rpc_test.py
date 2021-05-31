"""
Tests jsonrpc.py.
"""

import json

import pytest

from starkware.python.json_rpc import JsonRpcEncoder


def test_encoder():
    """
    Tests the JSON RPC encoder.
    """
    encoder = JsonRpcEncoder()

    assert json.loads(encoder.foo(1, 2, 3)) == {
        'jsonrpc': '2.0',
        'method': 'foo',
        'params': [1, 2, 3],
        'id': None,
    }

    assert json.loads(encoder.bar(x=1, y='abc', z={'a': 3, 'b': 'c'})) == {
        'jsonrpc': '2.0',
        'method': 'bar',
        'params': {
            'x': 1,
            'y': 'abc',
            'z': {
                'a': 3,
                'b': 'c',
            },
        },
        'id': None,
    }

    with pytest.raises(AssertionError, match='cannot contain both positional and named arguments.'):
        encoder.baz(1, 2, x=3)
