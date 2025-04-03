# Summary

- [Intro](./intro.md)

- [Modules](./modules.md)

  - [core](./core.md)

  - [traits](./core-traits.md)

  - [boolean](./core-boolean.md)

  - [circuit](./core-circuit.md)

  - [felt_252](./core-felt_252.md)

  - [box](./core-box.md)

  - [nullable](./core-nullable.md)

  - [array](./core-array.md)

  - [dict](./core-dict.md)

  - [result](./core-result.md)

  - [option](./core-option.md)

  - [clone](./core-clone.md)

  - [ec](./core-ec.md)

  - [ecdsa](./core-ecdsa.md)

  - [integer](./core-integer.md)

  - [math](./core-math.md)

  - [num](./core-num.md)

  - [ops](./core-ops.md)

  - [cmp](./core-cmp.md)

  - [gas](./core-gas.md)

  - [panics](./core-panics.md)

  - [serde](./core-serde.md)

  - [hash](./core-hash.md)

  - [keccak](./core-keccak.md)

  - [sha256](./core-sha256.md)

  - [pedersen](./core-pedersen.md)

  - [poseidon](./core-poseidon.md)

  - [debug](./core-debug.md)

  - [fmt](./core-fmt.md)

  - [starknet](./core-starknet.md)

  - [internal](./core-internal.md)

  - [zeroable](./core-zeroable.md)

  - [bytes_31](./core-bytes_31.md)

  - [byte_array](./core-byte_array.md)

  - [string](./core-string.md)

  - [to_byte_array](./core-to_byte_array.md)

  - [testing](./core-testing.md)

  - [metaprogramming](./core-metaprogramming.md)

  - [prelude](./core-prelude.md)

  - [iter](./core-iter.md)

  - [stark_curve](./core-ec-stark_curve.md)

  - [one_based](./core-math-one_based.md)

  - [num::traits](./core-num-traits.md)

  - [zero](./core-num-traits-zero.md)

  - [one](./core-num-traits-one.md)

  - [bit_size](./core-num-traits-bit_size.md)

  - [num::traits::ops](./core-num-traits-ops.md)

  - [overflowing](./core-num-traits-ops-overflowing.md)

  - [wrapping](./core-num-traits-ops-wrapping.md)

  - [checked](./core-num-traits-ops-checked.md)

  - [saturating](./core-num-traits-ops-saturating.md)

  - [pow](./core-num-traits-ops-pow.md)

  - [sqrt](./core-num-traits-ops-sqrt.md)

  - [widemul](./core-num-traits-ops-widemul.md)

  - [widesquare](./core-num-traits-ops-widesquare.md)

  - [num::traits::ops::wrapping::overflow_based](./core-num-traits-ops-wrapping-overflow_based.md)

  - [num::traits::ops::checked::overflow_based](./core-num-traits-ops-checked-overflow_based.md)

  - [num::traits::ops::saturating::overflow_based](./core-num-traits-ops-saturating-overflow_based.md)

  - [index](./core-ops-index.md)

  - [serde::into_felt252_based](./core-serde-into_felt252_based.md)

  - [hash::into_felt252_based](./core-hash-into_felt252_based.md)

  - [fmt::into_felt252_based](./core-fmt-into_felt252_based.md)

  - [storage_access](./core-starknet-storage_access.md)

  - [syscalls](./core-starknet-syscalls.md)

  - [secp256_trait](./core-starknet-secp256_trait.md)

  - [secp256k1](./core-starknet-secp256k1.md)

  - [secp256r1](./core-starknet-secp256r1.md)

  - [contract_address](./core-starknet-contract_address.md)

  - [eth_address](./core-starknet-eth_address.md)

  - [eth_signature](./core-starknet-eth_signature.md)

  - [class_hash](./core-starknet-class_hash.md)

  - [event](./core-starknet-event.md)

  - [account](./core-starknet-account.md)

  - [storage](./core-starknet-storage.md)

  - [starknet::testing](./core-starknet-testing.md)

  - [bounded_int](./core-internal-bounded_int.md)

  - [zero_based](./core-zeroable-zero_based.md)

- [Constants](./constants.md)

  - [ALPHA](./core-ec-stark_curve-ALPHA.md)

  - [BETA](./core-ec-stark_curve-BETA.md)

  - [ORDER](./core-ec-stark_curve-ORDER.md)

  - [GEN_X](./core-ec-stark_curve-GEN_X.md)

  - [GEN_Y](./core-ec-stark_curve-GEN_Y.md)

  - [VALIDATED](./core-starknet-VALIDATED.md)

  - [BYTES_IN_BYTES31](./core-bytes_31-BYTES_IN_BYTES31.md)

  - [POW_2_128](./core-bytes_31-POW_2_128.md)

  - [POW_2_8](./core-bytes_31-POW_2_8.md)

  - [BYTE_ARRAY_MAGIC](./core-byte_array-BYTE_ARRAY_MAGIC.md)

- [Free functions](./free_functions.md)

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

