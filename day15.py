import heapq

grid = [[int(x) for x in list(line)] for line in [x.strip() for x in open('data.in').readlines()]]


def solve(n_tiles):
    cost = [[-1 for _ in range(n_tiles * len(grid[0]))] for _ in range(n_tiles * len(grid))]
    queue = [(0, 0, 0)]
    while queue:
        dist, i, j = heapq.heappop(queue)
        if not (0 <= i < n_tiles * len(grid) and 0 <= j < n_tiles * len(grid[0])):
            continue

        val = grid[i % len(grid)][j % len(grid[0])] + (i // len(grid)) + (j // len(grid[0]))
        while val > 9:
            val -= 9
        rc_cost = dist + val

        if cost[i][j] == -1 or rc_cost < cost[i][j]:
            cost[i][j] = rc_cost
        else:
            continue
        if i == n_tiles * len(grid) - 1 and j == n_tiles * len(grid[0]) - 1:
            break

        for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            heapq.heappush(queue, (cost[i][j], i + x, j + y))
    return cost[n_tiles * len(grid) - 1][n_tiles * len(grid[0]) - 1] - grid[0][0]


print(solve(1))
print(solve(5))
