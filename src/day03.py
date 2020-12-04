from __future__ import annotations

from typing import Tuple, List

Point = Tuple[int, int]


class Wire:
    corners: List[Point]

    @staticmethod
    def parse(raw: str) -> Wire():
        Wire = [(0, 0)]
        for instruction in raw.split(","):
            try:
                if instruction.startswith("U"):
                    move = (0, int(instruction[1:]))
                elif instruction.startswith("D"):
                    move = (0, -int(instruction[1:]))
                elif instruction.startswith("L"):
                    move = (-int(instruction[1:]), 0)
                elif instruction.startswith("R"):
                    move = (int(instruction[1:]), 0)
                else:
                    print(f"ingnored instruction '{instruction}'")
                    continue
                Wire.append(tuple(x1 + x2 for x1, x2 in zip(Wire[-1], move)))
            except:
                breakpoint()
        return Wire


def find_crosses(wire1: Wire, wire2: Wire) -> List[Point]:
    crosses = []
    for start1, end1 in zip(wire1, wire1[1:]):
        for start2, end2 in zip(wire2, wire2[1:]):
            if start1[0] == end1[0]:
                if min(start2[0], end2[0]) < start1[0] < max(
                    start2[0], end2[0]
                ) and min(start1[1], end1[1]) < start2[1] < max(start1[1], end1[1]):
                    crosses.append((start1[0], start2[1]))
            elif start1[1] == end1[1]:
                if min(start2[1], end2[1]) < start1[1] < max(
                    start2[1], end2[1]
                ) and min(start1[0], end1[0]) < start2[0] < max(
                    start1[0], end1[0]
                ):  # Wires cross if start1.x < start2.x < end1.x if start1[]
                    crosses.append((start2[0], start1[1]))
    return crosses


def distance_along_wire(wire: Wire, cross: Point) -> int:
    distance = 0
    for start, end in zip(wire, wire[1:]):
        if min(start[0], end[0]) <= cross[0] <= max(start[0], end[0]) and min(
            start[1], end[1]
        ) <= cross[1] <= max(start[1], end[1]):
            return distance + abs(start[0] - cross[0]) + abs(start[1] - cross[1])
        else:
            distance += abs(start[0] - end[0]) + abs(start[1] - end[1])


def find_closest(crosses: List[Point]) -> int:
    closest = sum([abs(i) for i in crosses[0]])
    for cross in crosses:
        closest = min(closest, sum([abs(i) for i in cross]))
    return closest


inp1 = """R8,U5,L5,D3"""
inp2 = """U7,R6,D4,L4,"""
wire1 = Wire.parse(inp1)
wire2 = Wire.parse(inp2)

crosses = find_crosses(wire1, wire2)
print(crosses)
print(find_closest(crosses))

with open("../inputs/day03.txt") as f:
    wires = [Wire.parse(wire) for wire in f.readlines()]

crosses = find_crosses(*wires)
print(crosses)
print(find_closest(crosses))

closest = distance_along_wire(wires[0], crosses[0]) + distance_along_wire(
    wires[1], crosses[0]
)
for cross in crosses:
    closest = min(
        closest,
        (distance_along_wire(wires[0], cross) + distance_along_wire(wires[1], cross)),
    )
print(closest)
