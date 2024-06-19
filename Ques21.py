def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage:
numbers_list = [1, 2, 3, 4, 2, 2, 5, 2]
element_to_count = 2
count = count_occurrences(numbers_list, element_to_count)
print(f"The element {element_to_count} occurs {count} times in the list.")
