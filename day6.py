import sys

def read_input(s):
    total = 0
    group = None
    for line in s:
        if len(line) == 0:
            print(group)
            total += len(group)
            group = None
        elif group is None:
            group = set(line)
        else:
            group = group.intersection(set(line))
    total += len(group)
    print(total)

if __name__ == "__main__":
    data = [line.strip() for line in open(sys.argv[1]).readlines()]
    read_input(data)
