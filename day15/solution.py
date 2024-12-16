griddata, movesdata = open(0).read().split("\n\n")
grid = [[c for c in l] for l in griddata.splitlines()]
nrows = len(grid)
ncols = len(grid[0])

ncols2 = 2 * ncols
grid2 = [['x' for c in range(ncols2)] for r in range(nrows)]

for r in range(nrows):
    for c in range(ncols):
        char = grid[r][c]
        c2 = 2 * c
        if char == '#':
            grid2[r][c2]   = '#'
            grid2[r][c2+1] = '#'
        elif char == 'O':
            grid2[r][c2]   = '['
            grid2[r][c2+1] = ']'
        elif char == '.':
            grid2[r][c2]   = '.'
            grid2[r][c2+1] = '.'
        elif char == '@':
            grid2[r][c2]   = '@'
            grid2[r][c2+1] = '.'

def printgrid(grid):
    for r in grid:
        for c in r:
            print(c, end='')
        print()
    print()

# printgrid(grid)

moves = list(movesdata)

# rr = -1
# rc = -1
# for r in range(nrows):
#     for c in range(ncols):
#         if grid[r][c] == '@':
#             rr = r
#             rc = c

# def trymove(r, c, dr, dc):
#     nr = r + dr
#     nc = c + dc
#     if grid[nr][nc] == '.':
#         grid[r][c] = '.'
#         grid[nr][nc] = 'O'
#         return True
#     if grid[nr][nc] == 'O' and trymove(nr, nc, dr, dc):
#         grid[r][c] = '.'
#         grid[nr][nc] = 'O'
#         return True
#     return False

# for m in moves:
#     # print(m)
#     dr, dc = -1, -1
#     if m == '>':
#         dr = 0
#         dc = 1
#     elif m == 'v':
#         dr = 1
#         dc = 0
#     elif m == '<':
#         dr = 0
#         dc = -1
#     elif m == '^':
#         dr = -1
#         dc = 0
#     elif m == '\n':
#         continue
#     nrr = rr + dr
#     nrc = rc + dc
#     # if grid[nrr][nrc] == '#':
#         # print("wall\n")
#     if grid[nrr][nrc] == '.':
#         # move robot
#         grid[rr][rc] = '.'
#         grid[nrr][nrc] = '@'
#         rr, rc = nrr, nrc
#     elif grid[nrr][nrc] == 'O':
#         if trymove(nrr, nrc, dr, dc):
#             grid[rr][rc] = '.'
#             grid[nrr][nrc] = '@'
#             rr, rc = nrr, nrc
#         # else:
#         #     print("can't move Os\n")
#     # printgrid(grid)
# printgrid(grid)

# total = 0
# for r in range(nrows):
#     for c in range(ncols):
#         if grid[r][c] == 'O':
#             total += 100 * r + c

# print("Part I:", total)



## Part II

printgrid(grid2)

rr = -1
rc = -1
for r in range(nrows):
    for c in range(ncols2):
        if grid2[r][c] == '@':
            rr = r
            rc = c
print(rr, rc)

for m in moves:
    # print(m)
    dr, dc = -1, -1
    if m == '>':
        dr = 0
        dc = 1
    elif m == 'v':
        dr = 1
        dc = 0
    elif m == '<':
        dr = 0
        dc = -1
    elif m == '^':
        dr = -1
        dc = 0
    elif m == '\n': # ARGH! :)
        continue
    Q = [(rr, rc)]
    canmove = True
    for r, c in Q:
        nr = r + dr
        nc = c + dc
        if (nr, nc) in Q: continue
        char = grid2[nr][nc]
        if char == "#":
            canmove = False
            break
        if char == "[":
            Q.append((nr, nc))
            Q.append((nr, nc + 1))
        if char == "]":
            Q.append((nr, nc))
            Q.append((nr, nc - 1))
    if not canmove: continue
    copy = [list(row) for row in grid2]
    grid2[rr][rc] = "."
    grid2[rr + dr][rc + dc] = "@"
    for br, bc in Q[1:]:
        grid2[br][bc] = "."
    for br, bc in Q[1:]:
        grid2[br + dr][bc + dc] = copy[br][bc]
    rr += dr
    rc += dc
    # printgrid(grid2)
printgrid(grid2)

total = 0
for r in range(nrows):
    for c in range(ncols2):
        if grid2[r][c] == '[':
            total += 100 * r + c

print("Part II:", total)