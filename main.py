import tkinter as tk
from maze import Maze
from maze_solver import MazeSolver

class MazeGUI:
    def __init__(self, root, maze, solver):
        self.root = root
        self.maze = maze
        self.solver = solver
        self.cell_size = 20
        self.canvas = tk.Canvas(root, width=maze.width * self.cell_size, height=maze.height * self.cell_size)
        self.canvas.pack()

        # Schedule drawing and solving the maze after the GUI has been initialized
        self.root.after(100, self.draw_maze)
        self.root.after(200, self.solve_maze)

    def draw_maze(self):
        print("Drawing maze...")
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                color = "black" if self.maze.maze[y][x] == 1 else "white"
                self.canvas.create_rectangle(
                    x * self.cell_size, y * self.cell_size,
                    (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                    fill=color, outline="grey"
                )
        print("Maze drawn")

    def solve_maze(self):
        print("Solving maze...")
        if self.solver.solve():
            for x, y in self.solver.path:
                self.canvas.create_rectangle(
                    x * self.cell_size, y * self.cell_size,
                    (x + 1) * self.cell_size, (y + 1) * self.cell_size,
                    fill="blue", outline="blue"
                )
            print("Maze solved")
        else:
            print("No solution found!")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Maze Solver")
    width, height = 21, 21
    maze = Maze(width, height)
    solver = MazeSolver(maze.maze)
    gui = MazeGUI(root, maze, solver)
    root.mainloop()
