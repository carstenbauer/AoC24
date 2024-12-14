import re

lines = open(0).read().splitlines()

Lx = 101
Ly = 103
# Lx = 11
# Ly = 7
T = 100

states = [] # robot states
for l in lines:
    px, py, vx, vy = map(int, re.findall(r"-?\d+", l))
    states.append((px,py,vx,vy))

n = len(states)

# optional
def visualize(grid):
    for r in grid:
        for v in r:
            print(v, end='')
        print()

def grid(states):
    grid = [['.' for c in range(Lx)] for r in range(Ly)]
    for x,y,vx,vy in states:
        if type(grid[y][x]) == int:
            grid[y][x] += 1
        else:
            grid[y][x] = 1
    return grid

for t in range(100):
    for r in range(n):
        x, y, vx, vy = states[r]
        nx = (x + vx) % Lx
        ny = (y + vy) % Ly
        states[r] = (nx, ny, vx, vy)

def saftey_factor(states):
    q0 = 0
    q1 = 0
    q2 = 0
    q3 = 0
    for x,y,_,_ in states:
        if y < Ly // 2 and x < Lx // 2:
            q0 += 1
        elif y < Ly // 2 and x > Lx // 2:
            q1 += 1
        elif y > Ly // 2 and x < Lx // 2:
            q2 += 1
        elif y > Ly // 2 and x > Lx // 2:
            q3 += 1
    return q0 * q1 * q2 * q3

print("Part I:", saftey_factor(states))



## Part II

# reset input data
states = [] # robot states
for l in lines:
    px, py, vx, vy = map(int, re.findall(r"-?\d+", l))
    states.append((px,py,vx,vy))

sfmin = float("inf")
for t in range(10000):
    for r in range(n):
        x, y, vx, vy = states[r]
        nx = (x + vx) % Lx
        ny = (y + vy) % Ly
        states[r] = (nx, ny, vx, vy)
    sf = saftey_factor(states)
    if sf < sfmin:
        sfmin = sf
        tmin = t+1

print("Part I:", tmin)


# I want to see the christmas tree!

# reset input data
states = [] # robot states
for l in lines:
    px, py, vx, vy = map(int, re.findall(r"-?\d+", l))
    states.append((px,py,vx,vy))

for t in range(tmin):
    for r in range(n):
        x, y, vx, vy = states[r]
        nx = (x + vx) % Lx
        ny = (y + vy) % Ly
        states[r] = (nx, ny, vx, vy)
visualize(grid(states))