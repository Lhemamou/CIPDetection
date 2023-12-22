from src.detection_cip import find_unique_numbers  

# Test when both 7 and 13 digit numbers are present
def test_both_seven_and_thirteen_digits():
    string = "These are the numbers: 1234567 and 1234567890123."
    assert sorted(find_unique_numbers(string)) == sorted(["1234567", "1234567890123"])

# Test when only 7 digit numbers are present
def test_only_seven_digits():
    string = "Here we have 7654321 and 2345678."
    assert sorted(find_unique_numbers(string)) == sorted(["7654321", "2345678"])

# Test when only 13 digit numbers are present
def test_only_thirteen_digits():
    string = "Long numbers like 1234567890123 are here."
    assert find_unique_numbers(string) == ["1234567890123"]

# Test when no 7 or 13 digit numbers are present
def test_no_matching_digits():
    string = "All these numbers are too short 12345 or too long 12345678901234."
    assert find_unique_numbers(string) == []

# Test with a mixture of number lengths and other text
def test_mixture_of_lengths():
    string = "We have 1234567, a short 123, a too long 123456789012345 and just right 9876543210987 here."
    assert sorted(find_unique_numbers(string)) == sorted(["1234567", "9876543210987"])

# Test with special characters and boundaries
def test_special_boundaries():
    string = "Boundaries matter in 1234567-1234567 and 1234567890123; also 1234567."
    assert sorted(find_unique_numbers(string)) == sorted(["1234567", "1234567890123", "1234567"])

# Test with 7 or 13 digit numbers as part of a longer sequence
def test_part_of_longer_sequence():
    string = "This is a tricky one: 12345678 and 012345678901234 are part of longer sequences."
    assert find_unique_numbers(string) == []

# Test with numbers embedded in words
def test_numbers_in_words():
    string = "Embedded1234567numbers or 1234567890123within should not be matched."
    assert find_unique_numbers(string) == []

# Test with empty string
def test_empty_string():
    string = ""
    assert find_unique_numbers(string) == []
