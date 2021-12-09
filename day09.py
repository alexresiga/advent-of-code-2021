from math import prod

grid = [[int(x) for x in list(line)] for line in [x.strip() for x in open('data.in').readlines()]]
visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]


def is_low_point(i, j):
    for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= i + d[0] < len(grid) and 0 <= j + d[1] < len(grid[i]):
            if grid[i + d[0]][j + d[1]] <= grid[i][j]:
                return False
    return True


def find_basin(i, j):
    basin = 0
    for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= i + x < len(grid) and 0 <= j + y < len(grid[i]):
            if not visited[i + x][j + y] and grid[i + x][j + y] != 9:
                visited[i + x][j + y] = True
                basin += 1 + find_basin(i + x, j + y)
    return basin


part1 = 0
part2 = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if is_low_point(r, c):
            visited[r][c] = True
            part1 += 1 + grid[r][c]
            part2.append(1 + find_basin(r, c))

print(part1)
print(prod(sorted(part2)[-3:]))
