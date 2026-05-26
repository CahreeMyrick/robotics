from collections import deque
import heapq

WALL = "#"
FREE = "."
START = "S"
GOAL = "G"

grid_bfs_better = [
    "S.G....",
    ".......",
    ".......",
    ".......",
]

grid_best_first_better = [
    "S........G",
    "#########.",
    "..........",
]

grid_astar_better = [
    "S........",
    "#######..",
    "......#..",
    ".####.#..",
    ".#....#G.",
    ".#.####..",
    ".#.......",
    ".########",
    ".........",
]


def parse_grid(lines):
    grid = [list(row) for row in lines]
    return grid


def find_start_goal(grid):
    start = None
    goal = None

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == START:
                start = (r, c)
            elif grid[r][c] == GOAL:
                goal = (r, c)

    return start, goal


def print_grid(grid, path):
    path_set = set(path)

    for r in range(len(grid)):
        row = ""
        for c in range(len(grid[0])):
            if (r, c) in path_set and grid[r][c] not in [START, GOAL]:
                row += "*"
            else:
                row += grid[r][c]
        print(row)


def in_bounds(pos, num_rows, num_cols):
    return 0 <= pos[0] < num_rows and 0 <= pos[1] < num_cols


def neighbors(pos, num_rows, num_cols):
    neighs = []
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for direction in dirs:
        nxt_pos = tuple(x + y for x, y in zip(pos, direction))

        if in_bounds(nxt_pos, num_rows, num_cols):
            neighs.append(nxt_pos)

    return neighs


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reconstruct_path(parent, start, goal):
    path = []
    curr = goal

    while curr is not None:
        path.append(curr)
        curr = parent[curr]

    path.reverse()
    return path


def bfs(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    start, goal = find_start_goal(grid)

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while len(queue) > 0:
        curr = queue.popleft()

        if curr == goal:
            return reconstruct_path(parent, start, goal)

        for neigh in neighbors(curr, num_rows, num_cols):
            r, c = neigh

            if neigh not in visited and grid[r][c] != WALL:
                visited.add(neigh)
                parent[neigh] = curr
                queue.append(neigh)

    return []


def best_first(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    start, goal = find_start_goal(grid)

    pq = []
    heapq.heappush(pq, (manhattan(start, goal), start))

    visited = {start}
    parent = {start: None}

    while len(pq) > 0:
        _, curr = heapq.heappop(pq)

        if curr == goal:
            return reconstruct_path(parent, start, goal)

        for neigh in neighbors(curr, num_rows, num_cols):
            r, c = neigh

            if neigh not in visited and grid[r][c] != WALL:
                visited.add(neigh)
                parent[neigh] = curr

                priority = manhattan(neigh, goal)
                heapq.heappush(pq, (priority, neigh))

    return []


def run_demo(grid_lines):
    grid = parse_grid(grid_lines)

    algs = {
        "BFS": bfs,
        "Best-first": best_first,
    }

    for alg_name, alg in algs.items():
        path = alg(grid)

        print(alg_name)
        print(path)
        print(f"Path length: {len(path) - 1 if path else 'No path'}")
        print_grid(grid, path)
        print()


run_demo(grid_bfs_better)
run_demo(grid_best_first_better)
# run_demo(grid_astar_better)