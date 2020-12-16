import re
import copy

with open("/Users/pia/Desktop/Advent of Code/8/input.txt", "r") as f:
    inp = f.read()

binp = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

inp = [x.split(" ") for x in inp.split("\n")]

def part_1(inp):
    accumulator = 0
    i = 0
    index = []
    while i < len(inp):
        if i not in index:
            index.append(i)
        else:
            #print(accumulator)
            #print(("Fehler: Acc ist ", accumulator))
            return "Fehler"
        if inp[i][0] == "jmp":
            if inp[i][1][0] == "-":
                i-= int(inp[i][1][1:])
            else:
                i += int(inp[i][1][1:])
        elif inp[i][0] == "nop":
            i += 1
            continue
        elif inp[i][0] == "acc":
            if inp[i][1][0] == "-":
                accumulator -= int(inp[i][1][1:])
                i += 1
            else:
                accumulator += int(inp[i][1][1:])
                i += 1
    print("Alles hat geklappt. Acc ist ", accumulator)
    return accumulator

def part_2():
    for l in range(len(inp)):
        copy_inp = copy.deepcopy(inp)
        if copy_inp[l][0] == "nop":
            copy_inp[l][0] = "jmp"
            if part_1(copy_inp) != "Fehler":
                break
        if copy_inp[l][0] == "jmp":
            copy_inp[l][0] = "nop"
            if part_1(copy_inp) != "Fehler":
                break
