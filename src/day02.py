from typing import List

opcodes = [
    "1,0,0,0,99",
    "1,0,0,0,99",
    "2,3,0,3,99",
    "2,4,4,5,99,0",
    "1,1,1,4,99,5,6,0,99",
]


def compute(input: List[int]) -> List[int]:
    output = input.copy()
    pos = 0
    # Run until you get to an op code of 99
    while True:
        try:
            op, i1, i2, to = output[pos : pos + 4]
        except ValueError:
            # 99 can be near the end, if it's still a problem shout
            op = output[pos]
            if op != 99:
                raise ValueError("Program did not end")
        if op == 99:
            return output
        elif op == 1:
            output[to] = output[i1] + output[i2]
        elif op == 2:
            output[to] = output[i1] * output[i2]
        pos += 4


for opcode in opcodes:
    input = [int(i) for i in opcode.split(",")]
    print(input)
    print(compute(input))
    print()


with open("../inputs/day02.txt") as f:
    codes = f.read()

codes = [int(i) for i in codes.split(",")]
print(codes)
codes[1] = 12
codes[2] = 2
print(codes)
print()
print(compute(codes))
print(compute(codes)[0])

for noun in range(100):
    for verb in range(100):
        codes[1] = noun
        codes[2] = verb
        out = compute(codes)[0]
        if out == 19690720:
            print(100 * noun + verb)
            break
        else:
            print(noun, verb, out)