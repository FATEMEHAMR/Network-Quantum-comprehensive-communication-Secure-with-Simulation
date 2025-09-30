


def apply_repetition_code(binary_key):
    """
    Apply 3-qubit repetition code correction on the key (bit string).
    Majority voting is used to correct errors.
    """
    corrected_key = ''
    for bit in binary_key:
        # Encode: replicate bit 3 times (e.g., '0' -> '000', '1' -> '111')
        encoded_bits = bit * 3

        # Simulate error (randomly flip one bit) - optional demonstration
        # For now, assume at most one error per triplet and correct it
        syndrome = encoded_bits  # here, no error applied for demonstration

        # Majority voting
        votes = [int(b) for b in syndrome]
        corrected_bit = '1' if sum(votes) >= 2 else '0'
        corrected_key += corrected_bit

    return corrected_key
