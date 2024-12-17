import heapq

grid = [[c for c in l] for l in open(0).read().splitlines()]

# # for r in grid:
# #     print(*r, sep='')

nrows = len(grid)
ncols = len(grid[0])

r = -1
c = -1
for i in range(nrows):
    for j in range(ncols):
        if grid[i][j] == 'S':
            r = i
            c = j

def shortest_path(grid, r0, c0, dr0, dc0):
    q = [(0,r0,c0,dr0,dc0)]
    seen = {(r0,c0,dr0,dc0)}
    while q:
        state = heapq.heappop(q)
        score, r, c, dr, dc = state
        seen.add((r,c,dr,dc))
        if grid[r][c] == 'E':
            return score
        for nscore, nr, nc, ndr, ndc in ((score+1,r+dr,c+dc,dr,dc), (score+1000, r,c,dc,-dr), (score+1000, r,c,-dc,dr)):
            if grid[nr][nc] == '#': continue
            if (nr, nc, ndr, ndc) in seen: continue
            heapq.heappush(q, (nscore, nr, nc, ndr, ndc))

print("Part I:", shortest_path(grid,r,c,0,1))


## Part II

def shortest_path2(grid, r0, c0, dr0, dc0):
    q = [(0,r0,c0,dr0,dc0,[(r0,c0)])]
    seen = {(r0,c0,dr0,dc0)}
    lowest_score = -1
    best_paths_tiles = set()
    while q:
        state = heapq.heappop(q)
        score, r, c, dr, dc, path = state
        seen.add((r,c,dr,dc))
        if grid[r][c] == 'E':
            if lowest_score == -1:
                lowest_score = score
            if score == lowest_score:
                for p in path:
                    best_paths_tiles.add(p)
            elif score > lowest_score:
                return best_paths_tiles
        for nscore, nr, nc, ndr, ndc in ((score+1,r+dr,c+dc,dr,dc), (score+1000, r,c,dc,-dr), (score+1000, r,c,-dc,dr)):
            if grid[nr][nc] == '#': continue
            if (nr, nc, ndr, ndc) in seen: continue
            heapq.heappush(q, (nscore, nr, nc, ndr, ndc, path+[(nr, nc)]))

best_paths_tiles = shortest_path2(grid,r,c,0,1)

for tr, tc in best_paths_tiles:
    grid[tr][tc] = 'O'

for r in grid:
    print(*r, sep='')

print("Part II:", len(best_paths_tiles))