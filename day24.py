import sys

def part2(data):
    hexes = set()
    directions = {'e':(-1,0,1),'ne':(0,-1,1),'nw':(1,-1,0),'w':(1,0,-1),'sw':(0,1,-1),'se':(-1,1,0)}
    for line in data:
        h = (0,0,0)
        partial = None
        i = 0
        while i < len(line):
            char = line[i]
            if char in 'ns' and i != len(line)-1:
                nc = line[i+1]
                if nc in 'ew':
                    d = char+nc
                    i+=1
                else:
                    d = char
            else:
                d = char
            i += 1
            h = add_hex(h,directions[d])
        if h in hexes:
            hexes.remove(h)
        else:
            hexes.add(h)
    for day in range(100):
        toflip = set()
        for tile in hexes:
            n = hex_neigh(tile,hexes)
            print("tile has " + str(n) + " neighbors")
            if n == 0 or n > 2:
                toflip.add(tile)
            #white tiles
            for d in list(directions.values()):
                other = add_hex(tile,d)
                if other not in hexes:
                    n = hex_neigh(other,hexes)
                    if n == 2 and other not in toflip:
                        toflip.add(other)
        for tile in toflip:
            if tile in hexes:
                hexes.remove(tile)
            else:
                hexes.add(tile)
    print(len(hexes))

def hex_neigh(h,hexes):
    directions = {'e':(-1,0,1),'ne':(0,-1,1),'nw':(1,-1,0),'w':(1,0,-1),'sw':(0,1,-1),'se':(-1,1,0)}
    count = 0
    for d in directions:
        newh = add_hex(h,directions[d])
        if newh in hexes:
            count += 1
    return count


def add_hex(h1,h2):
    return (h1[0]+h2[0],h1[1]+h2[1],h1[2]+h2[2])

def day24(data):
    hexes = set()
    directions = {'e':(-1,0,1),'ne':(0,-1,1),'nw':(1,-1,0),'w':(1,0,-1),'sw':(0,1,-1),'se':(-1,1,0)}
    for line in data:
        h = (0,0,0)
        partial = None
        i = 0
        while i < len(line):
            char = line[i]
            if char in 'ns' and i != len(line)-1:
                nc = line[i+1]
                if nc in 'ew':
                    d = char+nc
                    i+=1
                else:
                    d = char
            else:
                d = char
            i += 1
            h = add_hex(h,directions[d])
        if h in hexes:
            hexes.remove(h)
        else:
            hexes.add(h)
    print(len(hexes))
            

if __name__ == "__main__":
    data = [s.strip() for s in open(sys.argv[1]).readlines()]
    part2(data)
