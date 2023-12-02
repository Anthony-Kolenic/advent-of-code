def _main():
    with open("input.txt", encoding="utf-8") as f:
        lines = [x.rstrip() for x in f.readlines()]
    total_a = 0
    total_b = 0

    for i, line in enumerate(lines):
        updated_line = line.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace(
            "five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")
        part_a = [x for x in line if x.isdigit()]
        part_b = [x for x in updated_line if x.isdigit()]
        total_a += int(part_a[0] + part_a[-1])
        total_b += int(part_b[0] + part_b[-1])
    print("Part A:", total_a)
    print("Part B:", total_b)


if __name__ == "__main__":
    _main()
