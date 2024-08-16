class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.width = len(maze[0])
        self.height = len(maze)
        self.path = []
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]

    def solve(self, x=0, y=0):
        if not (0 <= x < self.width and 0 <= y < self.height) or self.maze[y][x] == 1 or self.visited[y][x]:
            return False

        self.visited[y][x] = True
        self.path.append((x, y))

        if (x, y) == (self.width - 1, self.height - 1):
            return True

        if (self.solve(x + 1, y) or
                self.solve(x - 1, y) or
                self.solve(x, y + 1) or
                self.solve(x, y - 1)):
            return True

        self.path.pop()
        return False
