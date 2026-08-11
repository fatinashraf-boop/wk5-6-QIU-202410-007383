"""
Assignment starter: A* search on a grid.

Read ../guide.md and ../worked_example.md BEFORE you start coding here.

Your job: fill in every function marked TODO. Do not change function
signatures (the tests in test_astar_grid.py rely on them).

Grid legend:
    'S' = start
    'G' = goal
    '#' = wall (cannot be entered)
    '.' = free cell

Run this file directly to see your solver in action:
    python astar_grid.py
"""
import heapq

# The assignment grid. Do not edit this -- your solver must work on this
# AND on any other valid grid (the test file uses different grids too).
ASSIGNMENT_GRID = [
    "S.......",
    ".#..#.#.",
    ".#....#.",
    ".###.##.",
    "...#....",
    "##.#.##.",
    ".....#..",
    ".##...G.",
]

ROWS = len(ASSIGNMENT_GRID)
COLS = len(ASSIGNMENT_GRID[0])


def find_cell(grid, symbol):
    """Return the (row, col) of `symbol` in `grid`. Already implemented."""
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == symbol:
                return (r, c)
    raise ValueError(f"Symbol {symbol!r} not found in grid")


def is_walkable(grid, r, c):
    """Return True if (r, c) is inside the grid and not a wall.

    Already implemented -- use this inside your neighbours() function.
    """
    rows, cols = len(grid), len(grid[0])
    if not (0 <= r < rows and 0 <= c < cols):
        return False
    return grid[r][c] != "#"


def neighbours(grid, node):
    """
    Return all valid neighbouring cells.
    """

    r, c = node

    # Up, Down, Left, Right
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dr, dc in directions:

        nr = r + dr
        nc = c + dc

        if is_walkable(grid, nr, nc):
            yield (nr, nc)


def heuristic(node, goal):
    """
    Manhattan Distance
    """

    r, c = node
    gr, gc = goal

    return abs(r - gr) + abs(c - gc)


def reconstruct_path(came_from, current):
    """Rebuild the path from start to `current` using the came_from map.

    Already implemented.
    """
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def astar(grid, start, goal):

    open_heap = []

    g_score = {
        start: 0
    }

    came_from = {}

    closed = set()

    start_f = heuristic(start, goal)

    heapq.heappush(
        open_heap,
        (start_f, 0, start[0], start[1], start)
    )

    while open_heap:

        f, neg_g, row, col, current = heapq.heappop(open_heap)

        if current in closed:
            continue

        if current == goal:
            return reconstruct_path(came_from, current), g_score[current]

        closed.add(current)

        for nb in neighbours(grid, current):

            if nb in closed:
                continue

            tentative_g = g_score[current] + 1

            if (
                nb not in g_score
                or tentative_g < g_score[nb]
            ):

                came_from[nb] = current

                g_score[nb] = tentative_g

                f = tentative_g + heuristic(nb, goal)

                heapq.heappush(
                    open_heap,
                    (
                        f,
                        -tentative_g,
                        nb[0],
                        nb[1],
                        nb
                    )
                )

    return None, float("inf")


if __name__ == "__main__":
    start = find_cell(ASSIGNMENT_GRID, "S")
    goal = find_cell(ASSIGNMENT_GRID, "G")
    print(f"Start: {start}, Goal: {goal}")

    path, cost = astar(ASSIGNMENT_GRID, start, goal)

    if path:
        print(f"Path found (cost={cost}):")
        print(" -> ".join(str(p) for p in path))
    else:
        print("No path exists.")
