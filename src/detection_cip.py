import re


"""
# Example usage:
example_string = "My numbers are 1234567, 12345678, and 1234567890123."
unique_numbers = find_unique_numbers(example_string)
print("Unique 7 or 13 digit sequences found:", unique_numbers)

"""

# Function to find unique numbers in text
def find_unique_numbers(string):
    pattern = r'\b\d{7}\b|\b\d{13}\b'
    matches = re.findall(pattern, string)
    matches=list(set(matches))
    return matches