- [Structs](./structs.md)

  - [u384](./core-circuit-u384.md)

  - [CircuitElement](./core-circuit-CircuitElement.md)

  - [Span](./core-array-Span.md)

  - [SpanIter](./core-array-SpanIter.md)

  - [ArrayIter](./core-array-ArrayIter.md)

  - [u256](./core-integer-u256.md)

  - [u512](./core-integer-u512.md)

  - [Range](./core-ops-range-Range.md)

  - [Panic](./core-panics-Panic.md)

  - [pedersen::HashState](./core-pedersen-HashState.md)

  - [poseidon::HashState](./core-poseidon-HashState.md)

  - [Error](./core-fmt-Error.md)

  - [Formatter](./core-fmt-Formatter.md)

  - [starknet::eth_address::EthAddress](./core-starknet-eth_address-EthAddress.md)

  - [ExecutionInfo](./core-starknet-info-v2-ExecutionInfo.md)

  - [BlockInfo](./core-starknet-info-BlockInfo.md)

  - [TxInfo](./core-starknet-info-v2-TxInfo.md)

  - [ResourceBounds](./core-starknet-info-v2-ResourceBounds.md)

  - [Signature](./core-starknet-secp256_trait-Signature.md)

  - [starknet::eth_address::EthAddress](./core-starknet-eth_address-EthAddress.md)

  - [Call](./core-starknet-account-Call.md)

  - [AccountContractDispatcher](./core-starknet-account-AccountContractDispatcher.md)

  - [AccountContractLibraryDispatcher](./core-starknet-account-AccountContractLibraryDispatcher.md)

  - [AccountContractSafeLibraryDispatcher](./core-starknet-account-AccountContractSafeLibraryDispatcher.md)

  - [AccountContractSafeDispatcher](./core-starknet-account-AccountContractSafeDispatcher.md)

  - [StoragePointer](./core-starknet-storage-StoragePointer.md)

  - [StoragePointer0Offset](./core-starknet-storage-StoragePointer0Offset.md)

  - [StoragePath](./core-starknet-storage-StoragePath.md)

  - [PendingStoragePath](./core-starknet-storage-PendingStoragePath.md)

  - [Mutable](./core-starknet-storage-Mutable.md)

  - [Vec](./core-starknet-storage-vec-Vec.md)

  - [StorageBase](./core-starknet-storage-storage_base-StorageBase.md)

  - [FlattenedStorage](./core-starknet-storage-storage_base-FlattenedStorage.md)

  - [Map](./core-starknet-storage-map-Map.md)

  - [ByteArray](./core-byte_array-ByteArray.md)

- [Enums](./enums.md)

  - [bool](./core-bool.md)

  - [never](./core-never.md)

  - [AddInputResult](./core-circuit-AddInputResult.md)

  - [FromNullableResult](./core-nullable-FromNullableResult.md)

  - [Result](./core-result-Result.md)

  - [Option](./core-option-Option.md)

  - [PanicResult](./core-panics-PanicResult.md)

  - [OptionRev](./core-internal-OptionRev.md)

  - [IsZeroResult](./core-zeroable-IsZeroResult.md)

- [Type aliases](./type_aliases.md)

  - [usize](./core-usize.md)

  - [u96](./core-circuit-u96.md)

  - [ConstZero](./core-circuit-ConstZero.md)

  - [ConstOne](./core-circuit-ConstOne.md)

  - [NonZeroEcPoint](./core-ec-NonZeroEcPoint.md)

  - [SyscallResult](./core-starknet-SyscallResult.md)

- [Impl aliases](./impl_aliases.md)

  - [U8Zeroable](./core-integer-U8Zeroable.md)

  - [U16Zeroable](./core-integer-U16Zeroable.md)

  - [U32Zeroable](./core-integer-U32Zeroable.md)

  - [U64Zeroable](./core-integer-U64Zeroable.md)

  - [U128Zeroable](./core-integer-U128Zeroable.md)

  - [U256Zeroable](./core-integer-U256Zeroable.md)

  - [ContractAddressZeroable](./core-starknet-contract_address-ContractAddressZeroable.md)

  - [EthAddressZeroable](./core-starknet-eth_address-EthAddressZeroable.md)

  - [ClassHashZeroable](./core-starknet-class_hash-ClassHashZeroable.md)

  - [Felt252Zeroable](./core-zeroable-Felt252Zeroable.md)

