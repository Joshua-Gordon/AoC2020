import sys
import math


def part2(data):
    ship_x = 0
    ship_y = 0
    way_x = 10
    way_y = 1
    way_heading = 0
    ship_heading = 0
    for line in data:
        print(line)
        inst = line[0]
        val = int(line[1:])
        if inst == "N":
            way_y += val
        elif inst == "S":
            way_y -= val
        elif inst == "E":
            way_x += val
        elif inst == "W":
            way_x -= val
        elif inst == "F":
            ship_x += val*way_x
            ship_y += val*way_y
        elif inst == "L":
            if val == 0:
                way_x,way_y = way_x,way_y
            if val == 270:
                way_x,way_y = way_y,-way_x
            if val == 180:
                way_x,way_y = -way_x,-way_y
            if val == 90:
                way_x,way_y = -way_y,way_x
            #way_heading -= val
            #rway_heading = math.radians(way_heading)
            #temp_way_x = way_x*math.cos(rway_heading) - way_y*math.sin(rway_heading)
            #temp_way_y = way_x*math.sin(rway_heading) + way_y*math.cos(rway_heading)
            #way_x = int(temp_way_x)
            #way_y = int(temp_way_y)
        elif inst == "R":
            if val == 0:
                way_x,way_y = way_x,way_y
            if val == 270:
                way_x,way_y = -way_y,way_x
            if val == 180:
                way_x,way_y = -way_x,-way_y
            if val == 90:
                way_x,way_y = way_y,-way_x
            #way_heading -= val
            #rway_heading = math.radians(way_heading)
            #temp_way_x = way_x*math.cos(rway_heading) - way_y*math.sin(rway_heading)
            #temp_way_y = way_x*math.sin(rway_heading) + way_y*math.cos(rway_heading)
            #way_x = int(temp_way_x)
            #way_y = int(temp_way_y)
        print(ship_x,ship_y,math.degrees(ship_heading))
        print(way_x,way_y,(way_heading))
    print(abs(ship_x)+abs(ship_y))


def day12(data):
    ship_x = 0
    ship_y = 0
    ship_heading = 0
    for line in data:
        inst = line[0]
        val = int(line[1:])
        if inst == "N":
            ship_y += val
        elif inst == "S":
            ship_y -= val
        elif inst == "E":
            ship_x += val
        elif inst == "W":
            ship_x -= val
        elif inst == "F":
            ship_x += val*math.cos(ship_heading)
            ship_y += val*math.sin(ship_heading)
        elif inst == "L":
            ship_heading += math.radians(val)
        elif inst == "R":
            ship_heading -= math.radians(val)
        print(ship_x,ship_y,math.degrees(ship_heading))
    print(abs(ship_x)+abs(ship_y))

if __name__ == "__main__":
    data = open(sys.argv[1]).readlines()
    part2(data)
