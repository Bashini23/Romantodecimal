roman_numeral_map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

def roman_to_decimal(roman_numeral):
  """
  Converts a Roman numeral string to its decimal equivalent.

  Args:
    roman_numeral: The Roman numeral string to convert.

  Returns:
    The decimal equivalent of the Roman numeral.

  Raises:
    ValueError: If the Roman numeral string is invalid.
  """

  # ... (same implementation as before)

# Get user input
roman_numeral = input("Enter a Roman numeral: ").upper()

try:
  decimal_value = roman_to_decimal(roman_numeral)
  print(f"The decimal equivalent of {roman_numeral} is {decimal_value}.")
except ValueError as e:
  print(f"Invalid Roman numeral: {e}")

