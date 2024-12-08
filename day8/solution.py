grid = [list(l) for l in open(0).read().splitlines()]
nrows = len(grid)
ncols = len(grid[0])
positions = {}

for r in range(nrows):
    for c in range(ncols):
        x = grid[r][c]
        if x == '.' or x == '#':
            continue
        if x in positions:
            positions[x].add((r,c))
        else:
            positions[x] = set([(r,c)])

antinodes = set()
for (x, pos) in positions.items():
    for p in pos:
        for q in pos:
            if p == q:
                continue
            rdiff = p[0] - q[0]
            cdiff = p[1] - q[1]
            ar = p[0] + rdiff
            ac = p[1] + cdiff
            if 0 <= ar < nrows and 0 <= ac < ncols:
                antinodes.add((ar, ac))

print("Part I:", len(antinodes))


## Part II

antinodes = set()
for (x, pos) in positions.items():
    for p in pos:
        for q in pos:
            if p == q:
                continue
            rdiff = p[0] - q[0]
            cdiff = p[1] - q[1]
            ar = p[0] + rdiff
            ac = p[1] + cdiff
            while 0 <= ar < nrows and 0 <= ac < ncols:                
                if grid[ar][ac] == '.':
                    antinodes.add((ar, ac))
                ar = ar + rdiff
                ac = ac + cdiff

antenna_count = sum(len(v) for v in positions.values())

print("Part II:", len(antinodes) + antenna_count)