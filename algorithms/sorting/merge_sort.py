"""
Merge Sort      O(n * log(n))
    works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays
    back together to form the final sorted array.

    is 'divide and conquer' algorithm type
"""


def merge_sort(arr: list[int | float], is_reversed=False):
    """
    sorts a list by dividing an array into simpler subarrays, sorting them and merging the results

    :param arr: list[int | float]
    :param is_reversed: bool
    """
    if not arr:
        return
    if len(arr) == 1:
        return arr
    arr_middle_idx = len(arr) // 2
    left_arr = arr[:arr_middle_idx]
    right_arr = arr[arr_middle_idx:]
    # recursion
    merge_sort(left_arr)
    merge_sort(right_arr)
    # merge
    merge_arrays(arr, left_arr, right_arr)
    if is_reversed:
        arr.reverse()


def merge_arrays(arr, left_arr, right_arr):
    """
    merge phase of merge sort

    :param arr: list[int | float]
    :param left_arr: left_arr[int | float]
    :param right_arr: right_arr[int | float]
    """
    left_arr_idx = right_arr_idx = 0
    merged_arr_idx = 0
    while left_arr_idx < len(left_arr) and right_arr_idx < len(right_arr):
        if left_arr[left_arr_idx] < right_arr[right_arr_idx]:
            arr[merged_arr_idx] = left_arr[left_arr_idx]
            left_arr_idx += 1
        else:
            arr[merged_arr_idx] = right_arr[right_arr_idx]
            right_arr_idx += 1
        merged_arr_idx += 1
    # append if anything still not merged
    while left_arr_idx < len(left_arr):
        arr[merged_arr_idx] = left_arr[left_arr_idx]
        left_arr_idx += 1
        merged_arr_idx += 1
    while right_arr_idx < len(right_arr):
        arr[merged_arr_idx] = right_arr[right_arr_idx]
        right_arr_idx += 1
        merged_arr_idx += 1


if __name__ == '__main__':
    list_to_be_sorted = [2, 4, 7, 5, 72, 23, 8, 4]
    merge_sort(list_to_be_sorted)
    print(list_to_be_sorted)

    list_to_be_sorted = [2, 4, 7, 5, 72, 23, 8, 4]
    merge_sort(list_to_be_sorted, is_reversed=True)
    print(list_to_be_sorted)

    list_to_be_sorted = [5]
    merge_sort(list_to_be_sorted)
    print(list_to_be_sorted)

    list_to_be_sorted = [2.7, 4.2, 7.5, 5, 72.99, 23.5, 8, 4.12]
    merge_sort(list_to_be_sorted)
    print(list_to_be_sorted)
