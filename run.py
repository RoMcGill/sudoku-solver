# sudoku board to solve
sudoku_grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

def solve(sudoku_grid):
    """
    function to backtrack by calling the function inside its self
    our completed sudoku grid will be the basecase for the recursion 
    """
    find = find_zero(sudoku_grid)
    #if this is true the grid has been solved 
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if correct(sudoku_grid, i, (row, col)):
            sudoku_grid[row][col] = i
            
            if solve (sudoku_grid):
                return True
            sudoku_grid[row][col] = 0 
def correct(sudoku_grid, num, pos):
    """
    finds if the current game is correct or valid
    """
    # check row
    for i in range(len(sudoku_grid[0])):
        if sudoku_grid[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(sudoku_grid)):
        if sudoku_grid[i][pos[1]] == num and pos[0] != i:
            return False

    # check square
    square x = pos [1] // 3
    square y = pos [0] // 3
    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range (square_x * 3, square_x * 3 + 3):
            if sudoku_grid[i][j] == num and (i,j) != pos:
                return False

    return True


def print_grid(grid):
    """
    function to print sudoku grid
    """
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


def find_zero(grid):
    """
    function to find zero in grid,
    zero will be used to represent an empty space
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)
#if no zeros are left on the grid 
    return None

print_grid(sudoku_grid)