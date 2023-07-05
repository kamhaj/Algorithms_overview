"""
Insertion Sort      O(n²)
    - simple sorting algorithm
"""


def insertion_sort_asc(arr: list[int], is_reversed=False) -> None:
    """
    sorts a list by diving it into a sorted and unsorted part

    :param arr: list[int | float]
    :param is_reversed: bool
    """
    if not arr:
        return
    for item_id in range(1, len(arr)):
        swap_index = item_id
        while arr[swap_index-1] > arr[swap_index] and swap_index > 0:
            arr[swap_index], arr[swap_index-1] = arr[swap_index-1], arr[swap_index]
            swap_index -= 1
    if is_reversed:
        arr.reverse()


if __name__ == '__main__':
    list_to_be_sorted = [2, 4, 7, 5, 72, 23, 8, 4]
    insertion_sort_asc(list_to_be_sorted)
    print(list_to_be_sorted)

    list_to_be_sorted = [2, 4, 7, 5, 72, 23, 8, 4]
    insertion_sort_asc(list_to_be_sorted, is_reversed=True)
    print(list_to_be_sorted)

    list_to_be_sorted = ["Poland", "Germany", "Argentina", 'brasil', "England", "Belgium"]  # case sensitive
    insertion_sort_asc(list_to_be_sorted)
    print(list_to_be_sorted)

    list_to_be_sorted = [9]
    insertion_sort_asc(list_to_be_sorted)
    print(list_to_be_sorted)
