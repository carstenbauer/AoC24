data = [[c for c in l] for l in open(0).read().splitlines()]
nrows = len(data)
ncols = len(data[0])

def find_element(matrix, el):
    for row_idx, row in enumerate(matrix):
        if el in row:
            col_idx = row.index(el)
            return row_idx, col_idx
    return None

pos = find_element(data, '^')
dir = '^'

delta = {'^': (-1,0), '>': (0,1), '<': (0,-1), 'v': (1,0)}
# newdir = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

def walk1(pos, dir):
    r, c = pos
    dr, dc = delta[dir]
    seen_pos = set()
    inbounds = True
    while inbounds:
        seen_pos.add((r, c))
        newr = r + dr
        newc = c + dc
        if not (0 <= newr < nrows and 0 <= newc < ncols):
            break
        if data[newr][newc] == '#':
            dc, dr = -dr, dc
            continue
        r = newr
        c = newc
    return len(seen_pos)

print("Part I:", walk1(pos, dir))



# PART II

def walk2(pos, dir):
    r, c = pos
    dr, dc = delta[dir]
    seen_state = set()
    inbounds = True
    while inbounds:
        if (r, c, dr, dc) in seen_state:
            return True
        seen_state.add((r, c, dr, dc))
        newr = r + dr
        newc = c + dc
        if not (0 <= newr < nrows and 0 <= newc < ncols):
            break
        if data[newr][newc] == '#':
            dc, dr = -dr, dc
            continue
        r = newr
        c = newc
    return False

# very slow but works....
total = 0
for r in range(nrows):
    for c in range(ncols):
        if data[r][c] == '#' or data[r][c] == '^':
            continue
        data[r][c] = '#'
        if walk2(pos, dir):
            total += 1
        data[r][c] = '.'
print("Part II:", total)