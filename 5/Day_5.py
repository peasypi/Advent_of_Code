with open("/Users/pia/Desktop/Advent of Code/5/input.txt", "r") as f:
    inp = f.read()

inp = inp.split("\n")

def part_1(inp):
    rows = [x for x in range(128)]
    columns = [x for x in range(8)]
    highest_id = 0
    ids = []
    for i in inp:
        rows = [x for x in range(128)]
        columns = [x for x in range(8)]
        for k in i:
            middle_rows = int(len(rows)/2)
            middle_columns = int(len(columns)/2)
            if k == 'F':
                rows = rows[:middle_rows]
            elif k == 'B':
                rows = rows[middle_rows:]
            if len(rows) == 1:
                seat_row = rows[0]
            if k == 'L':
                columns = columns[:middle_columns]
            elif k == 'R':
                columns = columns[middle_columns:]
            if len(columns) == 1:
                seat_column = columns[0]
                #print("Sitz: ", seat_column)
        
        seat_id = seat_row*8 + seat_column
        ids.append(seat_id)

        if seat_id > highest_id:
            highest_id = seat_id
    
    return highest_id, ids

def part_2(ids):
    ids = sorted(ids)
    for m in range(len(ids)):
        if ids[m]+2 == ids[m+1]:
            my_id = range(ids[m], ids[m+1])[1]
            return my_id

highest_id, ids = part_1(inp)
my_id = part_2(ids)

print(f"Highest Seat ID ist {str(highest_id)}")
print(f"Meine Seat ID ist {str(my_id)}")


