"""
Selection Sort      O(n²)
    simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element
    from the unsorted portion of the list and moving it to the sorted portion of the list.
"""


def selection_sort_asc(arr: list[int], is_reversed=False) -> None:
    """
    sorts a list by selecting max (min) number and moving it to the beginning

    @arr: list[int]
    @is_reversed: bool
    """
    if not arr:
        return
    for i in range(0, len(arr) - 1):
        curr_min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                curr_min_idx = j
        arr[i], arr[curr_min_idx] = arr[curr_min_idx], arr[i]
    if is_reversed:
        arr.reverse()


if __name__ == '__main__':
    list_to_be_sorted = [2, 4, 7, 5, 72, 23, 8, 4]
    selection_sort_asc(list_to_be_sorted)
    print(list_to_be_sorted)

    list_to_be_sorted = [2, 4, 7, 5, 72, 23, 8, 4]
    selection_sort_asc(list_to_be_sorted, is_reversed=True)
    print(list_to_be_sorted)
