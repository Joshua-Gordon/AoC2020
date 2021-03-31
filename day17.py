import sys
import re

active = object()

def part2(data):
    space = [[[[None for _ in range(20)] for _ in range(20)] for _ in range(15)] for _ in range(15)]
    for x in range(-3,5):
        for y in range(-3,5):
            space[7][7][9+y][9+x] = active if data[y+3][x+3] == '#' else None

    for cycle in range(6):
        newspace = [[[[ssss for ssss in sss] for sss in ss] for ss in s] for s in space] #copy space
        for widx,w in enumerate(space):
            for zidx,z in enumerate(w):
                for yidx,y in enumerate(z):
                    for xidx,x in enumerate(y):
                        n = neighbors3(space,widx,zidx,yidx,xidx)
                        if x is None and n == 3:
                            newspace[widx][zidx][yidx][xidx] = active
                        if x is active and n != 2 and n != 3:
                            newspace[widx][zidx][yidx][xidx] = None
        space = newspace
    acount = 0
    for widx,w in enumerate(space):
        for zidx,z in enumerate(w):
            for yidx,y in enumerate(z):
                for xidx,x in enumerate(y):
                    if x is active:
                        acount += 1
    print(acount)

def neighbors3(space,w,z,y,x):
    count = 0
    for dw in range(-1,2):
        for dz in range(-1,2):
            for dy in range(-1,2):
                for dx in range(-1,2):
                    if dw == 0 and dz == 0 and dy == 0 and dx == 0:
                        continue
                    if w + dw >= 0 and w + dw < len(space):
                        if z + dz >= 0 and z + dz < len(space[0]):
                            if y + dy >= 0 and y + dy < len(space[0][0]):
                                if x + dx >= 0 and x + dx < len(space[0][0][0]):
                                    if space[w+dw][z+dz][y+dy][x+dx] is active:
                                        count += 1
    return count

def neighbors(space,z,y,x):
    count = 0
    for dz in range(-1,2):
        for dy in range(-1,2):
            for dx in range(-1,2):
                if dz == 0 and dy == 0 and dx == 0:
                    continue
                if z + dz >= 0 and z + dz < len(space):
                    if y + dy >= 0 and y + dy < len(space[0]):
                        if x + dx >= 0 and x + dx < len(space[0][0]):
                            if space[z+dz][y+dy][x+dx] is active:
                                count += 1
    return count

def print_space(space):
    slices = []
    for i,z in enumerate(space):
        ok = False
        for y in z:
            print(y)
            if active in y:
                ok = True
                break
        if ok:
            slices.append(z)
    for s in slices:
        toprint = ""
        for line in s:
            p = ''.join(["#" if x is active else "." for x in line])
            toprint += p + "\n"
        print(toprint)

def day17(data):
    space = [[[None for _ in range(20)] for _ in range(20)] for _ in range(15)]
    for x in range(-3,5):
        for y in range(-3,5):
            space[7][9+y][9+x] = active if data[y+3][x+3] == '#' else None

    print_space(space)
    for cycle in range(6):
        newspace = [[[sss for sss in ss] for ss in s] for s in space] #copy space
        for zidx,z in enumerate(space):
            for yidx,y in enumerate(z):
                for xidx,x in enumerate(y):
                    n = neighbors(space,zidx,yidx,xidx)
                    if x is None and n == 3:
                        newspace[zidx][yidx][xidx] = active
                    if x is active and n != 2 and n != 3:
                        newspace[zidx][yidx][xidx] = None
        space = newspace
    acount = 0
    for zidx,z in enumerate(space):
        for yidx,y in enumerate(z):
            for xidx,x in enumerate(y):
                if x is active:
                    acount += 1
    print(acount)




if __name__ == "__main__":
    data = open(sys.argv[1]).readlines()
    #day17(data)
    part2(data)
