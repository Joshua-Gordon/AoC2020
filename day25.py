import sys
import re

def part2(data):
    pass


def pulverizer(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: 
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: 
        x1 += b0
    return x1


def day25(data):
    def transform(sub,loop):
        val = 1
        for _ in range(loop):
            val = (val*sub) % 20201227
        return val
    def get_loop(key):
        i = 1
        while True:
            v = transform(7,i)
            print("i = " + str(i))
            print(v,key)
            if v == key:
                return i
            i += 1
    loop_door = 11002971#get_loop(int(data[0]))
    enc = transform(int(data[1]),loop_door)
    print(enc)

if __name__ == "__main__":
    data = [s.strip() for s in open(sys.argv[1]).readlines()]
    day25(data)
