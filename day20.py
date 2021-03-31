import sys
import re
import numpy as np
import itertools
from math import sqrt

class GraphConnection():

    def __init__(self,id_1,id_2,side,rot,flip):
        self.id_1 = id_1
        self.id_2 = id_2
        self.side = side #side of tile 1
        self.rot = rot #tile 2's relative rotation
        self.flip = flip #is tile 2 flipped?

    def __str__(self):
        return f"{self.id_1} -> {self.id_2} : side = {self.side}, rot = {self.rot}, flip = {self.flip}"

class OrientationData():

    def __init__(self,idx,rot,flip):
        self.idx = idx
        self.rot = rot
        self.flip = flip

def decode_orientation(od,gc):
    """Take a connection and the orientation of tile 1, then return the new orientation of tile 2"""
    new_or = OrientationData(gc.id_2,0,False)
    new_rot = (gc.rot + od.rot) % 4
    new_flip = gc.flip ^ od.flip
    new_or.rot = new_rot
    new_or.flip = new_flip
    return new_or

def apply_orientation(od,tile):
    if od.flip:
        tile = flip_tile(tile,0)
    return rotate_tile(tile,od.rot)
    """
    rot = rotate_tile(tile,od.rot)
    if od.flip:
        return flip_tile(rot,0)
    return rot
    """

