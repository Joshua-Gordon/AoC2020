import sys
import re

nums = [0,14,1,3,7,9]

def part2(data):
    count = 7
    memory = {0:1,14:2,1:3,3:4,7:5,9:6}
    last = 0
    while count < 30000000:
        if count % 100000 == 0:
            print(count)
        if last in memory:
            newval = count - memory[last]
            memory[last] = count
            count+= 1
            last = newval
        else:
            memory[last] = count
            count += 1
            last = 0
    print(last)



def day15(data):
    nums = [1,3,2]
    count = 3
    while count < 2020:
        if count % 10000 == 0:
            print(count)
        lastnum = nums[count-1]
        numsrev = nums[:-1][::-1]
        if lastnum not in numsrev:
            nums.append(0)
        else:
            idx = numsrev.index(lastnum)
            diff = count - (len(numsrev) - idx)
            nums.append(diff)
        count += 1
    print(nums)
    #print(nums)

if __name__ == "__main__":
    data = []
    day15(data)
    part2(data)