- [Traits](./traits.md)

  - [Copy](./core-traits-Copy.md)

  - [Drop](./core-traits-Drop.md)

  - [Add](./core-traits-Add.md)

  - [AddEq](./core-traits-AddEq.md)

  - [Sub](./core-traits-Sub.md)

  - [SubEq](./core-traits-SubEq.md)

  - [Mul](./core-traits-Mul.md)

  - [MulEq](./core-traits-MulEq.md)

  - [Div](./core-traits-Div.md)

  - [DivEq](./core-traits-DivEq.md)

  - [Rem](./core-traits-Rem.md)

  - [RemEq](./core-traits-RemEq.md)

  - [DivRem](./core-traits-DivRem.md)

  - [PartialEq](./core-traits-PartialEq.md)

  - [BitAnd](./core-traits-BitAnd.md)

  - [BitOr](./core-traits-BitOr.md)

  - [BitXor](./core-traits-BitXor.md)

  - [BitNot](./core-traits-BitNot.md)

  - [PartialOrd](./core-traits-PartialOrd.md)

  - [Into](./core-traits-Into.md)

  - [TryInto](./core-traits-TryInto.md)

  - [Neg](./core-traits-Neg.md)

  - [Not](./core-traits-Not.md)

  - [traits::IndexView](./core-traits-IndexView.md)

  - [traits::Index](./core-traits-Index.md)

  - [Destruct](./core-traits-Destruct.md)

  - [PanicDestruct](./core-traits-PanicDestruct.md)

  - [Default](./core-traits-Default.md)

  - [Felt252DictValue](./core-traits-Felt252DictValue.md)

  - [BoolTrait](./core-boolean-BoolTrait.md)

  - [CircuitElementTrait](./core-circuit-CircuitElementTrait.md)

  - [CircuitOutputsTrait](./core-circuit-CircuitOutputsTrait.md)

  - [CircuitInputs](./core-circuit-CircuitInputs.md)

  - [AddInputResultTrait](./core-circuit-AddInputResultTrait.md)

  - [EvalCircuitTrait](./core-circuit-EvalCircuitTrait.md)

  - [BoxTrait](./core-box-BoxTrait.md)

  - [NullableTrait](./core-nullable-NullableTrait.md)

  - [ToSpanTrait](./core-array-ToSpanTrait.md)

  - [ArrayTrait](./core-array-ArrayTrait.md)

  - [SpanTrait](./core-array-SpanTrait.md)

  - [Felt252DictTrait](./core-dict-Felt252DictTrait.md)

  - [Felt252DictEntryTrait](./core-dict-Felt252DictEntryTrait.md)

  - [ResultTrait](./core-result-ResultTrait.md)

  - [OptionTrait](./core-option-OptionTrait.md)

  - [Clone](./core-clone-Clone.md)

  - [EcStateTrait](./core-ec-EcStateTrait.md)

  - [EcPointTrait](./core-ec-EcPointTrait.md)

  - [NumericLiteral](./core-integer-NumericLiteral.md)

  - [BoundedInt](./core-integer-BoundedInt.md)

  - [AbsAndSign](./core-integer-AbsAndSign.md)

  - [num::traits::zero::Zero](./core-num-traits-zero-Zero.md)

  - [num::traits::one::One](./core-num-traits-one-One.md)

  - [num::traits::bit_size::BitSize](./core-num-traits-bit_size-BitSize.md)

  - [Bounded](./core-num-traits-bounded-Bounded.md)

  - [num::traits::ops::overflowing::OverflowingAdd](./core-num-traits-ops-overflowing-OverflowingAdd.md)

  - [num::traits::ops::overflowing::OverflowingSub](./core-num-traits-ops-overflowing-OverflowingSub.md)

  - [num::traits::ops::overflowing::OverflowingMul](./core-num-traits-ops-overflowing-OverflowingMul.md)

  - [num::traits::ops::wrapping::WrappingAdd](./core-num-traits-ops-wrapping-WrappingAdd.md)

  - [num::traits::ops::wrapping::WrappingSub](./core-num-traits-ops-wrapping-WrappingSub.md)

  - [num::traits::ops::wrapping::WrappingMul](./core-num-traits-ops-wrapping-WrappingMul.md)

  - [num::traits::ops::checked::CheckedAdd](./core-num-traits-ops-checked-CheckedAdd.md)

  - [num::traits::ops::checked::CheckedSub](./core-num-traits-ops-checked-CheckedSub.md)

  - [num::traits::ops::checked::CheckedMul](./core-num-traits-ops-checked-CheckedMul.md)

  - [num::traits::ops::pow::Pow](./core-num-traits-ops-pow-Pow.md)

  - [num::traits::ops::saturating::SaturatingAdd](./core-num-traits-ops-saturating-SaturatingAdd.md)

  - [num::traits::ops::saturating::SaturatingSub](./core-num-traits-ops-saturating-SaturatingSub.md)

  - [num::traits::ops::saturating::SaturatingMul](./core-num-traits-ops-saturating-SaturatingMul.md)

  - [num::traits::ops::widemul::WideMul](./core-num-traits-ops-widemul-WideMul.md)

  - [num::traits::ops::widesquare::WideSquare](./core-num-traits-ops-widesquare-WideSquare.md)

  - [num::traits::ops::sqrt::Sqrt](./core-num-traits-ops-sqrt-Sqrt.md)

  - [num::traits::zero::Zero](./core-num-traits-zero-Zero.md)

  - [num::traits::one::One](./core-num-traits-one-One.md)

  - [num::traits::bit_size::BitSize](./core-num-traits-bit_size-BitSize.md)

  - [num::traits::ops::overflowing::OverflowingAdd](./core-num-traits-ops-overflowing-OverflowingAdd.md)

  - [num::traits::ops::overflowing::OverflowingSub](./core-num-traits-ops-overflowing-OverflowingSub.md)

  - [num::traits::ops::overflowing::OverflowingMul](./core-num-traits-ops-overflowing-OverflowingMul.md)

  - [num::traits::ops::wrapping::WrappingAdd](./core-num-traits-ops-wrapping-WrappingAdd.md)

  - [num::traits::ops::wrapping::WrappingSub](./core-num-traits-ops-wrapping-WrappingSub.md)

  - [num::traits::ops::wrapping::WrappingMul](./core-num-traits-ops-wrapping-WrappingMul.md)

  - [num::traits::ops::checked::CheckedAdd](./core-num-traits-ops-checked-CheckedAdd.md)

  - [num::traits::ops::checked::CheckedSub](./core-num-traits-ops-checked-CheckedSub.md)

  - [num::traits::ops::checked::CheckedMul](./core-num-traits-ops-checked-CheckedMul.md)

  - [num::traits::ops::saturating::SaturatingAdd](./core-num-traits-ops-saturating-SaturatingAdd.md)

  - [num::traits::ops::saturating::SaturatingSub](./core-num-traits-ops-saturating-SaturatingSub.md)

  - [num::traits::ops::saturating::SaturatingMul](./core-num-traits-ops-saturating-SaturatingMul.md)

  - [num::traits::ops::pow::Pow](./core-num-traits-ops-pow-Pow.md)

  - [num::traits::ops::sqrt::Sqrt](./core-num-traits-ops-sqrt-Sqrt.md)

  - [num::traits::ops::widemul::WideMul](./core-num-traits-ops-widemul-WideMul.md)

  - [num::traits::ops::widesquare::WideSquare](./core-num-traits-ops-widesquare-WideSquare.md)

  - [ops::index::Index](./core-ops-index-Index.md)

  - [ops::index::IndexView](./core-ops-index-IndexView.md)

  - [AddAssign](./core-ops-arith-AddAssign.md)

  - [SubAssign](./core-ops-arith-SubAssign.md)

  - [MulAssign](./core-ops-arith-MulAssign.md)

  - [DivAssign](./core-ops-arith-DivAssign.md)

  - [RemAssign](./core-ops-arith-RemAssign.md)

  - [Deref](./core-ops-deref-Deref.md)

  - [SnapshotDeref](./core-ops-deref-SnapshotDeref.md)

  - [DerefMut](./core-ops-deref-DerefMut.md)

  - [FnOnce](./core-ops-function-FnOnce.md)

  - [Fn](./core-ops-function-Fn.md)

  - [ops::index::IndexView](./core-ops-index-IndexView.md)

  - [ops::index::Index](./core-ops-index-Index.md)

  - [Serde](./core-serde-Serde.md)

  - [HashStateTrait](./core-hash-HashStateTrait.md)

  - [Hash](./core-hash-Hash.md)

  - [LegacyHash](./core-hash-LegacyHash.md)

  - [HashStateExTrait](./core-hash-HashStateExTrait.md)

  - [PedersenTrait](./core-pedersen-PedersenTrait.md)

  - [PoseidonTrait](./core-poseidon-PoseidonTrait.md)

  - [PrintTrait](./core-debug-PrintTrait.md)

  - [Display](./core-fmt-Display.md)

  - [Debug](./core-fmt-Debug.md)

  - [LowerHex](./core-fmt-LowerHex.md)

  - [SyscallResultTrait](./core-starknet-SyscallResultTrait.md)

  - [starknet::storage_access::Store](./core-starknet-storage_access-Store.md)

  - [starknet::event::Event](./core-starknet-event-Event.md)

  - [starknet::account::AccountContract](./core-starknet-account-AccountContract.md)

  - [starknet::storage_access::Store](./core-starknet-storage_access-Store.md)

  - [StorePacking](./core-starknet-storage_access-StorePacking.md)

  - [Secp256Trait](./core-starknet-secp256_trait-Secp256Trait.md)

  - [Secp256PointTrait](./core-starknet-secp256_trait-Secp256PointTrait.md)

  - [starknet::event::Event](./core-starknet-event-Event.md)

  - [EventEmitter](./core-starknet-event-EventEmitter.md)

  - [starknet::account::AccountContract](./core-starknet-account-AccountContract.md)

  - [AccountContractDispatcherTrait](./core-starknet-account-AccountContractDispatcherTrait.md)

  - [AccountContractSafeDispatcherTrait](./core-starknet-account-AccountContractSafeDispatcherTrait.md)

  - [StorageAsPointer](./core-starknet-storage-StorageAsPointer.md)

  - [StoragePointerReadAccess](./core-starknet-storage-StoragePointerReadAccess.md)

  - [StoragePointerWriteAccess](./core-starknet-storage-StoragePointerWriteAccess.md)

  - [StorageAsPath](./core-starknet-storage-StorageAsPath.md)

  - [PendingStoragePathTrait](./core-starknet-storage-PendingStoragePathTrait.md)

  - [VecTrait](./core-starknet-storage-vec-VecTrait.md)

  - [MutableVecTrait](./core-starknet-storage-vec-MutableVecTrait.md)

  - [StorageNode](./core-starknet-storage-storage_node-StorageNode.md)

  - [StorageNodeMut](./core-starknet-storage-storage_node-StorageNodeMut.md)

  - [SubPointers](./core-starknet-storage-sub_pointers-SubPointers.md)

  - [SubPointersMut](./core-starknet-storage-sub_pointers-SubPointersMut.md)

  - [SubPointersForward](./core-starknet-storage-sub_pointers-SubPointersForward.md)

  - [SubPointersMutForward](./core-starknet-storage-sub_pointers-SubPointersMutForward.md)

  - [StorageTrait](./core-starknet-storage-storage_base-StorageTrait.md)

  - [StorageTraitMut](./core-starknet-storage-storage_base-StorageTraitMut.md)

  - [StorageMapReadAccess](./core-starknet-storage-map-StorageMapReadAccess.md)

  - [StorageMapWriteAccess](./core-starknet-storage-map-StorageMapWriteAccess.md)

  - [StoragePathEntry](./core-starknet-storage-map-StoragePathEntry.md)

  - [AddHelper](./core-internal-bounded_int-AddHelper.md)

  - [SubHelper](./core-internal-bounded_int-SubHelper.md)

  - [MulHelper](./core-internal-bounded_int-MulHelper.md)

  - [DivRemHelper](./core-internal-bounded_int-DivRemHelper.md)

  - [ConstrainHelper](./core-internal-bounded_int-ConstrainHelper.md)

  - [TrimHelper](./core-internal-bounded_int-TrimHelper.md)

  - [NegateHelper](./core-internal-bounded_int-NegateHelper.md)

  - [Zeroable](./core-zeroable-Zeroable.md)

  - [Bytes31Trait](./core-bytes_31-Bytes31Trait.md)

  - [ByteArrayTrait](./core-byte_array-ByteArrayTrait.md)

  - [StringLiteral](./core-string-StringLiteral.md)

  - [AppendFormattedToByteArray](./core-to_byte_array-AppendFormattedToByteArray.md)

  - [FormatAsByteArray](./core-to_byte_array-FormatAsByteArray.md)

  - [TypeEqual](./core-metaprogramming-TypeEqual.md)

  - [IsTuple](./core-metaprogramming-IsTuple.md)

  - [TupleSplit](./core-metaprogramming-TupleSplit.md)

  - [TupleExtendFront](./core-metaprogramming-TupleExtendFront.md)

  - [TupleSnapForward](./core-metaprogramming-TupleSnapForward.md)

  - [SnapRemove](./core-metaprogramming-SnapRemove.md)

  - [Iterator](./core-iter-traits-iterator-Iterator.md)

  - [IntoIterator](./core-iter-traits-iterator-IntoIterator.md)

