#221002268 - Sheikh Adnan Mostofa
def iddfs_maze(grid, start, target):
    rows, cols = len(grid), len(grid[0])

    max_depth = sum(grid[i][j] == 0 for i in range(rows) for j in range(cols))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def dls(node, depth, limit, visited, path):
        if node == target:
            return True

        if depth == limit:
            return False

        r, c = node
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < rows and
                0 <= nc < cols and
                grid[nr][nc] == 0 and
                (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                path.append((nr, nc))

                if dls((nr, nc), depth + 1, limit, visited, path):
                    return True

                visited.remove((nr, nc))
                path.pop()

        return False

    for depth_limit in range(max_depth + 1):
        visited = {start}
        path = [start]

        if dls(start, 0, depth_limit, visited, path):
            print(f"Path found at depth {depth_limit} using IDDFS")
            print(f"Traversal Order: {path}")
            return

    print(f"Path not found at max depth {max_depth} using IDDFS")


with open("IDDFSInput.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

rows, cols = map(int, lines[0].split())

grid = []
for i in range(1, rows + 1):
    grid.append(list(map(int, lines[i].split())))

start = tuple(map(int, lines[rows + 1].split(":")[1].split()))
target = tuple(map(int, lines[rows + 2].split(":")[1].split()))

iddfs_maze(grid, start, target)
