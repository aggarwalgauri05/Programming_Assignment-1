
def count_char_frequency(s):
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency
input_string = "hello world"
frequency = count_char_frequency(input_string)
print(frequency)
