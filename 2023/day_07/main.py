from functools import cmp_to_key
from collections import Counter

def get_hand_type(hand: str) -> int:
    counts=Counter(hand)
    hand_type = 0
    for k, v in counts.items():
        if v == 5:
            hand_type = 7
            break
        if v == 4:
            hand_type = 6
            break
        if v == 3:
            hand_type += 3
        if v == 2:
            hand_type += 1
    return hand_type

def convert_to_numbers(hand: str) -> list[int]:
    cards = [*hand]

    for i in range(len(cards)):
        cards[i] = cards[i].replace("A", "14").replace("K", "13").replace("Q", "12").replace("J", "0").replace("T", "10")
        cards[i] = int(cards[i])
    return cards
    
def compare_hands(first, second: list[int]) -> int:
    for x, y in zip(first, second):
        if x < y:
            return 1
        if x > y:
            return -1
    return 0

def compare(a, b: tuple[str, int]) -> int:
    hand_a, _ = a
    hand_b, _ = b
    hand_a = (hand_a, get_hand_type(hand_a))
    hand_b = (hand_b, get_hand_type(hand_b))

    if hand_a[1] == hand_b[1]:
        return  compare_hands(convert_to_numbers(hand_a[0]), convert_to_numbers(hand_b[0]))
    else:
        return hand_b[1] - hand_a[1]

def _main():
    with open("input.txt") as f:
        lines = [x.strip() for x in f.readlines()]
    cards = [(x.split(" ")[0], int(x.split(" ")[1])) for x in lines]
    cards.sort(key=cmp_to_key(compare), reverse=True)
    rank = 0
    winnings = 0
    for _, bid in cards:
        rank += 1
        winnings += rank * bid
    print(winnings)

if __name__ == "__main__":
    _main()
