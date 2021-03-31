import sys

def part2(t,ids):
    ids = [(int(i),(int(i)-idx) % int(i)) for idx,i in enumerate(ids) if i != "x"]
    n = [p[0] for p in ids]
    a = [p[1] for p in ids]
    print(n)
    print(a)
    acc = 0
    prod = 1
    for num in n:
        prod *= num
    for num,mod in ids:
        p = prod // num
        acc += mod * pulverizer(p,num) * p
    print(acc  % prod)

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

def day13(t,ids):
    print(t)
    ids = [int(i) for i in ids if i != "x"]
    print(ids)
    mods = [i - (t % i) for i in ids]
    print(mods)
    m = min(mods)
    print(m)
    print(ids[mods.index(m)])
    print(ids[mods.index(m)]*m)

if __name__ == "__main__":
    data = open(sys.argv[1]).readlines()
    timestamp = int(data[0])
    ids = data[1].split(",")
    part2(timestamp,ids)
