def quick_sort(arr: list, start: int = 0, end: int = None) -> None:
    # Stops when start pivot comes to
    # the end position

    # Workaround to get list length
    if end is None:
        # Ends at len n-1 because the last one
        # element is the pivot.
        end = len(arr) - 1
    # Check if list has more than one element
    # E.g. List with just one element [n]
    # ...The same as: start=0 < end=len(arr)-1
    # ...           : 0 < 1-1
    # ...           : 0 < 0 (False)
    if start < end:
        # Call quicksort for the left and
        # right sublists,
        # and return pivot position from left to right
        pivot_index = partition(arr, start, end)
        # left partition
        quick_sort(arr, start, pivot_index - 1)
        # right partition
        quick_sort(arr, pivot_index + 1, end)


def partition(arr, start, end):
    # End position pivot
    pivot = arr[end]
    # Left to right index
    start_index = start

    # Swap until list[n-1]
    for i in range(start, end):
        # Check from left to right,
        # each list element, and
        # sort list using start_index element
        if arr[i] <= pivot:
            arr[i], arr[start_index] = arr[start_index], arr[i]
            # Next position
            start_index += 1

    # Change pivot position
    arr[start_index], arr[end] = arr[end], arr[start_index]

    return start_index
