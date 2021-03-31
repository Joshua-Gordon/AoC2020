import sys
import re

def part2(data):
    pat = re.compile(r"mem\[(\d+)\] = (\d+)")
    mask = ""
    memory = {}
    for line in data:
        if "mask" in line:
            eq = line.find("=")
            mask = line[eq+2:]
        else:
            match = pat.match(line)
            addr = match.group(1)
            val = int(match.group(2))
            addr = list("{0:b}".format(int(addr)).zfill(36))
            addrs = [[]]
            for idx,c in enumerate(mask):
                if c == "0":
                    for i in range(len(addrs)):
                        addrs[i].append(addr[idx])
                if c == "1":
                    for i in range(len(addrs)):
                        addrs[i].append("1")
                if c == "X":
                    newaddrs = []
                    for i in range(len(addrs)):
                        newaddrs.append([])
                        newaddrs.append([])
                        for bit in addrs[i]:
                            newaddrs[2*i].append(bit)
                            newaddrs[2*i+1].append(bit)
                        newaddrs[2*i].append("0")
                        newaddrs[2*i+1].append("1")
                    addrs = [[s for s in a] for a in newaddrs]
            for a in addrs:
                location = int(''.join(a),2)
                print(location)
                memory[location] = val
    print(sum(memory.values()))

def day14(data):
    mask = ""
    memory = {}
    pat = re.compile(r"mem\[(\d+)\] = (\d+)")
    for line in data:
        if "mask" in line:
            eq = line.find("=")
            mask = line[eq+2:]
            print(mask)
        else:
            match = pat.match(line)
            addr = match.group(1)
            val = match.group(2)
            print(addr)
            print(val)
            val = list("{0:b}".format(int(val)).zfill(36))
            for idx,c in enumerate(mask):
                if c == "0":
                    val[idx] = "0"
                elif c == "1":
                    val[idx] = "1"
            memory[int(addr)] = int(''.join(val),2)
        print(memory)
    print(sum(memory.values()))

if __name__ == "__main__":
    data = open(sys.argv[1]).readlines()
    part2(data)
