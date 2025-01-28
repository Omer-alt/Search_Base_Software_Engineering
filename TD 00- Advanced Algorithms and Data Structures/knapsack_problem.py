def knapsack(items, max_weight):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.

    Args:
        items (list of tuples): Each tuple contains (value, weight) of an item.
        max_weight (int): The maximum weight capacity of the knapsack.

    Returns:
        tuple: Maximum value and the list of items included in the optimal solution.
    """
    # Number of items
    n = len(items)

    dp = [[0 for _ in range(max_weight + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, max_weight + 1):
            value, weight = items[i - 1]  

            if weight <= w:
                # Item can be included: take the max of including or excluding the item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                # Item cannot be included: carry forward the previous value
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the items included in the optimal solution
    w = max_weight
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # If value changed, item was included
            selected_items.append(items[i - 1])
            w -= items[i - 1][1]  

    # Reverse the selected items to maintain original order
    selected_items.reverse()

    return dp[n][max_weight], selected_items

if __name__ == "__main__":
    # Test 1
    items1 = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
    max_weight1 = 50
    max_value1, selected_items1 = knapsack(items1, max_weight1)
    print(f"Maximum Value: {max_value1}")
    print(f"Selected Items: {selected_items1}")

    # Test 2
    items2 = [(20, 5), (30, 10), (50, 15), (70, 20)]
    max_weight2 = 25
    max_value2, selected_items2 = knapsack(items2, max_weight2)
    print(f"Maximum Value: {max_value2}")
    print(f"Selected Items: {selected_items2}")
