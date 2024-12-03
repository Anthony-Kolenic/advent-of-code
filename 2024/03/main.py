import re

def process_b(items: list[str]):
    total = 0
    can_process = True
    for item in items:
        item = next((x for x in item if x))
        match item:
            case "do()":
                can_process = True
            case "don't()":
                can_process = False
            case _:
                if not can_process:
                    continue
                [a,b] = item.replace("mul(", "").replace(",", " ").replace(")", "").split()
                total += int(a) * int(b)
    return total

def process(items: list[str]):
    total = 0
    for item in items:
        [a,b] = item.replace("mul(", "").replace(",", " ").replace(")", "").split()
        total += int(a) * int(b)
    return total

def main():
    data = ""
    with open("input.txt") as f:
        data = "".join([x.rstrip() for x in f.readlines()])
    part_a = r"(mul\(\d+,\d+\))"
    part_b = r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))"
    print("Part A:", process(re.findall(part_a, data)))
    print("Part B:", process_b(re.findall(part_b, data)))

if __name__ == "__main__":
    main()