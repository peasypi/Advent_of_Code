with open("/Users/pia/Desktop/Advent of Code/input.txt", "r") as f:
    inp = f.read()

binp = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

inp = [int(x) for x in inp.split("\n")]
inp = sorted(inp)
def part_1():
    ones = 0
    twos = 0
    threes = 0

    beg = 0
    for i in inp:
        if i - beg == 1:
            ones += 1
        elif i - beg == 2:
            twos += 1
        elif i - beg == 3:
            threes += 1
        beg = i

    threes += 1

    print(ones)
    print(twos)
    print(threes)

    print(ones*threes)

counter = 0
begin = 0
arrangement = []
for i in inp:
    if

