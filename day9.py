import sys

def part2(data):
    target = 756008079
    for i,start in enumerate(data):
        for j,end in enumerate(data[i+1:]):
            if sum(data[i:i+1+j]) == target:
                print(min(data[i:i+1+j]) + max(data[i:i+1+j]))


def day9(data):
    preamble = set(data[0:25])
    for i,num in enumerate(data[25:]):
        for d in preamble:
            if (int(num)-int(d)) in preamble:
                break
        else:
            print(num)
            break
        preamble.remove(data[i])
        preamble.add(num)


if __name__ == "__main__":
    data = [int (d) for d in open(sys.argv[1]).readlines()]
    part2(data)
