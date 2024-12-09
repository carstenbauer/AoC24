input = open(0).read()
numbers = [int(c) for c in input]
files = []
spaces = []

for (i,n) in enumerate(numbers):
    if i % 2 == 0:
        files.append(n)
    else:
        spaces.append(n)
# print(files, spaces)
lentotal = len(files) + len(spaces)

compact = []
ilastnonzero = len(files)-1
for (i,f) in enumerate(files):
    if f == 0:
        continue
    compact.extend([i for k in range(f)])
    if i < len(spaces):
        s = spaces[i]
        for j in range(s):
            if files[ilastnonzero] == 0:
                ilastnonzero -= 1
            files[ilastnonzero] -= 1
            compact.append(ilastnonzero)

# print(compact)

print("Part I:", sum(i*compact[i] for i in range(len(compact)))) # 6211348208140


## Part II

# reset
files = []
spaces = []
for (i,n) in enumerate(numbers):
    if i % 2 == 0:
        files.append(n)
    else:
        spaces.append(n)


moves = {} # spaceid: [fids...]
for fid,fsz in reversed(list(enumerate(files))):
    sid = -1
    for j,s in enumerate(spaces):
        if j < fid and s >= fsz:
            sid = j
            break
    if sid >= 0:
        if sid in moves:
            moves[sid] += [fid for k in range(fsz)]
        else:
            moves[sid] = [fid for k in range(fsz)]
        spaces[sid] -= fsz

# compact = []
total = 0
pos = 0
for i in range(lentotal):
    if i % 2 == 0: # file
        fid = i // 2
        v = fid if not any(fid in v for v in moves.values()) else 0
        # compact.extend([v for k in range(files[fid])])
        for k in range(files[fid]):
            total += v * pos
            pos += 1
    else: # space
        sid = i // 2
        if sid in moves:
            # compact.extend(moves[sid])
            for v in moves[sid]:
                total += v * pos
                pos += 1
        # compact.extend([0 for k in range(spaces[sid])])
        for k in range(spaces[sid]):
            total += 0 * pos
            pos += 1

# print(compact)
# print("Part II:", sum(i*v for i,v in enumerate(compact)))
print("Part II:", total)
