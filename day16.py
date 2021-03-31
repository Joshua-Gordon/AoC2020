import sys
import re
import itertools
import tqdm
from constraint import *

pat = re.compile(r".*: (\d+)-(\d+) or (\d+)-(\d+)")

def part2(data):
    fields = []
    i = 0
    while True:
        if len(data[i].strip()) == 0:
            break
        fields.append(data[i].strip())
        i += 1
    acceptable = []
    fieldmap = []
    for f in fields:
        match = pat.match(f)
        min1 = match.group(1)
        max1 = match.group(2)
        min2 = match.group(3)
        max2 = match.group(4)
        acceptable.append((int(min1),int(max1)))
        acceptable.append((int(min2),int(max2)))
        fieldmap.append((f,(int(min1),int(max1)),(int(min2),int(max2))))
    print(fieldmap)
    departurefields = [d for d in fieldmap if "departure" in d[0]]
    print(departurefields)
    i += 5
    tickets = []
    invalid = 0
    valid_tickets = []
    while i < len(data):
        bad = False
        nums = [int(x) for x in data[i].strip().split(",")]
        for num in nums:
            for (a,b) in acceptable:
                if num in range(a,b+1):
                    break
            else:
                invalid += num
                bad = True
        if not bad:
            valid_tickets.append(nums)
        i += 1
    fieldpos = []
    for field in fieldmap:
        valid_positions = set()
        r1 = range(field[1][0],field[1][1]+1)
        r2 = range(field[2][0],field[2][1]+1)
        for n in range(len(fieldmap)):
            ok = True
            for t in valid_tickets:
                if t[n] not in r1 and t[n] not in r2:
                    ok = False
            if ok:
                valid_positions.add(n)
        fieldpos.append(valid_positions)
    print(fieldpos)
    field_assignments = []
    name_sets = list(zip([field[0] for field in fieldmap],fieldpos))
    p = Problem()
    for n,s in name_sets:
        p.addVariable(n,list(s))
    p.addConstraint(AllDifferentConstraint())
    solution = p.getSolutions()[0]
    prod = 1
    my_ticket = [int(x) for x in data[22].strip().split(",")]
    for f in solution:
        if "departure" in f:
            prod *= my_ticket[solution[f]]
            print("ok")
    print(prod)


def day16(data):
    fields = []
    i = 0
    while True:
        if len(data[i].strip()) == 0:
            break
        fields.append(data[i].strip())
        i += 1
    print(fields)
    acceptable = []
    for f in fields:
        print(f)
        match = pat.match(f)
        min1 = match.group(1)
        max1 = match.group(2)
        min2 = match.group(3)
        max2 = match.group(4)
        acceptable.append((int(min1),int(max1)))
        acceptable.append((int(min2),int(max2)))
    i += 5
    tickets = []
    invalid = 0
    while i < len(data):
        print(data[i])
        nums = [int(x) for x in data[i].strip().split(",")]
        for num in nums:
            for (a,b) in acceptable:
                if num in range(a,b+1):
                    break
            else:
                invalid += num
        i += 1
    print(invalid)
if __name__ == "__main__":
    data = open(sys.argv[1]).readlines()
    part2(data)
