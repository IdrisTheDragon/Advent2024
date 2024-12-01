example_r1=11
example_r2=31

def parse(filename):
    l1 = []
    l2 = []
    with open(filename,"r") as infile:
        for line in infile.readlines():
            data = line.split()
            l1.append(int(data[0]))
            l2.append(int(data[1]))
    return (l1,l2)

def p1(parsed_input):
    l1 = parsed_input[0]
    l2 = parsed_input[1]
    l1.sort()
    l2.sort()
    #print(l1,l2)

    sum = 0
    for i in range(0,len(l1)):
        dis = abs(l1[i] - l2[i])
        #print(dis,l1[i],l2[i])
        sum = sum+dis

    return sum

def p2(parsed_input):    
    l1 = parsed_input[0]
    l2 = parsed_input[1]
    sum = 0
    for v in l1:
        c = l2.count(v)
        #print(v*c,v,c)
        sum = sum+ (v*c)
    return sum

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
