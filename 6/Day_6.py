import collections
with open("/Users/pia/Desktop/Advent of Code/6/input.txt", "r") as f:
    inp = f.read()

bsp = """abc

a
b
c

ab
ac

a
a
a
a

b"""

inp = inp.split("\n\n")

def part_1(inp):
    inp = [x.replace("\n", "") for x in inp]
    all_yes = 0
    for i in inp:
        yes = []
        for c in i:
            if c not in yes:
                yes.append(c)
        all_yes += len(yes)

    return all_yes

def part_2(inp):
    inp = [x.split("\n") for x in inp]
    all_yes = 0

    for group in inp:
        yes = 0
        questions = []
        for p in range(len(group)):
            for c in group[p]:
                questions.append(c)
        counter=collections.Counter(questions)
        for key, value in counter.items():
            if value == len(group):
                yes += 1
        all_yes += yes

    return all_yes

anyone = part_1(inp)
everyone = part_2(inp)

print(anyone)
print(everyone)

        



        

            


