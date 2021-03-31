import sys
from functools import reduce

def run_slope(trees):
    lines = trees.split("\n")[:-1]
    pos_odds = [0]*4
    pos_down = 0
    counts = [0]*5
    for j,line in enumerate(lines[1:]):
        for i in range(4):
            pos_odds[i] = (pos_odds[i] + 2*i+1) % len(line)
            if line[pos_odds[i]] == "#":
                counts[i] += 1
        if j % 2 == 1:
            pos_down = (pos_down+1) % len(line)
            if line[pos_down] == "#":
                counts[4] += 1
    print(counts)
    print(reduce(lambda x,y: x*y,counts))

if __name__ == "__main__":
    trees = open(sys.argv[1]).read()
    run_slope(trees)
