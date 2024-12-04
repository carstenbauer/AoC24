input = open(0).read()
grid = list(map(lambda l: [c for c in l], input.splitlines()))
nrows = len(grid)
ncols = len(grid[0])
# for r in range(nrows):
#     print(grid[r])

# PART I

def safe_get(r, c):
    if 0 <= r < nrows and 0 <= c < ncols:
        return grid[r][c]
    else:
        return ''

total = 0
for r in range(nrows):
    for c in range(ncols):
        if grid[r][c] == 'X':
            for rsign in (0, 1, -1):
                for csign in (0, 1, -1):
                    str = ''.join(safe_get(r+rsign*i, c+csign*i) for i in range(4))
                    total += str == "XMAS"

print("Part I: ", total)


## PART II

total = 0
for r in range(nrows):
    for c in range(ncols):
        if grid[r][c] == 'A':
            str1 = ''.join([safe_get(r+1, c+1), 'A', safe_get(r-1, c-1)])
            str2 = ''.join([safe_get(r-1, c+1), 'A', safe_get(r+1, c-1)])
            if (str1 == "MAS" or str1[::-1] == "MAS") and (str2 == "MAS" or str2[::-1] == "MAS"):
                total += 1

print("Part II: ", total)