def part2(data):
    tiles = {}
    tile = []
    idx = -1
    for line in data:
        if "Tile" in line:
            idx = int(line[-5:-1])
        elif len(line.strip()) == 0:
            tiles[idx] = tile
            tile = []
        else:
            tile.append(list(line))
    tiles[idx] = tile
    side_size = int(sqrt(len(tiles)))
    corner_pieces = []
    edge_pieces = []
    ids = list(tiles.keys())
    outer_pieces = {}
    connection_graph = []
    for i in range(len(tiles)):
        tile = tiles[ids[i]]
        edges = 0
        edge_set = [0,1,2,3]
        for side in [0,1,2,3]:
            matched = False
            for other_i in range(len(tiles)):
                other = tiles[ids[other_i]]
                if i != other_i:
                    for rot in [0,1,2,3]:
                        rotated = rotate_tile(other,rot)
                        flipped = flip_tile(rotated,0)
                        if tiles_match(tile,rotated,side):
                            matched = True
                        if tiles_match(tile,flipped,side):
                            matched = True
            if matched:
                edges += 1
                edge_set.remove(side)
        if edges == 2:
            corner_pieces.append(ids[i])
        if edges == 3:
            edge_pieces.append(ids[i])
    puzzle = [[None for _ in range(side_size)] for _ in range(side_size)]
    puzzle_id = [[None for _ in range(side_size)] for _ in range(side_size)]
    puzzle_id[0][0] = corner_pieces[0]
    puzzle[0][0] = flip_tile(rotate_tile(tiles[corner_pieces[0]],1),0)
    used = set([corner_pieces[0]])
    for x in range(side_size):
        for y in range(side_size):
            matched = False
            print("Placing tile at " + str((x,y)))
            if x == 0 and y == 0:
                pass
            elif y == 0:
                prev_id = puzzle_id[x-1][y]
                for other_id in tiles:
                    if other_id not in used:
                        other_t = tiles[other_id]
                        for rot in [0,1,2,3]:
                            rot_t = rotate_tile(other_t,rot)
                            flip = flip_tile(rot_t,0)
                            if tiles_match(puzzle[x-1][y],rot_t,2):
                                puzzle[x][y] = rot_t
                                puzzle_id[x][y] = other_id
                                matched = True
                                used.add(other_id)
                            if tiles_match(puzzle[x-1][y],flip,2):
                                puzzle[x][y] = flip
                                puzzle_id[x][y] = other_id
                                matched = True
                                used.add(other_id)
            else:
                prev_id = puzzle_id[x][y-1]
                for other_id in tiles:
                    if other_id not in used:
                        other_t = tiles[other_id]
                        for rot in [0,1,2,3]:
                            rot_t = rotate_tile(other_t,rot)
                            flip = flip_tile(rot_t,0)
                            if rot_t is None:
                                print("rot_t is none!")
                            if flip is None:
                                print("flip is none!")
                            if puzzle[x][y-1] is None:
                                print(f"puzzle[{x}][{y-1}] is none!")
                            if tiles_match(puzzle[x][y-1],rot_t,1):
                                puzzle[x][y] = rot_t
                                puzzle_id[x][y] = other_id
                                matched = True
                                used.add(other_id)
                            if tiles_match(puzzle[x][y-1],flip,1):
                                puzzle[x][y] = flip
                                puzzle_id[x][y] = other_id
                                matched = True
                                used.add(other_id)
            if not matched:
                print("Did not find a tile!")
    to_print = ""
    for y in range(side_size):
        for t_y in range(len(puzzle[y][0])):
            row = ''.join([''.join(t[t_y])+"|" for t in puzzle[y]])
            to_print += row + "\n"
        to_print += "-"*33+"\n"
    print(to_print)
    print(np.array(puzzle_id))
    stripped_image = np.block([[np.array(a)[1:-1,1:-1] for a in row] for row in puzzle])
    stripped_image = np.rot90(stripped_image,1)
    to_print = ""
    for row in stripped_image:
        to_print += ''.join(row)+"\n"
    print(to_print)
    seamon ="""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
    num_mons = 0
    xl,yl = stripped_image.shape
    for x in range(xl):
        for y in range(yl):
            check = stripped_image[x:x+3,y:y+20]
            rep = ""
            for row in check:
                rep += ''.join(row)+"\n"
            if x == 2 and y == 2:
                print(rep)

            is_mon = True
            if len(rep)-1 == len(seamon):
                for n in range(len(seamon)):
                    if seamon[n] == "#" and rep[n] != "#":
                        is_mon = False
                        break
            else:
                is_mon = False
            if is_mon:
                num_mons += 1
    print(seamon)
    print(num_mons)
    mon_hashtags = 15
    water_count = 0
    for row in stripped_image:
        water_count += str(row).count("#")
    print(water_count - mon_hashtags*num_mons)
    

def _part2(data):
    tiles = {}
    tile = []
    idx = -1
    for line in data:
        if "Tile" in line:
            idx = int(line[-5:-1])
        elif len(line.strip()) == 0:
            tiles[idx] = tile
            tile = []
        else:
            tile.append(list(line))
    tiles[idx] = tile
    side_size = int(sqrt(len(tiles)))
    corner_pieces = []
    edge_pieces = []
    ids = list(tiles.keys())
    outer_pieces = {}
    connection_graph = []
    for i in range(len(tiles)):
        tile = tiles[ids[i]]
        edges = 0
        edge_set = [0,1,2,3]
        for side in [0,1,2,3]:
            matched = False
            for other_i in range(len(tiles)):
                other = tiles[ids[other_i]]
                if i != other_i:
                    for rot in [0,1,2,3]:
                        rotated = rotate_tile(other,rot)
                        flipped = flip_tile(rotated,0)
                        if tiles_match(tile,rotated,side):
                            matched = True
                            gc =  GraphConnection(ids[i],ids[other_i],side,rot,False)
                            connection_graph.append(gc)
                        if tiles_match(tile,flipped,side):
                            matched = True
                            gc = GraphConnection(ids[i],ids[other_i],side,rot,True)
                            connection_graph.append(gc)
            if matched:
                edges += 1
                edge_set.remove(side)
        if edges == 2:
            corner_pieces.append(ids[i])
            print(edge_set)
        if edges == 3:
            edge_pieces.append(ids[i])
            print(edge_set)
    print("="*4)
    print(len(corner_pieces))
    print(len(edge_pieces))
    print(len(connection_graph))
    puzzle = [[None for _ in range(side_size)] for _ in range(side_size)]
    puzzle_ids = [[None for _ in range(side_size)] for _ in range(side_size)]
    puzzle_or = [[None for _ in range(side_size)] for _ in range(side_size)]
    print(puzzle)
    to_place = corner_pieces[0]
    print(to_place)
    copy_tiles = tiles.copy()
    lascon = None
    global_rot = 0

    
    puzzle[0][0] = tiles[to_place]
    puzzle_ids[0][0] = to_place
    puzzle_or[0][0] = OrientationData(to_place,0,True)


    for i in range(1,side_size):
        prev_id = puzzle_ids[0][i-1]
        for connection in connection_graph:
            if connection.id_1 == prev_id and (connection.id_2 in edge_pieces or connection.id_2 in corner_pieces):
                puzzle_ids[0][i] = connection.id_2
                old_or = puzzle_or[0][i-1]
                new_or = decode_orientation(old_or,connection)
                puzzle_or[0][i] = new_or
                new_tile = apply_orientation(new_or,tiles[connection.id_2])
                puzzle[0][i] = new_tile
                break
        rem = []
        for c in connection_graph:
            if c.id_2 == connection.id_2:
                rem.append(c)
        for c in rem:
            connection_graph.remove(c)
    for i in range(1,side_size):
        prev_id = puzzle_ids[i-1][0]
        for connection in connection_graph:
            if connection.id_1 == prev_id and (connection.id_2 in edge_pieces or connection.id_2 in corner_pieces):
                puzzle_ids[i][0] = connection.id_2
                old_or = puzzle_or[i-1][0]
                new_or = decode_orientation(old_or,connection)
                puzzle_or[i][0] = new_or
                new_tile = apply_orientation(new_or,tiles[connection.id_2])
                puzzle[i][0] = new_tile
                break
        rem = []
        for c in connection_graph:
            if c.id_2 == connection.id_2:
                rem.append(c)
        for c in rem:
            connection_graph.remove(c)
    for x in range(1,side_size):
        for y in range(1,side_size):
            neighbor_1 = puzzle_ids[x-1][y] 
            neighbor_2 = puzzle_ids[x][y-1] 
            print(f"n1 == {neighbor_1}, n2 == {neighbor_2}")
            done = False
            for c1 in connection_graph:
                for c2 in connection_graph:
                    if c1.id_1 == neighbor_1 and c2.id_1 == neighbor_2:
                        if c1.id_2 == c2.id_2:
                            new_id = c1.id_2
                            old_or = puzzle_or[x-1][y]
                            new_or = decode_orientation(old_or,c1)
                            new_tile = apply_orientation(new_or,tiles[new_id])
                            puzzle[x][y] = new_tile
                            puzzle_ids[x][y] = new_id
                            puzzle_or[x][y] = new_or
                            done = True
                            break
                    if done:
                        break

    print(puzzle)
    full_image = np.block([[np.array(a) for a in row] for row in puzzle])
    print(full_image)
    stripped_image = full_image[1:-1,1:-1]
    stripped_image = np.rot90(stripped_image,3)
    stripped_image = np.flip(stripped_image,1)
    print(stripped_image)
    to_display = ""
    for row in stripped_image:
        to_display += ''.join(row) + "\n"

    seamon ="""                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
    np.set_printoptions(suppress=True,linewidth=np.nan,threshold=100)
    num_mons = 0
    xl,yl = stripped_image.shape
    for x in range(xl):
        for y in range(yl):
            check = stripped_image[x:x+20,y:y+3]
            is_mon = True
            if x == 2 and y == 2:
                print(check)
            if len(check) == 20 and len(check[0]) == 3:
                for mx in range(20):
                    for my in range(3):
                        if seamon[my*20 + mx] == "#" and check[mx][my] != "#":
                            is_mon = False
            else:
                is_mon = False
            if is_mon:
                num_mons += 1
    print(seamon)
    print(num_mons)
    print(to_display)






