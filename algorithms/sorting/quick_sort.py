"""
Quicksort      O(n * log(n)) - best and avarage | O(n²) - worst case
    picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot
    in its correct position in the sorted array.

    is 'divide and conquer' algorithm type
"""


def quicksort(arr: list[int], low: int | float, high: int | float, is_reversed=False) -> None:
    """
    sorts a list by choosing a pivot element, storing elements less than pivot in the left array, greater than pivot
    in the right array and using recursion.

    :param arr: list[ int]
    :param low: int
    :param high:  int
    :param is_reversed: bool
    """
    if not arr or len(arr) <= 1:
        return
    if low < high:
        pivot_element_idx = partition(arr, low, high)
        quicksort(arr, low, pivot_element_idx - 1)
        quicksort(arr, pivot_element_idx + 1, high)
    if is_reversed:
        arr.reverse()


def partition(arr, low, high):
    """
     Function to find the partition position

    :param arr: list[int]
    :param low: int
    :param high: int
    :return: int
    """
    pivot_element = arr[high]
    greater_element_pointer = low - 1
    for lesser_element_pointer in range(low, high):
        if arr[lesser_element_pointer] <= pivot_element:
            # swap with pivot element
            greater_element_pointer += 1
            arr[greater_element_pointer], arr[lesser_element_pointer] = (
                arr[lesser_element_pointer], arr[greater_element_pointer])
    # Swap with pivot element
    arr[greater_element_pointer + 1], arr[high] = arr[high], arr[greater_element_pointer + 1]
    # return array partition index
    return greater_element_pointer + 1


if __name__ == '__main__':
    list_to_be_sorted = [2, 4, 11, 7, 5, 72, 23, 8, 4, 9]
    quicksort(list_to_be_sorted, 0, len(list_to_be_sorted) - 1)
    print(list_to_be_sorted)

    list_to_be_sorted = [2, 4, 11, 7, 5, 72, 23, 8, 4, 9]
    quicksort(list_to_be_sorted, 0, len(list_to_be_sorted) - 1, is_reversed=True)
    print(list_to_be_sorted)

    list_to_be_sorted = [2.7, 4.2, 7.5, 5, 72.99, 23.5, 8, 4.12]
    quicksort(list_to_be_sorted, 0, len(list_to_be_sorted) - 1)
    print(list_to_be_sorted)

