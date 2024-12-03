example_r1=161
example_r2=48

import re




def parse(filename):
    with open(filename,"r") as file:
        memory = file.read()
    return memory

def p1(memory):
    sum =0
    p = re.compile('mul\\(\\d+,\\d+\\)')
    muls = p.findall(memory)
    for mul in muls:
        mul = mul[4:-1].split(',')
        sum = sum +(int(mul[0]) * int(mul[1]))
    return sum

def p2(memory):

    sum=0
    p = re.compile("mul\\(\\d+,\\d+\\)|do\\(\\)|don't\\(\\)")
    muls = p.findall(memory)
    enabled = True
    for mul in muls:
        if mul == "do()":
            enabled = True
        elif mul == "don't()":
            enabled = False
        elif enabled:
            mul = mul[4:-1].split(',')
            sum = sum +(int(mul[0]) * int(mul[1]))
    return sum

def main():
    parsed_input = parse("day3/example.txt")
    r1 = p1(parsed_input)
    assert r1 == example_r1, f"Failed p1 example, Got {r1} expeced {example_r1}"
    parsed_input = parse("day3/example2.txt")
    r2 = p2(parsed_input)
    assert r2 == example_r2, f"Failed p2 example, Got {r2} expeced {example_r2}"
    parsed_input = parse("day3/input.txt")
    r1 = p1(parsed_input)
    print(f"part 1: {r1}")
    r2 = p2(parsed_input)
    print(f"part 2: {r2}")

if __name__ == "__main__":
    main()
