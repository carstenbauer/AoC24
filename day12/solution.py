grid = list(map(list, open(0).read().splitlines()))
nrows = len(grid)
ncols = len(grid[0])

total = 0
points = set([(r,c) for r in range(nrows) for c in range(ncols)])
regions = {}
iregion = 0

while len(points) > 0:
    r, c = points.pop()
    if any((r, c) in region for region in regions.values()): continue
    char = grid[r][c]
    regions[iregion] = set([(r,c)])
    todo = set([(r,c)])
    area = 1
    perim = 4
    while len(todo) > 0:
        cr, cc = todo.pop()
        # print("\t", (cr, cc), perim)
        for dr, dc in ((0,1), (0,-1), (1,0), (-1,0)):
            nr = cr+dr
            nc = cc+dc
            if nr < 0 or nr >= nrows or nc < 0 or nc >= ncols: continue
            if grid[nr][nc] != char: continue
            perim -= 1
            if (nr, nc) in regions[iregion]: continue
            perim += 4
            regions[iregion].add((nr,nc))
            area += 1
            # print("\tadding perim", perim, (nr, nc))
            # perim += perim
            todo.add((nr, nc))
    # print("area: ", area)
    # print("perimeter: ", perim)
    iregion += 1
    total += area * perim

print("Part I:", total)

# for k,v in regions.items():
    # print(k, v)

# print(regions[1])