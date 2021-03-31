import sys
import re

def input2rules(fname):
    data = open(fname).readlines()
    bag_map = {}
    for line in data:
        bag_color,_,contents = line.partition("contain")
        bag_map[bag_color[:bag_color.find(" bags")]] = contents
    total_colors = 0
    all_colors = set(bag_map.keys())
    total_colors = set()
    acceptable_colors = ["shiny gold"]
    new_colors = []
    found = True
    while found:
        found = False
        for key in bag_map:
            for ac in acceptable_colors:
                if ac in bag_map[key]:
                    found = True
                    new_colors.append(key)
                    total_colors.add(key)
        acceptable_colors = new_colors
        new_colors = []
    print(len(total_colors))

def part2(fname):
    data = open(fname).readlines()
    bag_map = {}
    for line in data:
        bag_color,_,contents = line.partition("contain")
        bag_map[bag_color[:bag_color.find(" bags")]] = contents
    bag_parse = re.compile(r" (\d+) (.*) bags?")
    def bag_recurse(bag_key):
        print("recursing on " + bag_key)
        contents = bag_map[bag_key]
        print(contents)
        if "no other bags" in contents:
            return 1
        items = contents.split(",")
        subbags = 0
        for item in items:
            match = bag_parse.match(item)
            print(item)
            count = int(match.group(1))
            key = match.group(2)
            num_bags = bag_recurse(key)
            print(f"{bag_key} has {num_bags} more subbags")
            subbags += count * num_bags
        return subbags+1
    print(bag_recurse("shiny gold")-1)


if __name__ == "__main__":
    #input2rules(sys.argv[1])
    part2(sys.argv[1])
