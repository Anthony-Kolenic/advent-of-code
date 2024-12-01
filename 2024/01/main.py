from collections import Counter

def main():
    list_a: list[int] = []
    list_b: list[int] = []

    with open("input.txt") as f:
        for line in f.readlines():
            [a,b] = line.rstrip().split("   ")
            list_a.append(int(a))
            list_b.append(int(b))
    
    list_a.sort()
    list_b.sort()
    difference = sum([abs(a - b) for (a, b) in zip(list_a, list_b)])
    print("Part A:", difference)

    counts = Counter(list_b)
    similarity = sum([x * counts.get(x, 0) for x in list_a])
    print("Part B:", similarity)

if __name__ == "__main__":
    main()