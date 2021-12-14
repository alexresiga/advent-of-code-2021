from collections import Counter

template, lines = data = open('data.in').read().strip().split("\n\n")

d = dict(line.split(" -> ") for line in lines.split("\n"))

counter = Counter([template[i:i + 2] for i in range(len(template) - 1)])
for step in range(1, 41):
    new_counter = Counter()
    for pair in counter:
        left, right = pair
        mid = d[pair]
        new_counter[left + mid] += counter[pair]
        new_counter[mid + right] += counter[pair]

    counter = new_counter
    if step in [10, 40]:
        char_counter = Counter()
        for pair in counter:
            left, right = pair
            char_counter[left] += counter[pair]
        char_counter[template[-1]] += 1

        print(max(char_counter.values()) - min(char_counter.values()))
