import math

numbers = list(map(int, [x.strip() for x in open('data.in').readlines()][0].split(',')))
part1 = part2 = math.inf
for i in range(min(numbers), max(numbers) + 1):
    part1 = min(sum(map(lambda x: abs(i - x), numbers)), part1)
    part2 = min(sum(map(lambda x: abs(i - x) * (abs(i - x) + 1) // 2, numbers)), part2)
print(part1)
print(part2)
