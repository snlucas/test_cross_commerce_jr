def quick_sort(arr, start=0, end=None):
    # Stops when start pivot comes to
    # the end position

    # Workaround to get list length
    if end is None:
        end = len(arr) - 1
    if start < end:
        # Call quicksort for the left and
        # right partition
        pivot = partition(arr, start, end)
        quick_sort(arr, start, pivot - 1)
        quick_sort(arr, pivot + 1, end)


def partition(arr, start, end):
    pivot = arr[end]
    start_index = start

    # Swap until list[n-1]
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[start_index] = arr[start_index], arr[i]
            start_index += 1  # Next position

    # Change pivot position
    arr[start_index], arr[end] = arr[end], arr[start_index]

    return start_index
