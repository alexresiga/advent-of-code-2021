from parse import findall

data = open('data.in').read()
dots = findall('{:d},{:d}', data)
folds = findall('{:l}={:d}', data)

for i, fold in enumerate(folds):
    axis, line = fold
    dots = {(min(x, 2 * line - x) if axis == 'x' else x, min(y, 2 * line - y) if axis == 'y' else y) for x, y in dots}
    print(len(dots) if i == 0 else '', end='\n' if i == 0 else '')

for y in range(6):
    print(*[' #'[(x, y) in dots] for x in range(40)])
