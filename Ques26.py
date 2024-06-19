def starts_with_prefix(s, prefix):
    return s[:len(prefix)] == prefix

def ends_with_suffix(s, suffix):
    return s[-len(suffix):] == suffix

# Example usage:
input_string = "Hello, world!"
prefix = "Hello"
suffix = "world!"

print(f"Does '{input_string}' start with '{prefix}'? {starts_with_prefix(input_string, prefix)}")
print(f"Does '{input_string}' end with '{suffix}'? {ends_with_suffix(input_string, suffix)}")
