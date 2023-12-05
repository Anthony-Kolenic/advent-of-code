
def _main():
    with open("input.txt", encoding="utf-8") as f:
        lines = [x.rstrip() for x in f.readlines()]
    cards: dict[tuple[set[str], set[str]]] = {}
    for i, line in enumerate(lines):
        line = line.split(": ")[1]
        winning, card = line.strip().split(" | ")
        winning = set([x for x in winning.split(" ") if x])
        card = set([x for x in card.split(" ") if x])
        cards[i] = (winning, card)

    total = 0
    for winning, card in cards.values():
        matches = card.intersection(winning)
        if not matches:
            continue
        total += 2**(len(matches) - 1)
    print("Part A:", total)

    how_many_cards = {}
    highest_index = max(cards.keys())
    for current_index in range(highest_index, -1, -1):
        winning, card = cards[current_index]
        matches = card.intersection(winning)
        total = 0
        for i in range(current_index + 1, min(highest_index, current_index+ len(matches)) + 1):
            total += how_many_cards[i] + 1
        how_many_cards[current_index] = total
    total = 0
    for i in range(highest_index + 1):
        total += how_many_cards[i] + 1
    print("Part B:", total)

if __name__ == "__main__":
    _main()
