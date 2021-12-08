lines = [x.strip() for x in open('data.in').readlines()]


def deduce_mapping(patterns):
    mapping = {}  # pattern to digit

    for p, plen in patterns:
        if plen == 2:
            mapping[p] = 1
        elif plen == 3:
            mapping[p] = 7
        elif plen == 4:
            mapping[p] = 4
        elif plen == 7:
            mapping[p] = 8

    digits = {v: k for k, v in mapping.items()}  # digit to pattern

    for p, plen in patterns:
        if p in mapping:
            continue

        if plen == 5:
            # 2 or 3 or 5
            if len(p & digits[1]) == 2:
                mapping[p] = 3
            elif len(p & digits[4]) == 3:
                mapping[p] = 5
            else:
                mapping[p] = 2
        else:
            # 0 or 6 or 9
            if len(p & digits[4]) == 4:
                mapping[p] = 9
            elif len(p & digits[7]) == 2:
                mapping[p] = 6
            else:
                mapping[p] = 0

    return mapping


total = 0
count = 0
to_count = {2, 4, 3, 7}

for line in lines:
    data, output = map(str.split, line.split('|'))
    data = tuple(map(lambda p: (frozenset(p), len(p)), data))
    output = tuple(map(lambda p: (frozenset(p), len(p)), output))
    mappings = deduce_mapping(data)

    count += sum(l in to_count for _, l in output)
    for i in range(4):
        total += mappings[output[i][0]] * 10 ** (3 - i)

print(count)
print(total)