def tiles_match(t1,t2,side):
    #   0
    # 3   1
    #   2
    if side == 0:
        a = t1[0]
        b = t2[-1]
    elif side == 1:
        a = [t[-1] for t in t1]
        b = [t[0] for t in t2]
    elif side == 2:
        a = t1[-1]
        b = t2[0]
    elif side == 3:
        a = [t[0] for t in t1]
        b = [t[-1] for t in t2]
    return a == b

def flip_tile(t,axis):
    arr = np.array(t)
    arr = np.flip(arr,axis)
    return [[s for s in ss] for ss in arr]

def rotate_tile(t,turns):
    arr = np.array(t)
    arr = np.rot90(arr,turns)
    return [[s for s in ss] for ss in arr]

def day20(data):
    tiles = {}
    tile = []
    idx = -1
    for line in data:
        if "Tile" in line:
            idx = int(line[-5:-1])
        elif len(line.strip()) == 0:
            tiles[idx] = tile
            tile = []
        else:
            tile.append(list(line))
    tiles[idx] = tile

    corner_pieces = []
    ids = list(tiles.keys())
    for i in range(len(tiles)):
        tile = tiles[ids[i]]
        edges = 0
        for side in [0,1,2,3]:
            matched = False
            for other_i in range(len(tiles)):
                other = tiles[ids[other_i]]
                if i != other_i:
                    for rot in [0,1,2,3]:
                        rotated = rotate_tile(other,rot)
                        flipped = flip_tile(rotated,0)
                        if tiles_match(tile,rotated,side):
                            matched = True
                        if tiles_match(tile,flipped,side):
                            matched = True
            if matched:
                edges += 1
        if edges == 2:
            corner_pieces.append(ids[i])
    prod = 1
    for p in corner_pieces:
        prod *= p
    print(corner_pieces)
    print(prod)


if __name__ == "__main__":
    data = [s.strip() for s in open(sys.argv[1]).readlines()]
    part2(data)
