# Free functions

- [panic_with_felt252](./core-panic_with_felt252.md)

- [assert](./core-assert.md)

- [circuit_add](./core-circuit-circuit_add.md)

- [circuit_sub](./core-circuit-circuit_sub.md)

- [circuit_inverse](./core-circuit-circuit_inverse.md)

- [circuit_mul](./core-circuit-circuit_mul.md)

- [check_ecdsa_signature](./core-ecdsa-check_ecdsa_signature.md)

- [ecdsa::recover_public_key](./core-ecdsa-recover_public_key.md)

- [u128_wrapping_add](./core-integer-u128_wrapping_add.md)

- [u128_wrapping_sub](./core-integer-u128_wrapping_sub.md)

- [u128_wide_mul](./core-integer-u128_wide_mul.md)

- [u128_overflowing_mul](./core-integer-u128_overflowing_mul.md)

- [u8_wrapping_add](./core-integer-u8_wrapping_add.md)

- [u8_wrapping_sub](./core-integer-u8_wrapping_sub.md)

- [u16_wrapping_add](./core-integer-u16_wrapping_add.md)

- [u16_wrapping_sub](./core-integer-u16_wrapping_sub.md)

- [u32_wrapping_add](./core-integer-u32_wrapping_add.md)

- [u32_wrapping_sub](./core-integer-u32_wrapping_sub.md)

- [u64_wrapping_add](./core-integer-u64_wrapping_add.md)

- [u64_wrapping_sub](./core-integer-u64_wrapping_sub.md)

- [u256_overflowing_add](./core-integer-u256_overflowing_add.md)

- [u256_overflowing_sub](./core-integer-u256_overflowing_sub.md)

- [u256_overflow_sub](./core-integer-u256_overflow_sub.md)

- [u256_overflowing_mul](./core-integer-u256_overflowing_mul.md)

- [u256_overflow_mul](./core-integer-u256_overflow_mul.md)

- [u256_wide_mul](./core-integer-u256_wide_mul.md)

- [u128_add_with_bounded_int_carry](./core-integer-u128_add_with_bounded_int_carry.md)

- [u512_safe_div_rem_by_u256](./core-integer-u512_safe_div_rem_by_u256.md)

- [egcd](./core-math-egcd.md)

- [inv_mod](./core-math-inv_mod.md)

- [u256_inv_mod](./core-math-u256_inv_mod.md)

- [u256_div_mod_n](./core-math-u256_div_mod_n.md)

- [u256_mul_mod_n](./core-math-u256_mul_mod_n.md)

- [min](./core-cmp-min.md)

- [max](./core-cmp-max.md)

- [minmax](./core-cmp-minmax.md)

- [panic_with_byte_array](./core-panics-panic_with_byte_array.md)

- [keccak_u256s_le_inputs](./core-keccak-keccak_u256s_le_inputs.md)

- [keccak_u256s_be_inputs](./core-keccak-keccak_u256s_be_inputs.md)

- [cairo_keccak](./core-keccak-cairo_keccak.md)

- [compute_keccak_byte_array](./core-keccak-compute_keccak_byte_array.md)

- [compute_sha256_u32_array](./core-sha256-compute_sha256_u32_array.md)

- [compute_sha256_byte_array](./core-sha256-compute_sha256_byte_array.md)

- [poseidon_hash_span](./core-poseidon-poseidon_hash_span.md)

- [print_byte_array_as_string](./core-debug-print_byte_array_as_string.md)

- [get_execution_info](./core-starknet-info-get_execution_info.md)

- [get_caller_address](./core-starknet-info-get_caller_address.md)

- [get_contract_address](./core-starknet-info-get_contract_address.md)

- [get_block_info](./core-starknet-info-get_block_info.md)

- [get_tx_info](./core-starknet-info-get_tx_info.md)

- [get_block_timestamp](./core-starknet-info-get_block_timestamp.md)

- [get_block_number](./core-starknet-info-get_block_number.md)

- [signature_from_vrs](./core-starknet-secp256_trait-signature_from_vrs.md)

- [is_signature_entry_valid](./core-starknet-secp256_trait-is_signature_entry_valid.md)

- [is_valid_signature](./core-starknet-secp256_trait-is_valid_signature.md)

- [starknet::secp256_trait::recover_public_key](./core-starknet-secp256_trait-recover_public_key.md)

- [verify_eth_signature](./core-starknet-eth_signature-verify_eth_signature.md)

- [is_eth_signature_valid](./core-starknet-eth_signature-is_eth_signature_valid.md)

- [public_key_point_to_eth_address](./core-starknet-eth_signature-public_key_point_to_eth_address.md)

- [set_block_number](./core-starknet-testing-set_block_number.md)

- [set_caller_address](./core-starknet-testing-set_caller_address.md)

- [set_contract_address](./core-starknet-testing-set_contract_address.md)

- [set_sequencer_address](./core-starknet-testing-set_sequencer_address.md)

- [set_block_timestamp](./core-starknet-testing-set_block_timestamp.md)

- [set_version](./core-starknet-testing-set_version.md)

- [set_account_contract_address](./core-starknet-testing-set_account_contract_address.md)

- [set_max_fee](./core-starknet-testing-set_max_fee.md)

- [set_transaction_hash](./core-starknet-testing-set_transaction_hash.md)

- [set_chain_id](./core-starknet-testing-set_chain_id.md)

- [set_nonce](./core-starknet-testing-set_nonce.md)

- [set_signature](./core-starknet-testing-set_signature.md)

- [set_block_hash](./core-starknet-testing-set_block_hash.md)

- [pop_log_raw](./core-starknet-testing-pop_log_raw.md)

- [pop_log](./core-starknet-testing-pop_log.md)

- [pop_l2_to_l1_message](./core-starknet-testing-pop_l2_to_l1_message.md)

- [split_bytes31](./core-bytes_31-split_bytes31.md)

- [one_shift_left_bytes_felt252](./core-bytes_31-one_shift_left_bytes_felt252.md)

- [one_shift_left_bytes_u128](./core-bytes_31-one_shift_left_bytes_u128.md)

