from math import floor

example = [12, 14, 1969, 100756]


def fuel_required(mass: int) -> int:
    return (mass // 3) - 2


def fuel_required_inc_fuel(mass: int) -> int:
    fuel = fuel_required(mass)
    total_fuel = 0
    while fuel > 0:
        total_fuel += fuel
        fuel = fuel_required(fuel)
    return total_fuel


for mass in [12, 14, 1969, 100756]:
    print(fuel_required_inc_fuel(mass))

with open("../inputs/day01.txt") as f:
    masses = [int(line) for line in f]

print(sum([fuel_required_inc_fuel(mass) for mass in masses]))
