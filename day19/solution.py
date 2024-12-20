from collections import defaultdict

towelsstr, designsstr = open(0).read().split("\n\n")

towels = towelsstr.split(", ")
designs = designsstr.splitlines()

def ispossible(design, towels):
    todo = [design]
    while len(todo) > 0:
        rest = todo.pop()
        if len(rest) == 0:
            return True
        for t in towels:
            if rest.startswith(t):
                todo.append(rest.removeprefix(t))
    return False

print("Part I:", sum(ispossible(d, towels) for d  in designs))

## Part II

def nways(rest, towels, memory = defaultdict(int)):
    if len(rest) == 0:
        return 1
    if rest in memory:
        return memory[rest]
    results = []
    for t in towels:
        if rest.startswith(t):
            results.append(nways(rest.removeprefix(t), towels, memory))
    s = sum(results)
    memory[rest] += s
    return s

print("Part II:", sum(nways(d, towels) for d in designs))