- [Impls](./impls.md)

  - [BoolSerde](./core-BoolSerde.md)

  - [BoolBitAnd](./core-BoolBitAnd.md)

  - [BoolBitOr](./core-BoolBitOr.md)

  - [BoolNot](./core-BoolNot.md)

  - [BoolBitXor](./core-BoolBitXor.md)

  - [BoolPartialEq](./core-BoolPartialEq.md)

  - [BoolFelt252DictValue](./core-BoolFelt252DictValue.md)

  - [BoolIntoFelt252](./core-BoolIntoFelt252.md)

  - [Felt252Serde](./core-Felt252Serde.md)

  - [Felt252Add](./core-Felt252Add.md)

  - [Felt252AddEq](./core-Felt252AddEq.md)

  - [Felt252Sub](./core-Felt252Sub.md)

  - [Felt252SubEq](./core-Felt252SubEq.md)

  - [Felt252Mul](./core-Felt252Mul.md)

  - [Felt252MulEq](./core-Felt252MulEq.md)

  - [Felt252Neg](./core-Felt252Neg.md)

  - [Felt252PartialEq](./core-Felt252PartialEq.md)

  - [Felt252TryIntoNonZero](./core-Felt252TryIntoNonZero.md)

  - [Felt252Default](./core-Felt252Default.md)

  - [Felt252Felt252DictValue](./core-Felt252Felt252DictValue.md)

  - [boolCopy](./core-boolCopy.md)

  - [boolDrop](./core-boolDrop.md)

  - [boolDefault](./core-boolDefault.md)

  - [felt252Copy](./core-felt252Copy.md)

  - [felt252Drop](./core-felt252Drop.md)

  - [CircuitElementDrop](./core-circuit-CircuitElementDrop.md)

  - [CircuitElementCopy](./core-circuit-CircuitElementCopy.md)

  - [DestructFailureGuarantee](./core-circuit-DestructFailureGuarantee.md)

  - [Felt252Zero](./core-felt_252-Felt252Zero.md)

  - [Felt252One](./core-felt_252-Felt252One.md)

  - [SpanIndex](./core-array-SpanIndex.md)

  - [DestructOption](./core-option-DestructOption.md)

  - [EcStateImpl](./core-ec-EcStateImpl.md)

  - [EcPointImpl](./core-ec-EcPointImpl.md)

  - [U128TryIntoNonZero](./core-integer-U128TryIntoNonZero.md)

  - [U32TryIntoNonZero](./core-integer-U32TryIntoNonZero.md)

  - [U256TryIntoNonZero](./core-integer-U256TryIntoNonZero.md)

  - [Felt252TryIntoU8](./core-integer-Felt252TryIntoU8.md)

  - [U8IntoFelt252](./core-integer-U8IntoFelt252.md)

  - [Felt252TryIntoU16](./core-integer-Felt252TryIntoU16.md)

  - [U16IntoFelt252](./core-integer-U16IntoFelt252.md)

  - [Felt252TryIntoU32](./core-integer-Felt252TryIntoU32.md)

  - [U32IntoFelt252](./core-integer-U32IntoFelt252.md)

  - [Felt252TryIntoU64](./core-integer-Felt252TryIntoU64.md)

  - [U64IntoFelt252](./core-integer-U64IntoFelt252.md)

  - [Felt252TryIntoU128](./core-integer-Felt252TryIntoU128.md)

  - [U128IntoFelt252](./core-integer-U128IntoFelt252.md)

  - [Felt252IntoU256](./core-integer-Felt252IntoU256.md)

  - [U256TryIntoFelt252](./core-integer-U256TryIntoFelt252.md)

  - [I8IntoFelt252](./core-integer-I8IntoFelt252.md)

  - [I16IntoFelt252](./core-integer-I16IntoFelt252.md)

  - [I32IntoFelt252](./core-integer-I32IntoFelt252.md)

  - [I64IntoFelt252](./core-integer-I64IntoFelt252.md)

  - [I128IntoFelt252](./core-integer-I128IntoFelt252.md)

  - [PedersenImpl](./core-pedersen-PedersenImpl.md)

  - [PoseidonImpl](./core-poseidon-PoseidonImpl.md)

  - [Felt252PrintImpl](./core-debug-Felt252PrintImpl.md)

  - [BoolPrintImpl](./core-debug-BoolPrintImpl.md)

  - [ContractAddressPrintImpl](./core-debug-ContractAddressPrintImpl.md)

  - [U8PrintImpl](./core-debug-U8PrintImpl.md)

  - [U16PrintImpl](./core-debug-U16PrintImpl.md)

  - [U32PrintImpl](./core-debug-U32PrintImpl.md)

  - [U64PrintImpl](./core-debug-U64PrintImpl.md)

  - [U128PrintImpl](./core-debug-U128PrintImpl.md)

  - [U256PrintImpl](./core-debug-U256PrintImpl.md)

  - [I8PrintImpl](./core-debug-I8PrintImpl.md)

  - [I16PrintImpl](./core-debug-I16PrintImpl.md)

  - [I32PrintImpl](./core-debug-I32PrintImpl.md)

  - [I64PrintImpl](./core-debug-I64PrintImpl.md)

  - [I128PrintImpl](./core-debug-I128PrintImpl.md)

  - [ArrayGenericPrintImpl](./core-debug-ArrayGenericPrintImpl.md)

  - [Secp256k1Impl](./core-starknet-secp256k1-Secp256k1Impl.md)

  - [Secp256k1PointImpl](./core-starknet-secp256k1-Secp256k1PointImpl.md)

  - [Secp256r1Impl](./core-starknet-secp256r1-Secp256r1Impl.md)

  - [Secp256r1PointImpl](./core-starknet-secp256r1-Secp256r1PointImpl.md)

  - [Felt252TryIntoContractAddress](./core-starknet-contract_address-Felt252TryIntoContractAddress.md)

  - [ContractAddressIntoFelt252](./core-starknet-contract_address-ContractAddressIntoFelt252.md)

  - [Felt252TryIntoEthAddress](./core-starknet-eth_address-Felt252TryIntoEthAddress.md)

  - [EthAddressIntoFelt252](./core-starknet-eth_address-EthAddressIntoFelt252.md)

  - [U256IntoEthAddress](./core-starknet-eth_address-U256IntoEthAddress.md)

  - [EthAddressSerde](./core-starknet-eth_address-EthAddressSerde.md)

  - [EthAddressPrintImpl](./core-starknet-eth_address-EthAddressPrintImpl.md)

  - [Felt252TryIntoClassHash](./core-starknet-class_hash-Felt252TryIntoClassHash.md)

  - [ClassHashIntoFelt252](./core-starknet-class_hash-ClassHashIntoFelt252.md)

  - [StorableStoragePointerReadAccess](./core-starknet-storage-StorableStoragePointerReadAccess.md)

  - [NonZeroIntoImpl](./core-zeroable-NonZeroIntoImpl.md)

  - [Bytes31Impl](./core-bytes_31-Bytes31Impl.md)

  - [Bytes31IndexView](./core-bytes_31-Bytes31IndexView.md)

  - [Bytes31IntoFelt252](./core-bytes_31-Bytes31IntoFelt252.md)

  - [Bytes31IntoU256](./core-bytes_31-Bytes31IntoU256.md)

  - [Felt252TryIntoBytes31](./core-bytes_31-Felt252TryIntoBytes31.md)

  - [U8IntoBytes31](./core-bytes_31-U8IntoBytes31.md)

  - [U128IntoBytes31](./core-bytes_31-U128IntoBytes31.md)

  - [ByteArrayStringLiteral](./core-byte_array-ByteArrayStringLiteral.md)

  - [ByteArrayImpl](./core-byte_array-ByteArrayImpl.md)

  - [ByteArrayIndexView](./core-byte_array-ByteArrayIndexView.md)

