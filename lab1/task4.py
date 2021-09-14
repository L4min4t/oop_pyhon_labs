def pack_my_knapsack(bars, knapsack_capacity):
    """
    This function calculates the maximum weight that fits in the knapsack
    """
    memory_table = [[0 for i in range(knapsack_capacity + 1)] for j in range(len(bars))]
    for index_row in range (len(bars)):
        for index_col in range (knapsack_capacity + 1):
            if index_row == 0:
                if bars[index_row] <= index_col:
                    memory_table[index_row][index_col] = bars[index_row]
            else:
                if bars[index_row] + memory_table[index_row - 1][index_col - bars[index_row]] <= index_col:
                    memory_table[index_row][index_col] = max(bars[index_row] + memory_table[index_row - 1][index_col - bars[index_row]], memory_table[index_row - 1][index_col])
                elif bars[index_row] + memory_table[index_row - 1][index_col] <= index_col:
                    memory_table[index_row][index_col] = max(bars[index_row] + memory_table[index_row - 1][index_col], memory_table[index_row - 1][index_col])
                else:
                    memory_table[index_row][index_col] = memory_table[index_row - 1][index_col]
    return memory_table[-1][-1]


def main():
    print("Max weight", (pack_my_knapsack([int(x) for x in input("Enter weight of bars: ").split()], int(input("Enter knapsack capacity: ")))))


if __name__ == '__main__':
    main()