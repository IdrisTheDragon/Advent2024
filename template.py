example_r1=0
example_r2=1

def parse(filename):
    return

def p1(parsed_input):
    return 0

def p2(parsed_input):    
    return 1

def main():
    parsed_input = parse("day1/example.txt")
    r1 = p1(parsed_input)
    assert r1 == example_r1, f"Failed p1 example, Got {r1} expeced {example_r1}"
    r2 = p2(parsed_input)
    assert r2 == example_r2, f"Failed p2 example, Got {r2} expeced {example_r2}"
    parsed_input = parse("day1/input.txt")
    r1 = p1(parsed_input)
    print(f"part 1: {r1}")
    r2 = p2(parsed_input)
    print(f"part 2: {r2}")

if __name__ == "__main__":
    main()
