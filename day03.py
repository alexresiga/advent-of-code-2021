lines = [x.strip() for x in open('data.in').readlines()]
g = e = ''
for i in range(len(lines[0])):
    column = [x[i] for x in lines]
    if column.count('0') > column.count('1'):
        g += '0'
        e += '1'
    else:
        g += '1'
        e += '0'
print(int(g, 2) * int(e, 2))


def part2(inverse):
    candidates = lines
    for j in range(len(lines[0])):
        if len(candidates) == 1:
            break
        col = [x[j] for x in candidates]
        if col.count('0') > col.count('1'):
            candidates = [x for x in candidates if x[j] == ('0' if not inverse else '1')]
        else:
            candidates = [x for x in candidates if x[j] == ('1' if not inverse else '0')]
    return candidates[0]


print(int(part2(0), 2) * int(part2(1), 2))
