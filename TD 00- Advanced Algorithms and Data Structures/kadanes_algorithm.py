

def max_subarray_sum(nums):
    """
    Finds the maximum sum of any contiguous subarray using Kadane's Algorithm.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The maximum subarray sum.
    """
    max_sum = -2**31  # Smallest possible integer value
    current_sum = 0

    for num in nums:
        current_sum += num  
        max_sum = max(max_sum, current_sum)  
        if current_sum < 0:  # Reset current_sum to 0 if it becomes negative
            current_sum = 0

    return max_sum


if __name__ == "__main__":
    # Test 1: Mixed positive and negative numbers
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Maximum Subarray Sum:", max_subarray_sum(nums1))  # Output: 6

    # Test 2: All positive numbers
    nums2 = [1, 2, 3, 4]
    print("Maximum Subarray Sum:", max_subarray_sum(nums2))  # Output: 10

    # Test 3: All negative numbers
    nums3 = [-1, -2, -3, -4]
    print("Maximum Subarray Sum:", max_subarray_sum(nums3))  # Output: -1


