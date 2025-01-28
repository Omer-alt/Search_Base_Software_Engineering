def merge_intervals(intervals):
    """
    Merge overlapping intervals.

    Args:
        intervals (list of tuples): Each tuple contains (start_time, end_time).

    Returns:
        list of tuples: The merged list of intervals.
    """
    if not intervals:
        return []

    # Sort intervals by their start time
    intervals.sort(key=lambda x: x[0])

    # Initialize merged intervals list with the first interval
    merged = [intervals[0]]


    for current in intervals[1:]:
        previous = merged[-1]

        # Check if the current interval overlaps with the previous one
        if current[0] <= previous[1]:  
            # Merge intervals by updating the end time of the last interval in merged
            merged[-1] = (previous[0], max(previous[1], current[1]))
        else:
            
            merged.append(current)

    return merged


if __name__ == "__main__":
    # Test 1: Intervals with overlaps
    intervals1 = [(1, 3), (2, 6), (8, 10), (15, 18)]
    merged1 = merge_intervals(intervals1)
    print(f"Original: {intervals1}")
    print(f"Merged: {merged1}")

    # Test 2: Intervals with no overlaps
    intervals2 = [(1, 2), (3, 4), (5, 6)]
    merged2 = merge_intervals(intervals2)
    print(f"Original: {intervals2}")
    print(f"Merged: {merged2}")

    # Test 3: Fully overlapping intervals
    intervals3 = [(1, 10), (2, 6), (3, 8)]
    merged3 = merge_intervals(intervals3)
    print(f"Original: {intervals3}")
    print(f"Merged: {merged3}")

    # Test 4: Single interval
    intervals4 = [(1, 5)]
    merged4 = merge_intervals(intervals4)
    print(f"Original: {intervals4}")
    print(f"Merged: {merged4}")

    # Test 5: Empty list
    intervals5 = []
    merged5 = merge_intervals(intervals5)
    print(f"Original: {intervals5}")
    print(f"Merged: {merged5}")
