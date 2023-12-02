from collections import defaultdict
import math

def _main():
    with open("input.txt", encoding="utf-8") as f:
        lines = [x.rstrip() for x in f.readlines()]
    possible = []
    powers = []
    dice_couts = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for line in lines:
        values = line.split(" ")
        id = values[1].replace(":", "")
        colour_str = line.replace(f"Game {id}: ", "")
        sets = colour_str.strip().split(";")
        invalid = False
        minimum_sets = defaultdict(lambda: 0)
        for colour_set in sets:
            colours = colour_set.split(",")
            for dice in colours:
                amount, colour = dice.strip().split(" ")
                if minimum_sets[colour] < int(amount):
                    minimum_sets[colour] = int(amount)
                if int(amount) > dice_couts[colour]:
                    invalid = True
        powers.append(math.prod([v for v in minimum_sets.values()]))
        if not invalid:
            possible.append(int(id))

    print("Part A:", sum(possible))
    print("Part B:", sum(powers))

if __name__ == "__main__":
    _main()
