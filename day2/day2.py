example_r1=2
example_r2=4

def parse(filename):
    reports = []
    with open(filename,"r") as file:
        for l in file.readlines():
            reports.append([int(v) for v in l.split()])
    return reports

def issafe(report):
    dir = None
    for i in range(0,len(report)-1):
        diff = report[i] - report[i+1]
        if not 0 < abs(diff) < 4:
            return False
        if not dir:
            dir = "-" if diff >= 0 else "+"
        elif dir == "-" and diff <= 0:
            return False
        elif dir == "+" and diff >= 0:
            return False
    return True

def p1(reports):
    count = 0
    for report in reports:
        if issafe(report):
            count=count+1
    return count

def p2(reports):    
    count = 0
    for report in reports:
        if issafe(report):
            count=count+1
        else:
            for i in range(0,len(report)):
                if issafe(report[0:i]+report[i+1:len(report)]):
                    count=count+1
                    break
    return count

def main():
    reports = parse("day2/example.txt")
    r1 = p1(reports)
    assert r1 == example_r1, f"Failed p1 example, Got {r1} expeced {example_r1}"
    r2 = p2(reports)
    assert r2 == example_r2, f"Failed p2 example, Got {r2} expeced {example_r2}"
    reports = parse("day2/input.txt")
    r1 = p1(reports)
    print(f"part 1: {r1}")
    r2 = p2(reports)
    print(f"part 2: {r2}")

if __name__ == "__main__":
    main()
