from collections import Counter


def sanity_check(grid):
    if not (isinstance(grid, list)
            and len(grid) == 9
            and all(isinstance(row, list)
                    and len(row) == 9
                    for row in grid)
            and all(isinstance(elt, int)
                    and 0 <= elt <= 9
                    for row in grid
                    for elt in row)):
        return None
    return True


def all_different(line):
    freq = Counter(line)
    return all(freq[x] == 1
               for x in freq
               if x > 0)


def get_row(grid, index):
    return grid[index]


def get_column(grid, index):
    return [row[index]
            for row in grid]


def get_block(grid, index):
    r = int(3 * (index / 3))
    c = int(3 * (index % 3))
    return grid[r][c:c + 3] + grid[r + 1][c:c + 3] + grid[r + 2][c:c + 3]


def check_sudoku(grid):
    if sanity_check(grid) is None:
        return None
    return all(
        all_different(get_row(grid, k)) and
        all_different(get_column(grid, k)) and
        all_different(get_block(grid, k))
        for k in range(9))