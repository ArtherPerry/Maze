import random

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[1 for _ in range(width)] for _ in range(height)]
        self.generate_maze()
        self.print_maze()  # Print maze to console for debugging

    def generate_maze(self):
        stack = [(0, 0)]
        self.maze[0][0] = 0

        while stack:
            x, y = stack[-1]
            directions = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
            random.shuffle(directions)
            for nx, ny in directions:
                if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 1:
                    self.maze[ny][nx] = 0
                    self.maze[(ny + y) // 2][(nx + x) // 2] = 0
                    stack.append((nx, ny))
                    break
            else:
                stack.pop()

    def print_maze(self):
        for row in self.maze:
            print(' '.join(str(cell) for cell in row))
        print()
