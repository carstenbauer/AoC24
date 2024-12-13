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

# print(regions)

def countsides(region, d_start):
    cstart = min([c for r,c in region])
    rstart = min([r for r,c in region if c == cstart])
    # print((rstart, cstart))

    # left and top
    lgrid = [[(False, False) for c in range(ncols)] for r in range(ncols)]

    for r in range(nrows):
        for c in range(ncols):
            inregion = not (r,c) in region
            l = inregion
            t = inregion
            if not (r-1, c) in region:
                t = not t
            if not (r, c-1) in region:
                l = not l
            lgrid[r][c] = (l, t)

    # for r in lgrid:
    #     print(r)
    # exit()

    def check(r, c, i):
        if 0 <= r < nrows and 0 <= c < ncols:
            return lgrid[r][c][i]
        if 0 <= c < ncols and r == nrows and i == 1:
            return True
        if 0 <= r < nrows and c == ncols and i == 0:
            return True
        # if r == nrows and c == ncols and i == 0:
            # return True
        return False
            

    sides = 0
    r = rstart
    c = cstart
    d = d_start
    seen = set()
    while True:
        print((r,c), d)
        # if r == rstart and c == cstart and d == d_start and sides != 0:
            # break
        if (r,c,d) in seen:
            break
        seen.add((r,c,d))
        if d == (1,0): # down
            if not check(r,c,0):
                raise Exception("d:", d, "pos:", (r,c), "but no left border")
            if check(r+1,c,1): # we can't go down because blockade
                if check(r,c+1,0): # we can't go right -> go back up
                    sides += 2
                    d = (-1,0)
                else: # we can go right -> go right
                    sides += 1
                    d = (0,1)
                continue
            if check(r+1,c,0): # we can go down
                r = r+1
                continue
            if check(r+1,c-1,1): # we can go left
                sides += 1
                d = (0,-1)
                r, c = r+1, c-1
                continue
        elif d == (0,-1): # left
            if not check(r,c,1):
                raise Exception("d:", d, "pos:", (r,c), "but no top border")
            if check(r,c,0): # we can't go left because blockade
                if check(r+1,c,1): # we can't go down -> go back right
                    sides += 2
                    d = (0, 1)
                else: # we can go down -> go down
                    sides += 1
                    d = (1,0)
                continue
            if check(r,c-1,1): # we can go left
                c = c-1
                continue
            if check(r-1,c,0): # we can go up
                r,c = r-1,c-1
                d = (-1,0)
                sides += 1
                continue
        elif d == (-1,0): # up
            if not check(r,c+1,0):
                raise Exception("d:", d, "pos:", (r,c), "but no right border")
            if check(r,c,1): # we can't go up because blockade
                # if check(r,c-1,1): # we can't go left -> go back down
                if check(r,c,0): # we can't go left -> go back down
                    sides += 2
                    d = (1,0)
                else: # we can go left -> go left
                    sides += 1
                    d = (0,-1)
                continue
            if check(r-1,c+1,0): # we can go up
                r = r-1
                continue
            if check(r,c+1,1): # we can go right
                sides += 1
                r, c = r-1, c+1
                d = (0,1)
                continue
        elif d == (0,1): # right
            if not check(r+1,c,1):
                raise Exception("d:", d, "pos:", (r,c), "but no bottom border")
            if check(r,c+1,0): # we can't go right because blockade
                if check(r,c,1): # we can't go up -> go back left
                    sides += 2
                    d = (0,-1)
                else: # we can go up -> go up
                    sides += 1
                    d = (-1,0)
                continue
            if check(r+1,c+1,1): # we can go right
                c = c+1
                continue
            if check(r+1,c+1,0): # we can go down
                sides += 1
                r, c = r+1, c+1
                d = (1,0)
                continue
    return sides

print(regions[0])
print("# sides", countsides(regions[0], (1,0)))
# print("# sides", countsides(regions[1], (1,0)))
# print("# sides", countsides(regions[2], (1,0)))
# print("# sides", countsides(regions[3], (0,1)))
# print("# sides", countsides(regions[4], (1,0)))

# # down
# dr = 1
# dc = 0