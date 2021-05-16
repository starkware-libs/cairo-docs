from types import SimpleNamespace

from starkware.crypto.signature.signature import EC_ORDER, FIELD_PRIME, N_ELEMENT_BITS_ECDSA

value_upper_limits_bit_length = SimpleNamespace(
    token_id=251,
    non_mintable_token_id=250,
    nonce=31,
    expiration_timestamp=22,
    amount=63,
    order_id=63,
    sig_r=N_ELEMENT_BITS_ECDSA,
    vault_id=31,
)

value_upper_limits = SimpleNamespace(
    # Mintable tokens must have bit 250 set to 1, and bits 240-249 set to zero.
    mintable_token_id=2**250 + 2**240,
    stark_key=FIELD_PRIME,
    sig_s=EC_ORDER,
    **{val_name: 2**bits for val_name, bits in vars(value_upper_limits_bit_length).items()}
)


value_lower_limits = SimpleNamespace(
    token_id=0,
    mintable_token_id=2**250,
    non_mintable_token_id=0,
    stark_key=0,
    nonce=0,
    expiration_timestamp=0,
    amount=0,
    order_id=0,
    sig_r=0,
    sig_s=0,
    vault_id=0,
)


def is_value_in_range(value_name, value):
    try:
        lower_limit = getattr(value_lower_limits, value_name)
        upper_limit = getattr(value_upper_limits, value_name)
    except AttributeError:
        raise AttributeError(f'Unexpected transaction attribute name: {value_name}')

    return lower_limit <= value < upper_limit
