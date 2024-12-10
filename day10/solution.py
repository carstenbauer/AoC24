from collections import deque

grid = [list(map(int, list(l))) for l in open(0).read().splitlines()]
nrows = len(grid)
ncols = len(grid[0])
# print(grid)

trailheads = []
for r in range(nrows):
    for c in range(ncols):
        if grid[r][c] == 0:
            trailheads += [(r, c)]
# print(trailheads)

def part1(trailhead):
    q = deque()
    q.append((trailhead[0], trailhead[1]))
    goals = set()
    while len(q) > 0:
        pr, pc = q.pop()
        height = grid[pr][pc]
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr = pr + dr
            nc = pc + dc
            if not 0 <= nr < nrows: continue
            if not 0 <= nc < ncols: continue
            if not grid[nr][nc] == height + 1: continue
            if grid[nr][nc] == 9:
                goals.add((nr, nc))
            else:
                q.append((nr, nc))
    return len(goals)

print("Part I", sum(part1(th) for th in trailheads))


## Part II

def part2(trailhead):
    q = deque()
    id = 0
    q.append((trailhead[0], trailhead[1], id))
    paths = []
    while len(q) > 0:
        pr, pc, i = q.pop()
        height = grid[pr][pc]
        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr = pr + dr
            nc = pc + dc
            if not 0 <= nr < nrows: continue
            if not 0 <= nc < ncols: continue
            if not grid[nr][nc] == height + 1: continue
            if grid[nr][nc] == 9:
                paths.append(i)
            else:
                id += 1
                q.append((nr, nc, id))
    return len(paths)

print("Part II", sum(part2(th) for th in trailheads))