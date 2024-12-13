import re

total = 0
total2 = 0

def solve(ax, ay, bx, by, px, py):
    ca = (px * by - py * bx) / (ax * by - ay * bx)
    cb = (px - ax * ca) / bx
    if ca % 1 == 0 and cb % 1 == 0: # require integers
        return int(3 * ca + cb)
    else:
        return 0

for machine in open(0).read().split('\n\n'):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", machine))
    total += solve(ax, ay, bx, by, px, py)
    total2 += solve(ax, ay, bx, by, px+10000000000000, py+10000000000000)

print("Part I:", total)
print("Part II:", total2)