import sys
import re

intpat = re.compile(r"(\d+)")

def part2(data):
    total = 0
    for line in data:
        line = line.strip()
        print(line)
        def match(t):
            nonlocal line
            line = line[1:].strip()
        def expr():
            nonlocal line
            val = term()
            while line and line[0] == '*':
                match('*')
                val = ('*',val,term())
            return val
        def term():
            nonlocal line
            val = factor()
            while line and line[0] == '+':
                match('+')
                val = ('+',val,factor())
            return val
        def factor():
            nonlocal line
            val = ('N',None,None)
            g = intpat.match(line)
            if line[0] == '(':
                match('(')
                val = expr()
                match(')')
            elif g:
                end = g.span()[1]
                print(line)
                num = int(line[0:end])
                val = (val[0],num,val[2])
                line = line[end:].strip()
            return val
        v = expr()
        print(v)
        def compute(tree):
            op = tree[0]
            if op == '*':
                return compute(tree[1])*compute(tree[2])
            if op == '+':
                return compute(tree[1])+compute(tree[2])
            if op == 'N':
                return tree[1]
        total += compute(v)
    print(total)

def evallit(ex):
    ex = ex.strip()
    print(f"evallit: {ex}")
    if ex[0] == "(":
        stack = 1
        idx = 1
        for c in ex[1:]:
            idx += 1
            if c == "(":
                stack += 1
            if c == ")":
                stack -= 1
            if stack == 0:
                break
        ret,left =  evalu(ex[1:idx-1]), ex[idx:]
        print(f"evallit returning {ret} and {left}")
        return ret, left
    if intpat.match(ex):
        g = intpat.match(ex)
        return int(g.group(1)), ex[len(g.group(1)):].strip()
    return int(ex[0:ex.find(" ")]), ex[ex.find(" "):]

def evalu(ex,acc=None):
    ex = ex.strip()
    print(f"evalu: |{ex}|")
    if ex[0] == '+':
        nextlit,ex = evallit(ex[1:])
        if acc == None:
            acc = 0
        if len(ex.strip()) == 0:
            return acc + nextlit
        return evalu(ex,acc+nextlit)
    if ex[0] == '*':
        nextlit,ex = evallit(ex[1:])
        if acc == None:
            acc = 1
        if len(ex.strip()) == 0:
            return acc * nextlit
        return evalu(ex,acc*nextlit)
    nextlit,ex = evallit(ex)
    if ex == "":
        return nextlit
    return evalu(ex,nextlit) 

    

def day18(data):
    total = 0
    for line in data:
        val = evalu(line.strip())
        print(val)
        total += val
    print(total)


if __name__ == "__main__":
    data = open(sys.argv[1]).readlines()
    part2(data)
