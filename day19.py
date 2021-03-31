import sys
import re

def match(rules,idx,line):
    rule = rules[idx]
    if type(rule) is str:
        return line == rule
    if type(rule) is int:
        return match(rules,rule,line)
    if type(rule) is list:
        r1 = int(rule[0])
        r2 = int(rule[1])
        for idx in range(len(line)):
            if match(rules,r1,line[:idx]) and match(rules,r2,line[idx:]):
                return True
        return False
    if type(rule) is tuple and type(rule[0]) is list:
        rs00 = rule[0][0]
        rs01 = rule[0][1]
        rs10 = rule[1][0]
        rs11 = rule[1][1]
        for idx in range(len(line)):
            if match(rules,rs00,line[:idx]) and match(rules,rs01,line[idx:]):
                return True
        for idx in range(len(line)):
            if match(rules,rs10,line[:idx]) and match(rules,rs11,line[idx:]):
                return True
        return False
    elif type(rule) is tuple:
        r0 = rule[0]
        r1 = rule[1]
        return match(rules,r0,line) or match(rules,r1,line)
    print("Oh no, rule is " + str(rule)) 

def make_pat(rules,idx=0):
    rule = rules[idx]
    if idx == 8:
        p = make_pat(rules,42)
        return "{}+".format(p)
    if idx == 11:
        p1 = make_pat(rules,42)
        p2 = make_pat(rules,31)
        def cheat(acc=100):
            nonlocal p1
            nonlocal p2
            if acc == 0:
                return "(({}{}))".format(p1,p2)
            else:
                pref = cheat(acc-1)
                return "(({}{})|({}{}{}))".format(p1,p2,p1,pref,p2)
        return cheat()
    if type(rule) is str:
        return rule
    if type(rule) is int:
        return make_pat(rules,rule)
    if type(rule) is list:
        r1 = make_pat(rules,int(rule[0]))
        r2 = make_pat(rules,int(rule[1]))
        if len(rule) == 3:
            r3 = make_pat(rules,int(rule[2]))
            return "({}{}{})".format(r1,r2,r3)
        return "({}{})".format(r1,r2)
    if type(rule) is tuple and type(rule[0]) is list:
        rs00 = make_pat(rules,int(rule[0][0]))
        rs01 = make_pat(rules,int(rule[0][1]))
        rs10 = make_pat(rules,int(rule[1][0]))
        rs11 = make_pat(rules,int(rule[1][1]))
        if len(rule[1]) == 3:
            rs12 = make_pat(rules,int(rule[1][2]))
            return "(({}{})|({}{}{}))".format(rs00,rs01,rs10,rs11,rs12)
        return "(({}{})|({}{}))".format(rs00,rs01,rs10,rs11)
    elif type(rule) is tuple:
        r0 = make_pat(rules,int(rule[0]))
        if type(rule[1]) is list:
            r10 = make_pat(rules,int(rule[1][0]))
            r11 = make_pat(rules,int(rule[1][1]))
            return "({}|{}{})".format(r0,r10,r11)
        r1 = make_pat(rules,int(rule[1]))
        return "({}|{})".format(r0,r1)



def day19(data):
    rules = {}
    reading = False
    total = 0
    pat = None
    for line in data:
        line = line.strip()
        if len(line.strip()) == 0:
            reading = True
        if not reading:
            if '"' in line:
                num = int(line[0:line.index(":")])
                rule = line[line.find('"')+1:line.rfind('"')]
                rules[num] = rule
            else:
                num = int(line[0:line.index(":")])
                line = line[line.index(":")+2:]
                stuff = line.split(" ")
                if len(stuff) == 1:
                    rules[num] = int(stuff[0])
                elif len(stuff) == 2:
                    rules[num] = [int(stuff[0]),int(stuff[1])]
                elif len(stuff) == 3:
                    if stuff[1] == "|":
                        rules[num] = (int(stuff[0]),int(stuff[2]))
                    else:
                        rules[num] = [int(stuff[0]),int(stuff[1]),int(stuff[2])]
                elif len(stuff) == 4:
                    rules[num] = (int(stuff[0]),[int(stuff[2]),int(stuff[3])])
                elif len(stuff) == 5:
                    rules[num] = ([int(stuff[0]),int(stuff[1])],[int(stuff[3]),int(stuff[4])])
                elif len(stuff) == 6:
                    rules[num] = ([int(stuff[0]),int(stuff[1])],[int(stuff[3]),int(stuff[4]),int(stuff[5])])
                else:
                    print("Oh no, stuff is " + str(stuff))
                print(line)
        else:
            if pat is None:
                s = make_pat(rules,0)
                print(s)
                pat = re.compile("^"+s+"$")
            if pat.match(line):
                print(line)
                total += 1
    print(total)


if __name__ == "__main__":
    data = open(sys.argv[1]).readlines()
    day19(data)
