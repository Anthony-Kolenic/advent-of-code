from dataclasses import dataclass
import math
@dataclass
class Key():
    from_map: str
    to_map: str

    def __hash__(self):
        return f"{self.from_map}".__hash__()
    
    def __eq__( self, b ):
        return b == self.from_map
    
def get_locations(seeds: list[int], path: list[str], mappings: dict[Key, tuple[int, int, int]]) -> list[int]:
    final_locations = []
    for seed in seeds:
        current = seed
        for next_path in path:
            mapping = mappings[next_path]
            for (dst, src, rg) in mapping:
                if src <= current < src + rg:
                    current = dst + (current - src)
                    break
        final_locations.append(current)
    return final_locations
    
def _main():
    with open("input.txt", encoding="utf-8") as f:
        lines = f.read()
    sections = lines.split("\n\n")
    seeds = [int(x) for x in sections[0].replace("seeds:", "").strip().split(" ")]
    sections.pop(0)
    mappings = {}
    path = []
    for section in sections:
        lines = section.split("\n")
        from_map, to_map = lines[0].replace(" map:", "").replace("-to", "").split("-")
        path.append(from_map)
        key = Key(from_map, to_map)
        lines.pop(0)
        mappings[key] = []
        for line in lines:
            dst, src, value_range = line.split(" ")
            mappings[key].append((int(dst), int(src), int(value_range)))
    final_locations = get_locations(seeds, path, mappings)
    print("Part A:", min(final_locations))
    current_pairs = []
    for i in range(0, len(seeds), 2):
        current_pairs.append((seeds[i], seeds[i] + seeds[i + 1] - 1))
    
    total = 0
    smallest = None
    for i in range(20):
        for start, end in current_pairs:
            total += end - start + 1
        to_check = []
        for start, end in current_pairs:
            step = max(1,round(10000 / 2**i))
            current = start
            while current < end:
                to_check.append(current)
                current += step

        results = list(zip(to_check, get_locations(to_check, path, mappings)))
        results = sorted(results, key=lambda x: x[1])
        smallest = results[0][1]
        current_pairs = [[results[0][0] - max(2, step), results[0][0] + max(2, step)]]
    print("Part B:", smallest)

if __name__ == "__main__":
    _main()
    