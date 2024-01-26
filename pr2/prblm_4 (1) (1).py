def main():
    size = int(input("Enter the size of the grid: "))
    marker_position = [0, 0]  # Initial position of the marker
    grid = [['.' for _ in range(size)] for _ in range(100)]  # Create the grid

    grid[marker_position[0]][marker_position[1]] = '*'  # Place the marker at the initial position

    # Update the grid based on user input
    user_input = input("Enter the movement (R, L, B to move right, left, or back): ")
    while user_input != "END":
        if user_input == "L":
            if marker_position[0] - 1 >= 0:
                marker_position[0] -= 1
        elif user_input == "R":
            if marker_position[0] < size - 1:
                marker_position[0] += 1
        elif user_input == "B":
            marker_position[1] += 1
        grid[marker_position[1]][marker_position[0]] = '*'  # Update the marker position
        user_input = input("Enter the movement (R, L, B to move right, left, or back): ")

    # Remove duplicate grids and print the final grid
    unique_grids = [grid.pop(0) for _ in range(len(grid)) if grid[0] != grid]
    for row in unique_grids:
        print(' '.join(row))
    if marker_position[0] != size - 1:
        print("There's no way out!")

if __name__ == "__main__":
    main()
