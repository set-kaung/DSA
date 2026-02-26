import random

def create_maze(width, height):
    # Ensure width and height are odd to create walls properly
    if width % 2 == 0: width += 1
    if height % 2 == 0: height += 1

    # Initialize the maze with walls (1)
    maze = [[1 for _ in range(width)] for _ in range(height)]

    # Directions for movement (down, up, right, left)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Stack for the iterative backtracking
    stack = []
    start_x, start_y = 1, 1  # Start position
    maze[start_y][start_x] = 0  # Mark start position as a path (0)
    stack.append((start_x, start_y))

    while stack:
        x, y = stack[-1]  # Get the current position

        # Find all valid neighbors
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                neighbors.append((nx, ny, dx, dy))

        if neighbors:
            # Choose a random neighbor
            nx, ny, dx, dy = random.choice(neighbors)
            # Carve a path between the current cell and the chosen neighbor
            maze[y + dy][x + dx] = 0  # Remove the wall between
            maze[ny][nx] = 0  # Mark the new position as a path (0)
            stack.append((nx, ny))  # Push the new position to the stack
        else:
            stack.pop()  # Backtrack if no valid neighbors

    # Optionally, ensure there's an exit
    maze[height - 2][width - 1] = 0  # Make bottom right corner a path

    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(str(cell) for cell in row))

def main():
    width, height = 2001, 2001  # Set maze dimensions (must be odd numbers)
    maze = create_maze(width, height)
    print(f"{width} {height}")
    print(f"{1} {1}")
    print(f"{width-2} {height-2}")
    print_maze(maze)

if __name__ == "__main__":
    main()
