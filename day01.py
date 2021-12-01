lines = list(map(int, open('data.in').readlines()))
print(sum(x < y for x, y in zip(lines, lines[1:])))
print(sum(x < y for x, y in zip(lines, lines[3:])))
