import functools

x = open(0).read()
blocks = x.split("\n\n")
orderings = [list(map(int, o.split('|'))) for o in blocks[0].splitlines()]
updates = [[int(c) for c in u.split(",")] for u in blocks[1].splitlines()]
# print(orderings)
# print(updates)

# # PART I

comp = {}
for a,b in orderings:
    comp[(a,b)] = -1
    comp[(b,a)] = 1

def compare(a,b):
    return comp.get((a,b),0)

def isordered(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            k = (nums[i], nums[j])
            if k in comp and comp[k] == 1:
                return False
    return True

total = 0
for u in updates:
    if isordered(u):
        total += u[len(u)//2]

print("Part I:", total)


# # PART II

total = 0
for u in updates:
    if not isordered(u):
        u.sort(key=functools.cmp_to_key(compare))
        total += u[len(u)//2]

print("Part II:", total)