- [Extern types](./extern_types.md)

  - [RangeCheck](./core-RangeCheck.md)

  - [SegmentArena](./core-SegmentArena.md)

  - [felt252](./core-felt252.md)

  - [RangeCheck96](./core-circuit-RangeCheck96.md)

  - [AddMod](./core-circuit-AddMod.md)

  - [MulMod](./core-circuit-MulMod.md)

  - [CircuitModulus](./core-circuit-CircuitModulus.md)

  - [Circuit](./core-circuit-Circuit.md)

  - [CircuitInput](./core-circuit-CircuitInput.md)

  - [Box](./core-box-Box.md)

  - [Nullable](./core-nullable-Nullable.md)

  - [Array](./core-array-Array.md)

  - [Felt252Dict](./core-dict-Felt252Dict.md)

  - [SquashedFelt252Dict](./core-dict-SquashedFelt252Dict.md)

  - [Felt252DictEntry](./core-dict-Felt252DictEntry.md)

  - [EcOp](./core-ec-EcOp.md)

  - [EcPoint](./core-ec-EcPoint.md)

  - [EcState](./core-ec-EcState.md)

  - [u128](./core-integer-u128.md)

  - [U128MulGuarantee](./core-integer-U128MulGuarantee.md)

  - [Bitwise](./core-integer-Bitwise.md)

  - [u8](./core-integer-u8.md)

  - [u16](./core-integer-u16.md)

  - [u32](./core-integer-u32.md)

  - [u64](./core-integer-u64.md)

  - [i8](./core-integer-i8.md)

  - [i16](./core-integer-i16.md)

  - [i32](./core-integer-i32.md)

  - [i64](./core-integer-i64.md)

  - [i128](./core-integer-i128.md)

  - [BuiltinCosts](./core-gas-BuiltinCosts.md)

  - [GasBuiltin](./core-gas-GasBuiltin.md)

  - [Sha256StateHandle](./core-sha256-Sha256StateHandle.md)

  - [Pedersen](./core-pedersen-Pedersen.md)

  - [Poseidon](./core-poseidon-Poseidon.md)

  - [System](./core-starknet-System.md)

  - [starknet::storage_access::StorageAddress](./core-starknet-storage_access-StorageAddress.md)

  - [starknet::contract_address::ContractAddress](./core-starknet-contract_address-ContractAddress.md)

  - [starknet::class_hash::ClassHash](./core-starknet-class_hash-ClassHash.md)

  - [starknet::storage_access::StorageAddress](./core-starknet-storage_access-StorageAddress.md)

  - [StorageBaseAddress](./core-starknet-storage_access-StorageBaseAddress.md)

  - [Secp256k1Point](./core-starknet-secp256k1-Secp256k1Point.md)

  - [Secp256r1Point](./core-starknet-secp256r1-Secp256r1Point.md)

  - [starknet::contract_address::ContractAddress](./core-starknet-contract_address-ContractAddress.md)

  - [starknet::class_hash::ClassHash](./core-starknet-class_hash-ClassHash.md)

  - [BoundedInt](./core-internal-bounded_int-BoundedInt.md)

  - [NonZero](./core-zeroable-NonZero.md)

  - [bytes31](./core-bytes_31-bytes31.md)

