
def _is_decreasing(values: list[int]) -> bool:
    current_value = values[0]
    for value in values[1:]:
        if current_value - value < 1 or current_value - value > 3:
            return False
        current_value = value
    return True

def _is_increasing(values: list[int]) -> bool:
    current_value = values[0]
    for value in values[1:]:
        if current_value - value < -3 or current_value - value >= 0:
            return False
        current_value = value
    return True


def main():
    values: list[list[int]] = []

    with open("input.txt") as f:
        for line in f.readlines():
            values.append([int(x) for x in line.rstrip().split(" ")])
    count = 0
    countB = 0
    for items in values:
        if _is_increasing(items) or _is_decreasing(items):
            count += 1
        valid = False
        for idx in range(len(items)):
            new_list = [x for i,x in enumerate(items) if i != idx]
            valid = valid or _is_increasing(new_list ) or _is_decreasing(new_list)
            if valid:
                countB += 1
                break
    print("Part A:", count)
    print("Part B:", countB)

if __name__ == "__main__":
    main()