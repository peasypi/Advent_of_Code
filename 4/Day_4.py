import re
import time
"""
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
"""
start_time = time.time()
with open("/Users/pia/Desktop/Advent of Code/4/input.txt", "r") as f:
    inp = f.read()

inp = inp.split("\n\n")
inp = [x.replace("\n", " ") for x in inp]

needed = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

unvalid_counter = 0
for i in inp[:]:
    for n in needed:
        if n not in i:
            unvalid_counter +=1
            inp.remove(i)
            break


rules = ["byr:(19[2-8][0-9]|199[0-9]|200[0-2])", "iyr:(201[0-9]|2020)", "eyr:(202[0-9]|2030)", "hgt:((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in)", "hcl:#[a-f, 0-9]{6}", "ecl:amb|blu|brn|gry|grn|hzl|oth", "pid:\d{9}\\b"]

unvalid = 0
for l in inp[:]:
    print(l)
    for r in rules:
        kp = re.search(r, l)
        if kp is None:
            print(r)
            unvalid += 1
            break

#print(kp)
print(unvalid)
print(len(inp))
print(len(inp)-unvalid)
print("--- %s seconds ---" %(time.time() - start_time))
