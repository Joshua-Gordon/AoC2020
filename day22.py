import sys
import re

def game_hash(d1,d2):
    return ''.join([str(i) for i in d1+[-1]+d2])

def part2(data):
    d1 = [int(n) for n in data[1:26]]
    d2 = [int(n) for n in data[28:53]]
    #d1 = [int(n) for n in data[1:6]]
    #d2 = [int(n) for n in data[8:13]]
    
    def recursive_combat(d1,d2): #return true if d1 wins
        game_set = set()
        while len(d1) != 0 and len(d2) != 0:
            h = game_hash(d1,d2)
            if h in game_set:
                return True, d1
            game_set.add(h)
            m = d1.pop(0)
            d = d2.pop(0)
            if len(d1) >= m and len(d2) >= d:
                winner,_ = recursive_combat(d1[:m],d2[:d])
                if winner:
                    d1.append(m)
                    d1.append(d)
                else:
                    d2.append(d)
                    d2.append(m)
            else:
                if m > d:
                    print(f"p1 wins with {m} > {d}")
                    d1.append(m)
                    d1.append(d)
                else:
                    print(f"p2 wins with {d} > {m}")
                    d2.append(d)
                    d2.append(m)
        if len(d1) == 0:
            return False, d2
        else:
            return True, d1


    winner,deck = recursive_combat(d1,d2)
    print(d1)
    print(d2)
    print(winner,deck)
    acc = 0
    print(deck)
    for i in range(len(deck)):
        card = deck[-1-i]
    
        print(card)
        acc += card*(i+1)
    print(winner)
    print(acc)


def day22(data):
    d1 = [int(n) for n in data[1:26]]
    d2 = [int(n) for n in data[28:53]]
    print(d1)
    print(d2)
    while len(d1) != 0 and len(d2) != 0:
        print("go")
        if d1[0] > d2[0]:
            d = d2.pop(0)
            m = d1.pop(0)
            d1.append(m)
            d1.append(d)
        else:
            d = d1.pop(0)
            m = d2.pop(0)
            d2.append(m)
            d2.append(d)
    if len(d1) == 0:
        deck = d2
        print("player 2 wins")
    else:
        print("player 1 wins")
        deck = d1
    acc = 0
    print(deck)
    for i in range(len(deck)):
        card = deck[-1-i]
    
        print(card)
        acc += card*(i+1)
    print(acc)


if __name__ == "__main__":
    data = [s.strip() for s in open(sys.argv[1]).readlines()]
    #day22(data)
    part2(data)
