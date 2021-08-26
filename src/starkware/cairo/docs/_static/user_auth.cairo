%lang starknet
%builtins pedersen range_check ecdsa

from starkware.cairo.common.cairo_builtins import HashBuiltin, SignatureBuiltin
from starkware.cairo.common.signature import verify_ecdsa_signature
from starkware.starknet.common.storage import Storage

# A map from user (public key) to a balance.
@storage_var
func balance(user : felt) -> (res : felt):
end

# Increases the balance of the given user by the given amount.
@external
func increase_balance{
        storage_ptr : Storage*, pedersen_ptr : HashBuiltin*, range_check_ptr,
        ecdsa_ptr : SignatureBuiltin*}(user : felt, amount : felt, sig_r : felt, sig_s : felt):
    # Verify the user's signature.
    verify_ecdsa_signature(message=amount, public_key=user, signature_r=sig_r, signature_s=sig_s)

    let (res) = balance.read(user=user)
    balance.write(user, res + amount)
    return ()
end

# Returns the balance of the given user.
@view
func get_balance{storage_ptr : Storage*, pedersen_ptr : HashBuiltin*, range_check_ptr}(
        user : felt) -> (res : felt):
    let (res) = balance.read(user=user)
    return (res)
end
