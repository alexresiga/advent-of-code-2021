from itertools import product

grid = [[int(x) for x in list(line)] for line in [x.strip() for x in open('data.in').readlines()]]
res = 0


def flash(i, j):
    global res
    visited[i][j] = True
    res += 1
    for x, y in product([-1, 0, 1], repeat=2):
        if x == y == 0:
            continue
        if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[0]) and not visited[i + x][j + y]:
            grid[i + x][j + y] += 1
            if grid[i + x][j + y] > 9:
                flash(i + x, j + y)
    grid[i][j] = 0


for n in range(1, 1000):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if not visited[r][c]:
                grid[r][c] += 1
            if grid[r][c] > 9:
                flash(r, c)
    if n == 100:
        print(res)
    if all(x == 0 for line in grid for x in line):
        print(n)
        break
