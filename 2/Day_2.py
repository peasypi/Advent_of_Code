import re
with open("/Users/pia/Desktop/Advent of Code/2/input.txt", "r") as f:
    inp = f.read()

inp = inp.split("\n")

def part_1():
    counter = 0
    for i in inp:
        letter = re.findall(r"\w{1}:", i)
        letter = letter[0].replace(":", "")
        password = re.findall(r"[a-z]{2,}", i)
        password = password[0]
        minmax = re.findall(r"\d{1,3}-\d{1,3}", i)
        minmax = re.findall(r"\d{1,3}", str(minmax))
        minimum = int(minmax[0])
        maximum = int(minmax[1])
        anzahl = password.count(letter)
        if anzahl in range(minimum, maximum+1):
            counter += 1
    return counter

def part_2():
    counter = 0
    for i in inp:
        letter = re.findall(r"\w{1}:", i)
        letter = letter[0].replace(":", "")
        password = re.findall(r"[a-z]{2,}", i)
        password = password[0]
        occ = re.findall(r"\d{1,3}-\d{1,3}", i)
        occ = re.findall(r"\d{1,3}", str(occ))
        first_occ = int(occ[0])
        second_occ = int(occ[1])
        if (letter == password[first_occ-1]) ^ (letter == password[second_occ-1]):
            counter += 1
    return counter