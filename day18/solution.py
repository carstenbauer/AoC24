import heapq

L = 71
N = 1024
# L = 7
# N = 12

bytes = [list(map(int, l.split(","))) for l in open(0).read().splitlines()]

grid = [['.' for c in range(L)] for r in range(L)]
for r,c in bytes[:N]:
    grid[r][c] = '#'
# for r in grid:
#     print(*r, sep='')
# print()

def minsteps(grid):
    L = len(grid)
    xit = (L-1, L-1)
    q = [(0,0,0,[])] # dist, r, c, path
    seen = set()

    while len(q) > 0:
        dist,r,c,path = heapq.heappop(q)
        if (r,c) == xit:
            return dist, path+[xit]
        if (r,c) in seen:
            continue
        seen.add((r,c))
        for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
            nr = r + dr
            nc = c + dc
            if not nr in range(L) or not nc in range(L): continue
            if grid[nr][nc] == '#': continue
            heapq.heappush(q,(dist+1,nr,nc,path+[(r,c)]))
    return (-1,[])

print("Part I: ", minsteps(grid)[1])


## Part 2

grid = [['.' for c in range(L)] for r in range(L)]
cpath = []
for (i,(r,c)) in enumerate(bytes):
    grid[r][c] = '#'
    if not (r,c) in cpath and len(cpath) > 0: continue
    dist, cpath = minsteps(grid)
    if dist == -1:
        print("Part II:", (r,c), i)
        break