def binary_to_signed_decimal(binary_str):
    bit_length = len(binary_str)

    # Check if the number is negative (MSB is 1)
    if binary_str[0] == '1':
        # Convert two’s complement to negative integer
        # Step 1: Invert the bits
        inverted = ''.join('1' if b == '0' else '0' for b in binary_str)
        # Step 2: Convert to int and add 1
        magnitude = int(inverted, 2) + 1
        # Step 3: Make it negative
        return -magnitude
    else:
        # Positive number, just convert normally
        return int(binary_str, 2)

# Example usage:
binary_input = input("Enter a binary number (two’s complement): ")
result = binary_to_signed_decimal(binary_input)
print(f"Signed decimal value: {result}")
