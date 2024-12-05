
def rotate_matrix(matrix: list[list]):
    rows, cols = len(matrix), len(matrix[0])
    result = []
    for c in range(cols):
        result.append(["." for _ in range(rows)])

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            result[c][r] = matrix[r][c]
    return result
    # Intresting way to achieve the same logic 
    # list(zip(*matrix[::-1]))
    # reverse matrix row order, unpack, and finally group the items with zip

def flip_matrix(grid):
    return [x[::-1] for x in grid]

def search_grid(grid) -> int:
    total = 0
    for row in grid:
        line = "".join(row)
        total += line.count("XMAS")
        total += line.count("SAMX")
    return total

def diagonal_search(grid, search = "XMAS") -> list[tuple[int, int]]:
    search_rev = search[::-1]
    result = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            try:
                word = ""
                for i in range(len(search)):
                    word += grid[r + i][c + i]
                if word == search or word == search_rev:
                    result.append((r, c))
            except:
                # Except when out of bounds, so we skip these
                continue    
    return result

def xmas_scan(grid) -> int:
    first_scan = diagonal_search(grid, "MAS")
    second_scan = diagonal_search(flip_matrix(grid), "MAS")
    # flip the positions back to the orginal matrix coord system
    second_scan = [(a,len(grid) - 1 - b) for (a,b) in second_scan]
    total = 0
    for (a_y, a_x) in first_scan:
        for (b_y, b_x) in second_scan:
            if (a_y == b_y) and (b_x - a_x == 2):
                total += 1
    return total

def main():
    grid : list[list[str]] = []
    with open("input.txt") as f:
        for line in f.readlines():
            grid.append([(x if x in "XMAS" else ".") for x in line.rstrip()])
    result = search_grid(grid) + search_grid(rotate_matrix(grid)) + len(diagonal_search(grid)) + len(diagonal_search(flip_matrix(grid)))
    print("Part A:", result)
    print("Part B:", xmas_scan(grid))
    
if __name__ == "__main__":
    main()