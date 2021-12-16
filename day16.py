from math import prod


def solve(binary, index):
    global res_version
    current = index
    v = binary[current:current + 3]
    res_version += int(v, 2)
    current += 3
    t = binary[current:current + 3]
    current += 3
    if int(t, 2) == 4:
        value = ''
        c = 0
        for pos in range(0, len(binary[current:]), 5):
            c += 1
            chunk = binary[current + pos:current + pos + 5]
            if len(chunk) != 5:
                break
            value += chunk[1:]
            if chunk[0] == '0':
                break
        current += c * 5
        return current, int(value, 2)
    elif int(t, 2) != 4:
        i = binary[current]
        current += 1
        vals = []
        if int(i, 2) == 0:
            length = binary[current: current + 15]
            current += 15
            assert len(length) == 15
            c = 0
            while c < int(length, 2):
                ll, val = solve(binary, current)
                vals.append(val)
                c += ll - current
                current += ll - current
        else:
            length = binary[current: current + 11]
            current += 11
            assert len(length) == 11
            for i in range(int(length, 2)):
                ll, val = solve(binary, current)
                vals.append(val)
                current += ll - current

        res = 0
        match int(t, 2):
            case 0:
                res = sum(vals)
            case 1:
                res = prod(vals)
            case 2:
                res = min(vals)
            case 3:
                res = max(vals)
            case 5:
                res = vals[0] > vals[1]
            case 6:
                res = vals[0] < vals[1]
            case 7:
                res = vals[0] == vals[1]

        return current, res


lines = open('data.in').read().splitlines()[0]
inp = ''.join(list(map(lambda x: bin(int(x, 16))[2:].zfill(4), list(lines))))
res_version = 0
print(solve(inp, 0)[1])
print(res_version)
