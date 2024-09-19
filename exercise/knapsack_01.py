def knapsack(capacity, weights, values, i):
    # base case
    if i == 0 or capacity == 0:
        return 0

    if weights[i-1] > capacity:
        # can't add i-1 to the sum
        return knapsack(capacity, weights, values, i-1)
    else:
        return max(
            values[i-1] + knapsack(capacity-weights[i-1], weights, values, i-1),
            knapsack(capacity, weights, values, i-1)
        )


if __name__=="__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    n = len(values)
    print(knapsack(capacity, weights, values, n))
