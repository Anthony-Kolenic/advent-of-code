def get_number(line:str, x: int):
    if not line[x].isdigit():
        return "", x
    result = ""
    counter = x
    start = x
    while counter >= 0:
        if not line[counter].isdigit():
            break
        result = line[counter] + result
        start = counter
        counter -= 1

    counter = x + 1
    while counter < len(line):
        if not line[counter].isdigit():
            break
        result = result + line[counter]
        counter += 1
    return result, start

def get_surrounding_parts(lines: list[str], x, y):
    parts = set()
    for yy in range(max(0, y - 1), min(len(lines) - 1, y + 1) + 1):
        for xx in range(max(0, x - 1), min(len(lines[0]) - 1, x + 1) + 1):
            if not lines[yy][xx].isdigit() or lines[yy][xx] == ".":
                continue
            number, start = get_number(lines[yy], xx)
            if number:
                parts.add(f"{start}_{yy}")
    return parts

def _main():
    with open("input.txt", encoding="utf-8") as f:
        lines = [x.rstrip() for x in f.readlines()]
    unique_numbers = {}
    for k, line in enumerate(lines):
        current_number = ""
        for j, char in enumerate(line):
            if char.isdigit():
                current_number += char
            elif current_number:
                unique_numbers[f"{j - len(current_number)}_{k}"] = current_number
                current_number = ""
        if current_number:
            unique_numbers[f"{len(line) - len(current_number)}_{k}"] = current_number
            current_number = ""
    found_numbers: set = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char.isdigit() or char == ".":
                continue
            found_numbers.update(get_surrounding_parts(lines, x, y))

                        
    total = 0
    for value in found_numbers:
        total += int(unique_numbers[value])
    print("Part A:", total)

    total = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != "*":
                continue
            parts = get_surrounding_parts(lines, x, y)
            if len(parts) == 2:
                total += int(unique_numbers[parts.pop()]) * int(unique_numbers[parts.pop()])
    print("Part B:", total)


if __name__ == "__main__":
    _main()