- [Extern functions](./extern_functions.md)

  - [bool_and_impl](./core-bool_and_impl.md)

  - [bool_or_impl](./core-bool_or_impl.md)

  - [bool_not_impl](./core-bool_not_impl.md)

  - [bool_xor_impl](./core-bool_xor_impl.md)

  - [bool_to_felt252](./core-bool_to_felt252.md)

  - [felt252_const](./core-felt252_const.md)

  - [felt252_add](./core-felt252_add.md)

  - [felt252_sub](./core-felt252_sub.md)

  - [felt252_mul](./core-felt252_mul.md)

  - [felt252_div](./core-felt252_div.md)

  - [felt252_is_zero](./core-felt252_is_zero.md)

  - [dup](./core-dup.md)

  - [drop](./core-drop.md)

  - [null](./core-nullable-null.md)

  - [nullable_from_box](./core-nullable-nullable_from_box.md)

  - [match_nullable](./core-nullable-match_nullable.md)

  - [array_snapshot_pop_front](./core-array-array_snapshot_pop_front.md)

  - [felt252_dict_new](./core-dict-felt252_dict_new.md)

  - [felt252_dict_squash](./core-dict-felt252_dict_squash.md)

  - [ec_point_unwrap](./core-ec-ec_point_unwrap.md)

  - [u128_to_felt252](./core-integer-u128_to_felt252.md)

  - [u128_overflowing_add](./core-integer-u128_overflowing_add.md)

  - [u128_overflowing_sub](./core-integer-u128_overflowing_sub.md)

  - [u128_sqrt](./core-integer-u128_sqrt.md)

  - [u128_safe_divmod](./core-integer-u128_safe_divmod.md)

  - [u128_is_zero](./core-integer-u128_is_zero.md)

  - [u128_byte_reverse](./core-integer-u128_byte_reverse.md)

  - [u8_overflowing_add](./core-integer-u8_overflowing_add.md)

  - [u8_overflowing_sub](./core-integer-u8_overflowing_sub.md)

  - [u8_wide_mul](./core-integer-u8_wide_mul.md)

  - [u8_sqrt](./core-integer-u8_sqrt.md)

  - [u8_safe_divmod](./core-integer-u8_safe_divmod.md)

  - [u16_overflowing_add](./core-integer-u16_overflowing_add.md)

  - [u16_overflowing_sub](./core-integer-u16_overflowing_sub.md)

  - [u16_wide_mul](./core-integer-u16_wide_mul.md)

  - [u16_sqrt](./core-integer-u16_sqrt.md)

  - [u16_safe_divmod](./core-integer-u16_safe_divmod.md)

  - [u32_overflowing_add](./core-integer-u32_overflowing_add.md)

  - [u32_overflowing_sub](./core-integer-u32_overflowing_sub.md)

  - [u32_wide_mul](./core-integer-u32_wide_mul.md)

  - [u32_sqrt](./core-integer-u32_sqrt.md)

  - [u32_safe_divmod](./core-integer-u32_safe_divmod.md)

  - [u64_overflowing_add](./core-integer-u64_overflowing_add.md)

  - [u64_overflowing_sub](./core-integer-u64_overflowing_sub.md)

  - [u64_wide_mul](./core-integer-u64_wide_mul.md)

  - [u64_sqrt](./core-integer-u64_sqrt.md)

  - [u64_safe_divmod](./core-integer-u64_safe_divmod.md)

  - [u256_sqrt](./core-integer-u256_sqrt.md)

  - [upcast](./core-integer-upcast.md)

  - [downcast](./core-integer-downcast.md)

  - [i8_wide_mul](./core-integer-i8_wide_mul.md)

  - [i8_diff](./core-integer-i8_diff.md)

  - [i16_wide_mul](./core-integer-i16_wide_mul.md)

  - [i16_diff](./core-integer-i16_diff.md)

  - [i32_wide_mul](./core-integer-i32_wide_mul.md)

  - [i32_diff](./core-integer-i32_diff.md)

  - [i64_wide_mul](./core-integer-i64_wide_mul.md)

  - [i64_diff](./core-integer-i64_diff.md)

  - [i128_diff](./core-integer-i128_diff.md)

  - [withdraw_gas](./core-gas-withdraw_gas.md)

  - [withdraw_gas_all](./core-gas-withdraw_gas_all.md)

  - [redeposit_gas](./core-gas-redeposit_gas.md)

  - [get_builtin_costs](./core-gas-get_builtin_costs.md)

  - [panic](./core-panics-panic.md)

  - [pedersen](./core-pedersen-pedersen.md)

  - [hades_permutation](./core-poseidon-hades_permutation.md)

  - [print](./core-debug-print.md)

  - [starknet::contract_address::contract_address_const](./core-starknet-contract_address-contract_address_const.md)

  - [storage_base_address_const](./core-starknet-storage_access-storage_base_address_const.md)

  - [storage_base_address_from_felt252](./core-starknet-storage_access-storage_base_address_from_felt252.md)

  - [storage_address_to_felt252](./core-starknet-storage_access-storage_address_to_felt252.md)

  - [storage_address_from_base_and_offset](./core-starknet-storage_access-storage_address_from_base_and_offset.md)

  - [storage_address_from_base](./core-starknet-storage_access-storage_address_from_base.md)

  - [storage_address_try_from_felt252](./core-starknet-storage_access-storage_address_try_from_felt252.md)

  - [call_contract_syscall](./core-starknet-syscalls-call_contract_syscall.md)

  - [deploy_syscall](./core-starknet-syscalls-deploy_syscall.md)

  - [emit_event_syscall](./core-starknet-syscalls-emit_event_syscall.md)

  - [get_block_hash_syscall](./core-starknet-syscalls-get_block_hash_syscall.md)

  - [get_execution_info_syscall](./core-starknet-syscalls-get_execution_info_syscall.md)

  - [get_execution_info_v2_syscall](./core-starknet-syscalls-get_execution_info_v2_syscall.md)

  - [library_call_syscall](./core-starknet-syscalls-library_call_syscall.md)

  - [send_message_to_l1_syscall](./core-starknet-syscalls-send_message_to_l1_syscall.md)

  - [storage_read_syscall](./core-starknet-syscalls-storage_read_syscall.md)

  - [storage_write_syscall](./core-starknet-syscalls-storage_write_syscall.md)

  - [replace_class_syscall](./core-starknet-syscalls-replace_class_syscall.md)

  - [get_class_hash_at_syscall](./core-starknet-syscalls-get_class_hash_at_syscall.md)

  - [keccak_syscall](./core-starknet-syscalls-keccak_syscall.md)

  - [sha256_process_block_syscall](./core-starknet-syscalls-sha256_process_block_syscall.md)

  - [starknet::contract_address::contract_address_const](./core-starknet-contract_address-contract_address_const.md)

  - [contract_address_to_felt252](./core-starknet-contract_address-contract_address_to_felt252.md)

  - [contract_address_try_from_felt252](./core-starknet-contract_address-contract_address_try_from_felt252.md)

  - [class_hash_const](./core-starknet-class_hash-class_hash_const.md)

  - [class_hash_to_felt252](./core-starknet-class_hash-class_hash_to_felt252.md)

  - [class_hash_try_from_felt252](./core-starknet-class_hash-class_hash_try_from_felt252.md)

  - [cheatcode](./core-starknet-testing-cheatcode.md)

  - [revoke_ap_tracking](./core-internal-revoke_ap_tracking.md)

  - [require_implicit](./core-internal-require_implicit.md)

  - [bytes31_const](./core-bytes_31-bytes31_const.md)

  - [get_available_gas](./core-testing-get_available_gas.md)

