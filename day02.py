lines = [x.strip() for x in open('data.in').readlines()]
h = d = aim = 0
for line in lines:
    match line.split():
        case "forward", amount:
            h += int(amount)
            d += aim * int(amount)
        case "up", amount:
            aim -= int(amount)
        case "down", amount:
            aim += int(amount)

print(h * aim, h * d)
