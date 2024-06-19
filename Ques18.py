def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example usage:
string1 = "listen"
string2 = "silent"
result = are_anagrams(string1, string2)
print(f"Are '{string1}' and '{string2}' anagrams? {result}")
