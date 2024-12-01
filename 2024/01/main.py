from collections import Counter

def main():
    with open("input.txt") as f:
        lines = [x.rstrip().replace("   ", " ") for x in f.readlines()]
    
    list_a: list[int] = []
    list_b: list[int] = []
    for line in lines:
        [a,b] = line.split(" ")
        list_a.append(int(a))
        list_b.append(int(b))
    
    list_a.sort()
    list_b.sort()

    difference = 0
    for a,b in zip(list_a, list_b):
        difference += abs(a - b)
    print("Part A:", difference)

    counts = Counter(list_b)
    similarity = 0
    for a in list_a:
        similarity += a * counts.get(a, 0)
    print("Part B:", similarity)

if __name__ == "__main__":
    main()