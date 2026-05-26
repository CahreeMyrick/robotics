from collections import deque
import heapq

WALL = "#"
FREE = "."
START = "S"
GOAL = "G"


# Demo 1: BFS is good because the goal is very close.
grid_bfs_better = [
    "S.G....",
    ".......",
    ".......",
    ".......",
]

# Demo 2: Best-first is good because the heuristic leads almost directly to the goal.
# It usually expands very few nodes.
grid_best_first_better = [
    "S........G",
    "#########.",
    "..........",
]

# Demo 3: A* is best because it avoids BFS's broad search,
# but still guarantees a shortest path unlike greedy best-first.
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
    start = goal = None

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == START:
                start = (r, c)
            elif grid[r][c] == GOAL:
                goal = (r, c)

    return grid, start, goal

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
    if (pos[0] >= 0 and pos[0] < num_rows) and (pos[1] >= 0 and pos[1] < num_cols):
        return True
    return False

def neighbors(pos, num_rows, num_cols):
    neighs = []
    dirs = {(1, 0), (-1, 0), (0, 1), (0, -1)}

    for dir in dirs:
        nxt_pos = tuple(x+y for x,y in zip(pos, dir))
        if not in_bounds(nxt_pos, num_rows, num_cols):
            continue
        neighs.append(nxt_pos)

    # print("nieghs", neighs)
    # breakpoint()
    return neighs

def bfs(grid):
    # num rows and cols
    num_rows = len(grid)
    num_cols = len(grid[0])

    # initialize visited and queue and sol
    queue = deque([(0, 0)])
    visited = {(0,0)}
    sol = [(0,0)]

    while len(queue) > 0:

        # curr node
        curr = queue.popleft()

        for neigh in neighbors(curr, num_rows, num_cols):
            if neigh not in visited and grid[neigh[0]][neigh[1]] != WALL:
                visited.add(neigh)
                queue.append(neigh)
                sol.append(neigh)
                # print("sol", sol)
                if grid[neigh[0]][neigh[1]] == GOAL:
                    return sol
    return sol

def run_demo(grid):
    path = bfs(grid)
    print(path)

run_demo(grid_bfs_better)
