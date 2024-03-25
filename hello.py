def count_mines(matrix, i, j):
    """
    Count the number of mines around a cell (i, j) in the matrix.
    """
    count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            ni, nj = i + dx, j + dy
            if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and matrix[ni][nj] == 1:
                count += 1
    return count


def mine_sweeper(N, arr):
    """
    Display the minefield with numbers indicating the number of surrounding mines.
    """
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                print('*', end=' ')
            else:
                print(count_mines(arr, i, j), end=' ')
        print()


# Main code
arr = []
N = int(input("N: "))

for _ in range(N):
    row = input(": ")
    arr.append(list(map(int, row.split())))

mine_sweeper(N, arr)