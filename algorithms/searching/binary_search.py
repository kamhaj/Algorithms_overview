def binary_search(arr: list[int], number_to_be_found):
    """
    use binary search to find a number location (array index) in a sorted array

    :param arr: list[int | float]
    :param number_to_be_found: int | float
    :rtype int
    """
    left_idx, right_idx = 0, len(arr) - 1
    while left_idx <= right_idx:
        middle_idx = left_idx + (right_idx - left_idx) // 2
        if arr[middle_idx] == number_to_be_found:
            return middle_idx
        elif arr[middle_idx] < number_to_be_found:
            left_idx = middle_idx + 1
        else:
            right_idx = middle_idx - 1
    return -1


# Driver Code
if __name__ == '__main__':
    sorted_arr = [2, 4, 4, 5, 7, 7, 8, 23, 72]
    number_to_be_found = 8

    # Function call
    result = binary_search(sorted_arr, number_to_be_found)
    if result != -1:
        print("Element found at index", result)
    else:
        print("Element not found in array")
