from collections import deque
import heapq

WALL = "#"
FREE = "."
START = "S"
GOAL = "G"

def parse_grid(lines):
    pass

def print_grid(grid, path):
    pass


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
