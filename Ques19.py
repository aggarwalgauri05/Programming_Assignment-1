
import string
def remove_punctuation(s):
    return ''.join(char for char in s if char not in string.punctuation)

# Example usage:
input_string = "Hello, world! This is a test string."
clean_string = remove_punctuation(input_string)
print(clean_string)
