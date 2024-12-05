example_r1 = 18
example_r2 = 9

import re


def parse(filename):
    with open(filename, "r") as file:
        return [l.strip() for l in file.readlines()]

def find_horizontal(grid):
    count = 0
    # print(grid)
    for l in grid:
        p1 = re.compile("XMAS")
        count = count + len(p1.findall(l))
        p2 = re.compile("SAMX")
        count = count + len(p2.findall(l))
    return count

def p1(parsed_input):
    count = 0
    # Normal
    count = count + find_horizontal(parsed_input)

    # Rotated 90
    rotated90 = ["".join(l) for l in list(zip(*parsed_input[::-1]))]
    count = count + find_horizontal(rotated90)

    # Rotated 45 one way
    rotated45 = []
    i = 0
    for l in parsed_input:
        j = i
        for v in l:
            if len(rotated45) > j:
                rotated45[j].append(v)
            else:
                rotated45.append([v])
            j = j + 1
        i = i + 1

    rotated45 = ["".join(l) for l in rotated45]
    count = count + find_horizontal(rotated45)

    # Rotated 45 the other way
    rotated45 = []
    i = 0
    for l in parsed_input:
        j = i
        for v in reversed(l):
            if len(rotated45) > j:
                rotated45[j].append(v)
            else:
                rotated45.append([v])
            j = j + 1
        i = i + 1

    rotated45 = ["".join(l) for l in rotated45]
    count = count + find_horizontal(rotated45)

    return count

patterns = [
    [["M", "S"],
     ["M", "S"]],

    [["M", "M"],
     ["S", "S"]],

    [["S", "M"],
     ["S", "M"]],

    [["S", "S"],
     ["M", "M"]],

]


def p2(parsed_input):
    count = 0
    for p in patterns:
        for i in range(0, len(parsed_input) - 2):
            for j in range(0, len(parsed_input[0]) - 2):
                #print(f"{parsed_input[i][j]}_{parsed_input[i][j + 2]}  {p[0][0]}_{p[0][0]}")
                #print(f"_{parsed_input[i + 1][j + 1]}_  _A_")
                #print(f"{parsed_input[i+2][j]}_{parsed_input[i+2][j + 2]}  {p[1][0]}_{p[1][1]}")
                if (
                    parsed_input[i + 1][j + 1] == "A"
                    and parsed_input[i][j] == p[0][0]
                    and parsed_input[i][j + 2] == p[0][1]
                    and parsed_input[i + 2][j] == p[1][0]
                    and parsed_input[i + 2][j + 2] == p[1][1]
                ):
                    #print("matched")
                    count = count + 1
                #else:
                    #print("no match")
    return count


def main():
    parsed_input = parse("day4/example.txt")
    r1 = p1(parsed_input)
    assert r1 == example_r1, f"Failed p1 example, Got {r1} expected {example_r1}"
    r2 = p2(parsed_input)
    assert r2 == example_r2, f"Failed p2 example, Got {r2} expected {example_r2}"
    parsed_input = parse("day4/input.txt")
    r1 = p1(parsed_input)
    print(f"part 1: {r1}")
    r2 = p2(parsed_input)
    print(f"part 2: {r2}")


if __name__ == "__main__":
    main()
