import sys

def part2(data):
    print(len(data))
    for i,line in enumerate(data):
        inst,_,arg = line.partition(" ")
        if inst == "nop":
            newdata = data[:i] + ["jmp " + arg] + data[i+1:]
            print(len(newdata))
            acc = day8(newdata)
            if acc is not None:
                print(acc)
                return
        if inst == "jmp":
            newdata = data[:i] + ["nop " + arg] + data[i+1:]
            print(len(newdata))
            acc = day8(newdata)
            if acc is not None:
                print(acc)
                return


def day8(data):
    executed = set()
    acc = 0
    ip = 0
    while ip not in executed:
        if ip == len(data):
            return acc
        executed.add(ip)
        inst,_,arg = data[ip].partition(" ")
        if inst == "acc":
            sign = arg[0]
            if sign == '+':
                val = int(arg[1:])
            else:
                val = -int(arg[1:])
            acc += val
            ip += 1
        elif inst == "jmp":
            sign = arg[0]
            if sign == '+':
                ip += int(arg[1:])
            else:
                ip -= int(arg[1:])
        else:
            ip += 1
    return None

if __name__ == "__main__":
    data = open(sys.argv[1]).readlines()
    part2(data)
