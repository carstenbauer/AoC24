# PART I

reports = [list(map(int, line.split())) for line in open(0).read().splitlines()]
# print(reports)

def absdiff(lst):
    return [abs(j - i) for i, j in zip(lst, lst[1:])]

def is_safe_report(x):
    if x != sorted(x) and x != sorted(x, reverse=True):
        return False
    if not all([i >= 1 and i <= 3 for i in absdiff(x)]):
        return False
    return True

result = sum(is_safe_report(r) for r in reports)
print("Part I: ", result)



# PART II

result2 = sum(any(is_safe_report(r[:index] + r[index + 1:]) for index in range(len(r))) for r in reports)
print("Part II: ", result2)