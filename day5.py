import sys
def get_seat_id(boarding_pass):
    row = int(str(''.join(["1" if c == "B" else "0" for c in boarding_pass[:7]])),2)
    col = int(str(''.join(["1" if c == "R" else "0" for c in boarding_pass[7:]])),2)
    return row*8+col

if __name__ == "__main__":
    data = open(sys.argv[1]).readlines()
    print(data)
    seats = [get_seat_id(p[:-1]) for p in data]
    sort_seats = sorted(seats)
    print(sort_seats)
    subbed = [s - i for i,s in enumerate(sort_seats)]
    masked = zip(subbed,subbed[1:])
    tested = [x - y for (x,y) in masked]
    print(tested.index(-1)+sort_seats[0]+1)
