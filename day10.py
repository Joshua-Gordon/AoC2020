import sys
import re
import itertools

def part2(data):
    jolt_sort = [0]+sorted(data)
    diffs = [y-x for (x,y) in zip(jolt_sort,jolt_sort[1:])]
    print(diffs)
    split_on_threes = []
    acc = []
    for i,d in enumerate(diffs):
        if d == 3:
            split_on_threes.append(acc+[jolt_sort[i]])
            acc = []
        else:
            acc.append(jolt_sort[i])
    split_on_threes.append(acc+[jolt_sort[-1]])
    print(split_on_threes)
    def count_skips(elems):
        if len(elems) < 3:
            return 1
        if len(elems) == 3:
            return 2
        if len(elems) == 4:
            return 4
        if len(elems) == 5:
            return 7
    acc = 1
    for skippable in split_on_threes:
        acc *= count_skips(skippable)
    print(acc)

def day10(data):
    jolt_sort = [0]+sorted(data)
    diffs = [y-x for (x,y) in zip(jolt_sort,jolt_sort[1:])]
    print(len(jolt_sort))
    print(len(diffs))
    print(diffs.count(1) * (1+diffs.count(3)))

if __name__ == "__main__":
    data = [int(j) for j in open(sys.argv[1]).readlines()]
    print(sorted(data))
    part2(data)
