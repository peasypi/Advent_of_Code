with open("/Users/pia/Desktop/Advent of Code/9/input.txt", "r") as f:
    inp = f.read()

binp = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

inp = [int(x) for x in inp.split("\n")]


def part_1():
    for i in range(25,len(inp)):
        nums = []
        valid = False
        nums = [int(x) for x in inp[i-25:i]]
        for n in nums:
            for m in nums:
                if n != m and n+m == int(inp[i]):
                    valid = True
                    break
            if valid == True:
                break
        if valid == False:
            print(inp[i])
            break
                
answer = 15690279
#answer = 127

def part_2():
    for i in range(len(inp)):
        summe = inp[i]
        for j in range(1,100):
            summe += inp[i+j]
            if summe == answer:
                print(inp[i], inp[i+j])
                numbers = sorted(inp[i:i+j+1])
                return (numbers[0] + numbers[len(numbers)-1])
            elif summe > answer:
                break

print(part_2())