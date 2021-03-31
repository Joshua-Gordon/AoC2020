import sys
import re
from tqdm import tqdm

class LList():

    def __init__(self,label,n):
        self.label = label
        self.n = n




cups = [int(s) for s in "158937462"] + list(range(10,1000001))
#cups = [3,8,9,1,2,5,4,6,7]


def part2(data):
    mil = 1000000
    l = LList(1,None)
    current = l
    labelmap = {1:l}
    for cup in cups[1:]:
        node = LList(cup,None)
        labelmap[cup] = node
        l.n = node
        l = node
    l.n = current
    itr = current
    for i in range(20):
        print(itr.label)
        itr = itr.n

    for i in range(10000000):
        next1 = current.n
        next2 = next1.n
        next3 = next2.n
        next4 = next3.n
        current.n = next4

        destination_label = (current.label - 1) 
        if destination_label == 0:
            destination_label = mil
        while destination_label in [next1.label,next2.label,next3.label]:
            destination_label -= 1
            if destination_label == 0:
                destination_label = mil
        dest_node = labelmap[destination_label]
        next5 = dest_node.n
        dest_node.n = next1
        next3.n = next5
        current = next4
    node1 = labelmap[1]
    next1 = node1.n
    next2 = next1.n
    print(next1.label,next2.label)
    print(next1.label*next2.label)

def day23(data):
    global cups
    current = 0 #index of first cup
    for m in tqdm(range(10000000)):
        current_label = cups[current]
        if current + 3 >= len(cups):
            removed = cups[current+1:len(cups)] + cups[0:current+3 - len(cups)+1]
        else:
            removed = cups[current+1:current+4]
        destination = cups[current]-1
        if destination == 0:
            destination = len(cups)-1
        while destination in removed:
            destination -= 1
            if destination == 0:
                destination = len(cups) - 1
        newcups = [c for c in cups if c not in removed]
        idx = newcups.index(destination)
        for c in removed[::-1]:
            newcups.insert(idx+1 % len(newcups),c)
        cups = newcups
        old_current = cups.index(current_label)
        if old_current == len(cups)-1:
            current = 0
        else:
            current = old_current + 1
        print(str(cups[-20:-1]) + "|||" + str(cups[:300]))
        if current == 0:
            sys.exit(1)

    print(','.join([str(c) for c in cups]))

if __name__ == "__main__":
    data = ""
    part2(data)
