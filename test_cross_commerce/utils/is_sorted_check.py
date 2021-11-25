def is_sorted(arr):
    """
    Check if each comparison returns 1 (True)
    If any comparison is 0 (False), it should not pass.
    """
    # Check if arr isn't None
    if arr:
        if all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)):
            return True
        return False
