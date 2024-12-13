grid = list(map(list, open(0).read().splitlines()))
nrows = len(grid)
ncols = len(grid[0])

# (Second attempt)

from collections import defaultdict

cr = {} # connected regions
def dfs(r,c,char,i):
    if 0 <= r < nrows and 0 <= c < ncols:
        if (r,c) in cr: return
        if grid[r][c] == char:
            cr[(r, c)] = i
            for dr, dc in ((0,1), (0,-1), (1,0), (-1,0)):
                dfs(r + dr, c + dc, char, i)

iregion = 0
for r in range(nrows):
    for c in range(ncols):
        if (r,c) not in cr:
            dfs(r,c,grid[r][c],iregion)
            iregion += 1

# invert cr
crr = defaultdict(set)
for p,i in cr.items():
    crr[i].add(p)

# for x in crr.values():
#     print(x)

total = 0
for nodes in crr.values():
    area = len(nodes)
    perim = 0
    for r,c in nodes:
        for dr, dc in ((0,1), (0,-1), (1,0), (-1,0)):
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= nrows or nc < 0 or nc >= ncols or (nr,nc) not in nodes:
                perim += 1
    total += area * perim

print("Part I:", total)


## Part II

total = 0
for nodes in crr.values():
    area = len(nodes)
    perim = set()
    for r,c in nodes:
        for dr, dc in ((0,1), (0,-1), (1,0), (-1,0)):
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= nrows or nc < 0 or nc >= ncols or (nr,nc) not in nodes:
                perim.add(((r,c), (nr,nc)))
    perim2 = set()
    for p1, p2 in perim:
        doadd = True
        for dr, dc in ((1,0), (0,1)):
            np1 = (p1[0]+dr, p1[1]+dc)
            np2 = (p2[0]+dr, p2[1]+dc)
            if (np1, np2) in perim:
                doadd = False
        if doadd:
            perim2.add((p1,p2))
    total += len(perim2) * area

print("Part II:", total)