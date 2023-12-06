import re


def _calculate_ways(time: int, record: int) -> int:
    # While this works, I cannot help but think that you could just calculate the where a parabola intersects the x-axis
    counter = 0
    for current in range(time):
        speed = current
        remaining = time - current
        distance = remaining * speed
        if distance > record:
            counter += 1
    return counter


def _main():
    with open("input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    times = [int(x) for x in re.findall(r"(\d+)", lines[0])]
    records = [int(x) for x in re.findall(r"(\d+)", lines[1])]
    result = 1
    for time, record in zip(times, records):
        counter = _calculate_ways(time, record)
        if counter > 0:
            result *= counter
    print("Part A:", result)

    time = int("".join([str(x) for x in times]))
    record = int("".join([str(x) for x in records]))

    ways = _calculate_ways(time, record)
    print("Part B:", ways)


if __name__ == "__main__":
    _main()
