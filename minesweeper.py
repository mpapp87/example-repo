def count_adjacent_mines(grid, row, col):
    mine_count = 0

    for row_offset in range(-1, 2):
        for col_offset in range(-1, 2):
            # Do not check the current cell.
            if row_offset == 0 and col_offset == 0:
                continue

            neighbour_row = row + row_offset
            neighbour_col = col + col_offset

            # Check that the neighbouring position is within the grid.
            if (
                0 <= neighbour_row < len(grid)
                and 0 <= neighbour_col < len(grid[neighbour_row])
                and grid[neighbour_row][neighbour_col] == "#"
            ):
                mine_count += 1

    return mine_count


def create_minesweeper_grid(grid):
    result = []

    for row_index, row in enumerate(grid):
        new_row = []

        for col_index, cell in enumerate(row):

            if cell == "#":
                new_row.append("#")
            else:
                new_row.append(count_adjacent_mines(grid, row_index, col_index))

        result.append(new_row)

    return result


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

grid = []

print(f"\nEnter {rows} rows using only '#' for mines and '-' for empty spaces.")

for i in range(rows):
    while True:
        row = input(f"Row {i + 1}: ")

        if len(row) != cols:
            print(f"Error: Row must contain exactly {cols} characters.")
        elif any(char not in "#-" for char in row):
            print("Error: Only '#' and '-' are allowed.")
        else:
            grid.append(list(row))
            break

# Generate the minesweeper grid
result = create_minesweeper_grid(grid)

print("\nResult:")

for row in result:
    print(row)
