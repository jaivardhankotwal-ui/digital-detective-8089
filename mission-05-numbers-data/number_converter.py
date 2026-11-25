#!/usr/bin/env python3
"""
Number Converter CLI
Converts positive decimal numbers into binary and hexadecimal representations.
Created for Digital Detective Assignment - Mission 5.
"""

def convert_number(num: int):
    """Takes an integer and returns its binary and uppercase hexadecimal representations."""
    # bin() returns string with '0b' prefix
    binary_str = bin(num)[2:]
    # hex() returns string with '0x' prefix
    hex_str = hex(num)[2:].upper()
    return binary_str, hex_str

def main():
    print("=========================================")
    print(" Digital Detective — Base Number Converter")
    print("=========================================")
    try:
        user_input = input("Enter a positive decimal integer: ").strip()
        if not user_input.isdigit():
            print("Error: Please enter a valid non-negative integer.")
            return

        decimal_value = int(user_input)
        binary_val, hex_val = convert_number(decimal_value)

        print("\nConversion Results:")
        print(f"Decimal Value     : {decimal_value}")
        print(f"Binary (Base 2)   : {binary_val} (prefix: 0b{binary_val})")
        print(f"Hexadecimal (16)  : {hex_val} (prefix: 0x{hex_val})")
        print("=========================================")
    except (ValueError, KeyboardInterrupt) as e:
        print(f"\nExecution interrupted or invalid input: {e}")

if __name__ == "__main__":
    main()
