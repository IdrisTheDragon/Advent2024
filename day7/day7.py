example_r1=3749
example_r2=11387

def parse(filename):
    data = []
    with open(filename,"r") as file:
        for l in file.readlines():
            l = l.split(":")
            data.append([int(l[0]),[int(v) for v in l[1].split()]])
    return data

def valid_combos(actual_total,t,vs):
    #print(actual_total,t,vs)
    if len(vs) == 0:
        if actual_total == t:
            return 1
        else:
            return 0
    
    v = vs.pop(0)
    valid = 0
    valid = valid + valid_combos(actual_total,t+v,vs.copy())
    valid = valid + valid_combos(actual_total,t*v,vs.copy())
    return valid
    

def p1(data):
    #print(data)
    sum = 0
    for [at,vs] in data:
        vs = vs.copy()
        valid = valid_combos(at,vs.pop(0),vs)
        if valid > 0:
            sum = sum + at
    return sum

def valid_combos_p2(actual_total,t,vs):
    #print(actual_total,t,vs)
    if len(vs) == 0:
        if actual_total == t:
            return 1
        else:
            return 0
    
    v = vs.pop(0)
    valid = 0
    valid = valid + valid_combos_p2(actual_total,t+v,vs.copy())
    valid = valid + valid_combos_p2(actual_total,t*v,vs.copy())
    valid = valid + valid_combos_p2(actual_total,int(str(t)+str(v)),vs.copy())
    return valid

def p2(data):
    #print(data)
    sum = 0
    for [at,vs] in data:
        vs = vs.copy()
        valid = valid_combos_p2(at,vs.pop(0),vs.copy())
        if valid > 0:
            sum = sum + at
    return sum

def main():
    parsed_input = parse("day7/example.txt")
    r1 = p1(parsed_input)
    assert r1 == example_r1, f"Failed p1 example, Got {r1} expected {example_r1}"
    r2 = p2(parsed_input)
    assert r2 == example_r2, f"Failed p2 example, Got {r2} expected {example_r2}"
    parsed_input = parse("day7/input.txt")
    r1 = p1(parsed_input)
    print(f"part 1: {r1}")
    r2 = p2(parsed_input)
    print(f"part 2: {r2}")

if __name__ == "__main__":
    main()
