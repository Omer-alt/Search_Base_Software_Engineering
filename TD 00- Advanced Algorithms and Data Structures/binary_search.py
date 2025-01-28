



def binary_search(sorted_list, target):
    """
    Perform binary search to find the target in the sorted list.

    Parameters:
        sorted_list (list): A sorted list of integers.
        target (int): The target value to search for.

    Returns:
        int: Index of the target value if found, otherwise -1.
    """
    start_list = 0
    end_list = len(sorted_list) - 1

    while start_list <= end_list:
        mid = start_list + (end_list - start_list) // 2  # Avoids overflow for large indices

        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            start_list = mid + 1
        else:
            end_list = mid - 1

    return -1


if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 7, 9, 11, 13], 7),  
        ([1, 3, 5, 7, 9, 11, 13], 1),  
        ([1, 3, 5, 7, 9, 11, 13], 13), 
        ([1, 3, 5, 7, 9, 11, 13], 8),  # Target does not exist
        ([], 4),                       # Empty list
        ([1], 1),                      
        ([1], 2)                       # Single-element list where target does not exist
    ]

    for sorted_list, target in test_cases:
        result = binary_search(sorted_list, target)
        print(f"Searching for {target} in {sorted_list}: Index {result}")
