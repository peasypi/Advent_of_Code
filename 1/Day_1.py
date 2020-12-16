with open("/Users/pia/Desktop/Advent of Code/1/input.txt", "r") as txt:
    inp = txt.read()
 
inp = inp.split("\n")
for i in inp:
    for l in inp:
        for k in inp:
            if int(i)+int(l)+int(k) == 2020:
                print(int(i)*int(l)*int(k))

