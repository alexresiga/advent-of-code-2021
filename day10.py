lines = [x.strip() for x in open('data.in').readlines()]
b = {'(': ')', '{': '}', '[': ']', '<': '>'}
part1_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
part2_score = {'(': 1, '[': 2, '{': 3, '<': 4}
part1 = 0
part2 = []
for line in lines:
    stack = []
    ok = True
    for e in line:
        if e in b.keys():
            stack.append(e)
        if e in b.values() and stack:
            v = stack.pop()
            if e != b[v]:
                ok = False
                part1 += part1_score[e]
    if ok:
        score = 0
        for c in reversed(stack):
            score = 5 * score + part2_score[c]
        part2.append(score)
print(part1)
print(sorted(part2)[len(part2) // 2])
