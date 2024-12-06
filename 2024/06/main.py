
def find_path(guard, direction, width, height, obstacles):
    visited = set()
    visited.add(guard)
    while True:
        next_pos = (guard[0] + direction[0], guard[1] + direction[1])
        if next_pos[0] < 0 or next_pos[0] >= width or next_pos[1] < 0 or next_pos[1] >= height:
            break
        if next_pos in obstacles:
            direction = (-1 * direction[1], direction[0])
        else:
            guard = next_pos
            visited.add(next_pos)
    return visited

def cycles(guard, direction, width, height, obstacles):
    visited = set()
    visited.add((*guard, *direction))
    while True:
        next_pos = (guard[0] + direction[0], guard[1] + direction[1])
        if next_pos[0] < 0 or next_pos[0] >= width or next_pos[1] < 0 or next_pos[1] >= height:
            return False
        if (*next_pos, *direction) in visited:
            return True
        if next_pos in obstacles:
            direction = (-1 * direction[1], direction[0])
        else:
            guard = next_pos
            visited.add((*next_pos, *direction))

def main():
    guard = (0, 0)
    direction = (0, -1)
    obstacles = set()
    width, height = 0, 0
    with open("input.txt") as f:
        for r, line in enumerate(f.readlines()):
            height += 1
            width = len(line)
            for c, val in enumerate(line.rstrip()):
                if val == "#":
                    obstacles.add((c, r))
                elif val == "^":
                    guard = (c, r)
    original_path = find_path(guard, direction, width, height, obstacles)
    print("Part A:", len(original_path))
    counter = 0
    for obstacle in original_path:
        current_obstacles = obstacles.copy()
        current_obstacles.add(obstacle)
        if cycles(guard, direction, width, height, current_obstacles):
            counter += 1
    print("Part B:", counter)

if __name__ == "__main__":
    main()