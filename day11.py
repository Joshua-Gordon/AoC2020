import sys

def part2(data):
    data = [list(s) for s in data]
    itrs = 0
    newdata = [row.copy() for row in data]
    print_grid(data)
    print("="*20)
    while True:
        for y in range(len(data)):
            for x in range(len(data[0])):
                if data[y][x] == ".":
                    pass
                elif data[y][x] == "L":
                    n = visible_neighbors(x,y,data)
                    if n == 0:
                        newdata[y][x] = "#"
                elif data[y][x] == "#":
                    n = visible_neighbors(x,y,data)
                    if n >= 5:
                        newdata[y][x] = "L"
        
        if newdata == data:
            print(f"itrs={itrs}")
            print_grid(newdata)
            return count_occ(data)
        data = [row.copy() for row in newdata]
        print_grid(data)
        print("="*20)
        itrs += 1

def visible_neighbors(x,y,data,debug=False):
    row = data[y]
    col = [row[x] for row in data]
    neighbors = 0
    leftrow = row[:x][::-1]
    rightrow = row[x+1:]
    leftcol = col[:y][::-1]
    rightcol = col[y+1:]
    leftdown_diag = []
    itr = 1
    while x - itr >= 0 and y - itr >= 0:
        leftdown_diag.append(data[y-itr][x-itr])
        itr+=1
    itr = 1
    rightdown_diag = []
    while x + itr < len(data[0]) and y + itr < len(data):
        rightdown_diag.append(data[y+itr][x+itr])
        itr+=1
    rightup_diag = []
    itr = 1
    while x + itr < len(data[0]) and y - itr >= 0:
        rightup_diag.append(data[y-itr][x+itr])
        itr+=1
    itr = 1
    leftup_diag = []
    while x - itr >= 0 and y + itr < len(data):
        leftup_diag.append(data[y+itr][x-itr])
        itr+=1
    paths = [leftrow,leftcol,leftdown_diag,leftup_diag,rightrow,rightcol,rightdown_diag,rightup_diag]
    for p in paths:
        p = ''.join(p)
        unoc = p.find("L")
        oc = p.find("#")
        if debug:
            print(f"p is {p}, unoc is {unoc}, oc is {oc}")
        if (unoc > oc or unoc == -1) and oc != -1:
            if debug:
                print("yep")
            neighbors += 1
    return neighbors

def neighbors(x,y,data):
    if x == 0:
        start = 0
    else:
        start = x-1
    if x == len(data)-1:
        end = x+1
    else:
        end = x+2
    topslice = 0
    centerslice = data[y][start:end].count("#")
    botslice = 0
    if y != 0:
        topslice = data[y-1][start:end].count("#")
    if y != len(data)-1:
        botslice = data[y+1][start:end].count("#")
    return topslice+centerslice+botslice

def count_occ(data):
    return sum([l.count("#") for l in data])

def print_grid(data):
    sdata = [''.join(row) for row in data]
    for s in sdata:
        print(s)

def day11(data):
    data = [list(s) for s in data]
    itrs = 0
    newdata = [row.copy() for row in data]
    print_grid(data)
    while True:
        for y in range(len(data)):
            for x in range(len(data[0])):
                #print(f"y,x = {y},{x}")
                if data[y][x] == ".":
                    continue
                elif data[y][x] == "L":
                    n = neighbors(x,y,data)
                    if n == 0:
                        newdata[y][x] = "#"
                elif data[y][x] == "#":
                    n = neighbors(x,y,data) -1
                    if n >= 4:
                        newdata[y][x] = "L"
        
        if newdata == data:
            print(f"itrs={itrs}")
            print_grid(newdata)
            return count_occ(data)
        data = [row.copy() for row in newdata]
        print_grid(data)
        itrs += 1

def test1():
    grid = [['#', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', '#'], ['#', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'], ['L', '.', 'L', '.', 'L', '.', '.', 'L', '.', '.'], ['L', 'L', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'], ['L', '.', 'L', 'L', '.', 'L', 'L', '.', 'L', 'L'], ['L', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', 'L'], ['.', '.', 'L', '.', 'L', '.', '.', '.', '.', '.'], ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', '#'], ['#', '.', 'L', 'L', 'L', 'L', 'L', 'L', '.', 'L'], ['#', '.', 'L', 'L', 'L', 'L', 'L', '.', 'L', '#']]
    print_grid(grid)
    return grid


if __name__ == "__main__":
    data = [s.strip() for s in open(sys.argv[1]).readlines()]
    #print(day11(data))
    print(part2(data))
