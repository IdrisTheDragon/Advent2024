example_r1=41
example_r2=6

def parse(filename):
    with open(filename,"r") as file:
        return [list(l.strip()) for l in file.readlines()]

def find_guard(map):
    for i in range(0,len(map)):
        for j in range(0,len(map[0])):
            if map[i][j] == "^":
                return (i,j)
    print("NOT FOUND")
    exit(1)

move = [
    [-1,0],
    [0,1],
    [1,0],
    [0,-1]
]

def p1(map):
    (i,j) = find_guard(map)
    #print(i,j)
    dir = 0
    while 0 <= i < len(map) and 0 <= j < len(map[0]):
        map[i][j] = "X"
        ni = i + move[dir][0]
        nj = j + move[dir][1]
        if not (0 <= ni < len(map) and 0 <= nj < len(map[0])):
            #print("next edge",ni,nj)
            break
        elif map[ni][nj] == '#':
            dir= (dir+1)%4
            #print("next wall",ni,nj)
            continue
        i = ni
        j = nj
        #print(i,j)
    
    count = 0
    for l in map:
        for v in l:
            if v == "X":
                count = count + 1
                
    return count

def find_loop(map,i,j):
    dir = 0
    visited = []
    while 0 <= i < len(map) and 0 <= j < len(map[0]):
        visited.append([i,j,dir])
        ni = i + move[dir][0]
        nj = j + move[dir][1]
        if not (0 <= ni < len(map) and 0 <= nj < len(map[0])):
            #print("next edge",ni,nj)
            break
        elif map[ni][nj] == '#':
            dir= (dir+1)%4
            #print("next wall",ni,nj)
            continue
        i = ni
        j = nj
        if [i,j,dir] in visited:
            return True
    return False
    

def p2(map):
    (i,j) = find_guard(map)
    (io,jo) = find_guard(map)
    dir = 0
    obstacles = []
    while 0 <= i < len(map) and 0 <= j < len(map[0]):
        #map[i][j] = "X"
        ni = i + move[dir][0]
        nj = j + move[dir][1]
        if not (0 <= ni < len(map) and 0 <= nj < len(map[0])):
            #print("next edge",ni,nj)
            break
        elif map[ni][nj] == '#':
            dir= (dir+1)%4
            #print("next wall",ni,nj)
            continue
        i = ni
        j = nj
        prev = map[i][j]
        map[i][j] = "#"
        if find_loop(map,io,jo) and [i,j] not in obstacles:
            obstacles.append([i,j])
        map[i][j] = prev
        #print(i,j)
    
    # for i,obstacle in enumerate(obstacles):
    #     map[obstacle[0]][obstacle[1]] = i
        
    # for l in map:
    #     for v in l:
    #         print(v,end="")
    #     print()   
    
    return len(obstacles)

def main():
    # P1
    parsed_input = parse("day6/example.txt")
    r1 = p1(parsed_input)
    assert r1 == example_r1, f"Failed p1 example, Got {r1} expected {example_r1}"
    parsed_input = parse("day6/input.txt")
    r1 = p1(parsed_input)
    print(f"part 1: {r1}")
    
    # P2
    parsed_input = parse("day6/example.txt")
    r2 = p2(parsed_input)
    assert r2 == example_r2, f"Failed p2 example, Got {r2} expected {example_r2}"
    parsed_input = parse("day6/input.txt")
    r2 = p2(parsed_input)
    print(f"part 2: {r2}")

if __name__ == "__main__":
    main()
