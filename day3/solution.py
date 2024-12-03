# PART I

import re

x = open(0).read()

def summul(x):
    pairs = re.findall(r'mul\((\d+),(\d+)\)', x)
    return sum(int(x)*int(y) for x,y in pairs)

print("Part I: ", summul(x))


# PART II

# dontsplit = x.split("don't")
# s = summul(dontsplit[0])
# for dns in dontsplit[1:]:
#     ds = dns.split("do()")
#     if len(ds) == 1:
#         continue
#     s += sum(summul(x) for x in ds[1:])

def summul_doordont(x):
    mul = True
    result = 0
    match = re.findall(r"(do\(\))|(don't\(\))|mul\((\d+),(\d+)\)", x)
    for m in match:
        if "do()" in m:
            mul = True
        elif "don't()" in m:
            mul = False
        elif mul:
            result += int(m[2]) * int(m[3])
    return result

print("Part II: ", summul_doordont(x))