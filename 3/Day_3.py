with open("/Users/pia/Desktop/Advent of Code/3/input.txt", "r") as f:
    the_map = f.read()

the_map = the_map.split("\n")

def part_1(right, the_map):
    index = 0
    tree_counter = 0
    for line in the_map:
        if index > len(line)-1:
            index = index%len(line)
            if line[index] == '#':
                tree_counter += 1
        else:
            if line[index] == '#':
                tree_counter += 1
        index += right

    return tree_counter

def part_2(the_map):
    index = 0
    tree_counter = 0
    row = 0
    for line in the_map[:]:
        if (row%2) == 0:
            if index > len(line)-1:
                index = index%len(line)
                if line[index] == '#':
                    tree_counter += 1
            else:
                if line[index] == '#':
                    tree_counter += 1
            index += 1
        row += 1

    return tree_counter

nums = [1, 3, 5, 7]
answer = 1
for number in nums:
    anzahl_trees = part_1(number, the_map)
    print(anzahl_trees)
    answer = answer * anzahl_trees
    print(answer)

#answer = 87753728
anzahl_trees = part_2(the_map)
print(anzahl_trees)
answer = answer * anzahl_trees

print(answer)
