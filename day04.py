num, *blocks = open('data.in').read().split('\n\n')
numbers = list(map(int, num.split(',')))
boards = [[list(map(int, row.split())) for row in block.split('\n')] for block in blocks]
visited = {i: [[0 for _ in range(5)] for _ in range(5)] for i in range(len(boards))}
winners = [0 for _ in range(len(boards))]


def check_win(matrix):
    for j in range(5):
        if all(x == 1 for x in matrix[j]) and not winners[i]:
            winners[i] = 1
            unmarked = sum(board[ii][jj] for ii in range(5) for jj in range(5) if visited[i][ii][jj] == 0)
            if len([x for x in winners if x == 0]) == 0:  # part 2
                print(n * unmarked)
            # exit() part 1


for n in numbers:
    for i, board in enumerate(boards):
        for r in range(5):
            for c in range(5):
                if board[r][c] == n:
                    visited[i][r][c] = 1
        check_win(visited[i])
        t = [[visited[i][column][row] for column in range(len(visited[i]))] for row in range(len(visited[i][0]))]
        check_win(t)
