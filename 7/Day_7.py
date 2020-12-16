import re

with open("/Users/pia/Desktop/Advent of Code/7/input.txt", "r") as f:
    inp = f.read()

bsp_inp = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

inp = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

my_bag = "shiny gold"

inp = inp.split("\n")
#print(inp)

inp = [x[:-1].split(" contain ") for x in inp]
inp = dict(inp)
#print("\n", inp)

#possible_bags = []
def part_1():
    bags = []
    for out, inner in inp.items():
        if my_bag in inner:
            bag = re.sub(" bag(s)?", "", out)
            bags.append(bag)
    #print(bags)

    neue_bags = bags
    for key, val in inp.items():
        for bag in bags:
            if bag in val:
                b = re.sub(" bag(s)?", "", key)
                #print(b)
                neue_bags.append(b)

    neuere_bags = neue_bags
    for key, val in inp.items():
        for bag in neue_bags:
            if bag in val:
                b = re.sub(" bag(s)?", "", key)
                #print(b)
                neuere_bags.append(b)

    noch_neuere = neuere_bags
    for key, val in inp.items():
        for bag in neuere_bags:
            if bag in val:
                b = re.sub(" bag(s)?", "", key)
                #print(b)
                noch_neuere.append(b)

    neuste = noch_neuere
    for key, val in inp.items():
        for bag in noch_neuere:
            if bag in val:
                b = re.sub(" bag(s)?", "", key)
                #print(b)
                neuste.append(b)

    am_neusten = neuste
    for key, val in inp.items():
        for bag in neuste:
            if bag in val:
                b = re.sub(" bag(s)?", "", key)
                #print(b)
                am_neusten.append(b)

    possible_bags = set(am_neusten)
    #print(possible_bags)
    print(len(possible_bags))
    return len(possible_bags)

rules = {}
for key, value in inp.items():
    k = re.sub(" bag(s)?", "", key)
    v = re.sub(" bag(s)?", "", value)
    rules[k] = v.split(", ")

pattern = r"(\d+)\s([a-z]+\s?[a-z]+\s?)"
bags = []
numbers = []
"""for i in range(len(rules[my_bag])):
    match = re.match(pattern, rules[my_bag][i])
    num = match.groups()[0]
    color = match.groups()[1]
    numbers.append(num)
    bags.append(color)
print(bags)
print(numbers)"""

my_bag_rule = {"shiny gold": ""}
my_bag_rule[my_bag] = rules[my_bag]
#copy = {"shiny gold": ""}
#copy[my_bag] = rules[my_bag]
#print(copy)

for i in range(10):
    for b in my_bag_rule[my_bag]:
        match = re.match(pattern, b)
        if not match:
            pass
        else:
            num = match.groups()[0]
            color = match.groups()[1]
            for r in rules[color]:
                print(r)
                if "no other" in r:
                    my_bag_rule[my_bag].extend(rules[color])
                else:
                    match = re.match(pattern, r)
                    inner_num = match.groups()[0]
                    #print(inner_num)
                    #print(num)
                    numb = int(num)* int(inner_num)
                    #print(num)
                    color = match.groups()[1]
                    new = str(numb) + " " + color
                    my_bag_rule[my_bag].append(new)
    #print(my_bag_rule)
    my_bag_rule[my_bag].remove(b)
    #print(b)
my_bag_rule[my_bag] = set(my_bag_rule[my_bag])

print(my_bag_rule)

#print(set(my_bag_rule[my_bag]))
#print(copy)
anzahl = 0
for k in my_bag_rule[my_bag]:
    match = re.match(pattern, k)    
    if not match:
        pass
    else:
        num = match.groups()[0]
        anzahl += int(num)

print(anzahl)


  
#print(anzahl)
#part_1()


