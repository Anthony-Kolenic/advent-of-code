from collections import defaultdict
import math

def valid_order(update: list[int], rules: dict[int, list[int]]) -> bool:
    for idx, value in enumerate(update):
        current_rules = rules.get(value, [])
        for next_value in update[idx + 1:]:
            if next_value in current_rules:
                return False
    return True


def create_valid(update: list[int], rules: dict[int, list[int]]) -> list[int]:
    result = []
    for elem in update:
        idx = 0
        current_rules = rules.get(elem, [])
        for i, existing in enumerate(result):
            for rule in current_rules:
                if rule == existing:
                    idx = i + 1
        result.insert(idx, elem)
    return result
        

def main():
    with open("input.txt") as f:
        rule_data, update_data  = f.read().split("\n\n")
        rules: dict[int, list[int]] = defaultdict(list)
        for rule in rule_data.split("\n"):
            before, after = rule.rstrip().split("|")
            rules[int(after)].append(int(before))
        updates: list[list[int]] = []
        for update in update_data.split("\n"):
            updates.append([int(x) for x in update.rstrip().split(",")])
    middle_elements = []
    invalid_middle_elements = []
    for update in updates:
        if valid_order(update, rules):
            middle_elements.append(update[math.ceil(len(update) / 2) - 1])
        else:
            update = create_valid(update, rules)
            invalid_middle_elements.append(update[math.ceil(len(update) / 2) - 1])
        
    print("Part A:", sum(middle_elements))
    print("Part B:", sum(invalid_middle_elements))

if __name__ == "__main__":
    main()