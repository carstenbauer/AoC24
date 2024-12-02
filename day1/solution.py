# PART I

num_pairs = [list(map(int, line.split())) for line in open(0).read().splitlines()]
# print(num_pairs)
pair_of_lists = list(map(list, zip(*num_pairs)))
# print(pair_of_lists)
sorted_lists = list(map(sorted, pair_of_lists))
# print(sorted_lists)
result = sum(abs(x-y) for x,y in zip(*sorted_lists))
print("Part I: ", result)



# PART II

l, r = sorted_lists
result2 = sum(k * r.count(k) for k in l)
print("Part II:", result2)