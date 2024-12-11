# stones = list(map(int, open(0).read().split()))
# print(stones)
# def nblinks(stones, n):
#     def blink(stones):
#         i = 0
#         while True:
#             if i >= len(stones):
#                 break
#             if stones[i] == 0:
#                 stones[i] = 1
#                 i += 1
#                 continue
#             digits = list(str(stones[i]))
#             if len(digits) % 2 == 0:
#                 h = len(digits) // 2
#                 l = int(''.join(digits[:h]))
#                 r = int(''.join(digits[h:]))
#                 stones[i] = r
#                 stones.insert(i, l)
#                 i += 2
#                 continue
#             stones[i] *= 2024
#             i += 1
#     for b in range(n):
#         blink(stones)
#         # print(b+1, stones)
#     return len(stones)
#
# print("Part I:", nblinks(stones, 25))

stones_str = open(0).read()

def nblinks_optimized(stones_str, n, mem = {}):
    return sum(blinklen(s, n, mem) for s in stones_str.split())

def blinklen(s, n, mem):
    if n == 0:
        return 1
    if (s, n) in mem:
        return mem[(s, n)]
    # otherwise do work
    blen = 0
    if s == '0':
        blen += blinklen('1', n-1, mem)
    elif len(s) % 2 == 0:
        h = len(s) // 2
        l = str(int(s[:h]))
        r = str(int(s[h:]))
        blen += blinklen(l, n-1, mem) + blinklen(r, n-1, mem)
    else:
        blen += blinklen(str(int(s)*2024), n-1, mem)
    mem.setdefault((s, n), blen)
    return blen

print("Part I:", nblinks_optimized(stones_str, 25))
print("Part II:", nblinks_optimized(stones_str, 75))