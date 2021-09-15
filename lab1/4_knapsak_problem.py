def pack_my_knapsack(bars, knapsack_capacity):
    """
    This function calculates the maximum weight,
    that fits in the knapsack
    """
    memory_table = [[0 for i in range(knapsack_capacity + 1)] for j in range(len(bars))]
    for row in range (len(bars)):
        for col in range (knapsack_capacity + 1):
            if row == 0:
                if bars[row] <= col:
                    memory_table[row][col] = bars[row]
            else:
                if (col - bars[row] >= 0) and (bars[row] + memory_table[row - 1][col - bars[row]] <= col):
                    memory_table[row][col] = max(bars[row] + memory_table[row - 1][col - bars[row]], memory_table[row - 1][col])
                elif bars[row] + memory_table[row - 1][col] <= col:
                    memory_table[row][col] = max(bars[row] + memory_table[row - 1][col], memory_table[row - 1][col])
                else:
                    memory_table[row][col] = memory_table[row - 1][col]
    return memory_table[-1][-1]


print("Max weight", (pack_my_knapsack([int(x) for x in input("Enter weight of bars: ").split()], int(input("Enter knapsack capacity: ")))))