# Read the input data into a matrix of characters
const data = stack(eachline(stdin), dims=1)
const nrows = size(data, 1)
const ncols = size(data, 2)

# Find initial position and direction
const pos = findfirst(==('^'), data)
const dir = '^'

# Direction deltas
const delta = Dict('^' => (-1, 0), '>' => (0, 1), '<' => (0, -1), 'v' => (1, 0))

# Part I: Walk in one direction until out of bounds or hitting a wall
function walk1(data, pos, dir)
    r = pos[1]
    c = pos[2]
    dr, dc = delta[dir]
    seen_pos = Set()
    inbounds = true
    while inbounds
        push!(seen_pos, (r, c))
        newr = r + dr
        newc = c + dc
        if !(1 <= newr <= nrows && 1 <= newc <= ncols)
            break
        end
        if data[newr,newc] == '#'
            dc, dr = -dr, dc
            continue
        end
        # print((r, c))
        r, c = newr, newc
    end
    return length(seen_pos)
end

println("Part I: ", walk1(data, pos, dir))

# Part II: Walk in one direction and detect cycles
function walk2(pos, dir)
    r = pos[1]
    c = pos[2]
    dr, dc = delta[dir]
    seen_state = Set()
    inbounds = true
    while inbounds
        if (r, c, dr, dc) in seen_state
            return true
        end
        push!(seen_state, (r, c, dr, dc))
        newr = r + dr
        newc = c + dc
        if !(1 <= newr <= nrows && 1 <= newc <= ncols)
            break
        end
        if data[newr, newc] == '#'
            dc, dr = -dr, dc
            continue
        end
        r, c = newr, newc
    end
    return false
end

function part2(data, pos, dir)
    total = 0
    for r in 1:nrows
        for c in 1:ncols
            if data[r,c] == '#' || data[r,c] == '^'
                continue
            end
            data[r,c] = '#'
            if walk2(pos, dir)
                total += 1
            end
            data[r,c] = '.'
        end
    end
    return total
end

println("Part II: ", part2(data, pos, dir))
