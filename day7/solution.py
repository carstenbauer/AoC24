lines = [list(map(int, l.split())) for l in open(0).read().replace(':', '').splitlines()]

def add(a,b):
    return a+b
def mul(a,b):
    return a*b

ops = [add, mul]

def compute_all(nums):
    a = nums[0]
    b = nums[1]
    results = set([op(a,b) for op in ops])
    for n in nums[2:]:
        tmp = set()
        for r in results:
            for op in ops:
                tmp.add(op(r, n))
                # print(results, r, n, op, tmp)
        results = tmp
    return results

total = 0
for l in lines:
    if l[0] in compute_all(l[1:]):
        total += l[0]
print("Part I: ", total)

## Part II

def concat(a,b):
    return int(str(a) + str(b))

ops = [add, mul, concat]

total = 0
for l in lines:
    if l[0] in compute_all(l[1:]):
        total += l[0]
print("Part II: ", total)