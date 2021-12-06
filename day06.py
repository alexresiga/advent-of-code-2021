lines = [x.strip() for x in open('data.in').readlines()]
f = [*map(lines[0].count, '012345678')]
for _ in range(256):
    f = f[1:] + f[:1]
    f[6] += f[-1]
print(sum(f))
