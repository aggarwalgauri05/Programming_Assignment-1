def find_min_max(numbers):
    if not numbers:
        return None, None  # If the list is empty, return None for both min and max

    min_val = numbers[0]
    max_val = numbers[0]

    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val

# Example usage:
numbers_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value, max_value = find_min_max(numbers_list)
print(f"The minimum value is: {min_value}")
print(f"The maximum value is: {max_value}")
