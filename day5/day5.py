example_r1=143
example_r2=123

def parse(filename):
    with open(filename, "r") as file:
        rules = []
        updates = []
        for l in file.readlines():
            if "|" in l:
               v= l.split("|")
               rules.append([int(v[0]), int(v[1])])
            elif "," in l:
                updates.append([int(v) for v in l.split(",")])
    return (rules,updates)

def isvalid(update,rules):
    valid=True
    for rule in rules:
        try:
            x = update.index(rule[0])
            y = update.index(rule[1])
            if x>y:
                valid=False
                break
        except:
            pass
            # only one of the numbers so we are fine
    return valid

def p1(parsed_input):
    rules = parsed_input[0]
    updates = parsed_input[1]

    count = 0

    for update in updates:
        if isvalid(update,rules):
            count = count + update[int(len(update)/2)]
    return count

def p2(parsed_input):
    rules = parsed_input[0]
    updates = parsed_input[1]

    count = 0

    for update in updates:
        if not isvalid(update,rules):
            fixed = []
            for z in update:
                if len(fixed) == 0:
                    fixed.append(z)
                    continue
                before = []
                after = []
                for rule in rules:
                    if rule[0] == z:
                        try:
                            after.append(fixed.index(rule[1]))
                        except:
                            pass
                    elif rule[1] == z:
                        try:
                            before.append(fixed.index(rule[0]))
                        except:
                            pass
                if before:
                    bm=max(before)
                    fixed = fixed[:bm+1] + [z] + fixed[bm+1:]
                elif after:
                    am=min(after)
                    fixed = fixed[:am] + [z] + fixed[am:]
                else:
                    print("Failed to place {z} in {fixed}")
                    exit(1)

            count = count + fixed[int(len(fixed)/2)]

    return count

def main():
    parsed_input = parse("day5/example.txt")
    r1 = p1(parsed_input)
    assert r1 == example_r1, f"Failed p1 example, Got {r1} expected {example_r1}"
    parsed_input = parse("day5/input.txt")
    r1 = p1(parsed_input)
    print(f"part 1: {r1}")
    parsed_input = parse("day5/example.txt")
    r2 = p2(parsed_input)
    assert r2 == example_r2, f"Failed p2 example, Got {r2} expected {example_r2}"
    parsed_input = parse("day5/input.txt")
    r2 = p2(parsed_input)
    print(f"part 2: {r2}")

if __name__ == "__main__":
    main()
