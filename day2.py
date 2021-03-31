import re
import sys
pattern = re.compile(r"(\d+)-(\d+) ([a-z]): (\w+)")

def validate(line):
    match = pattern.match(line)
    letter = match.group(3)
    lower = int(match.group(1))
    upper = int(match.group(2))
    password = match.group(4)
    return password.count(letter) in range(lower,upper+1)

def better_validate(line):
    match = pattern.match(line)
    letter = match.group(3)
    first = int(match.group(1))
    second = int(match.group(2))
    password = match.group(4)
    return (password[first-1] == letter) ^ (password[second-1] == letter)

with open(sys.argv[1]) as f:
    lines = f.readlines()
    count = 0
    for l in lines:
        if better_validate(l):
            count += 1
    print(count)
