import gspread
from google.oauth2.service_account import Credentials

SCOPE = [    
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",    
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('sudoku')

sales = SHEET.worksheet('sudoku')

data = sales .get_all_values()

print(data)


import pyfiglet

txt = pyfiglet.figlet_format("Sudoku Solver", font="big")
solved = pyfiglet.figlet_format("solved", font="big")
print(txt)



print("please enter your sudoku numbers like the example below.")
print("zero = blank space on your sudoku board.")
# sudoku board to solve
sudoku_grid = [
    [0, 0, 1, 0, 0, 0, 0, 0, 7],
    [0, 9, 0, 0, 0, 6, 1, 3, 0],
    [0, 0, 0, 3, 0, 0, 0, 0, 4],
    [0, 6, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 9, 7, 0, 0, 5, 8, 0],
    [0, 0, 5, 8, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0]
]


def solve(sudoku_grid): 
    """
    function to loop through numbers 1 to 9 and call the solve function,
    if sove function return false, reset current number to zero and try again
    """
    find = find_zero(sudoku_grid)
# if this is true the grid has been solved as the function cannot find zero
    if not find:
        return True
    else:
        row, col = find
# loop throught 1 to 9, inputing each number
    for i in range(1, 10):
# if number is possible in position add it to the grid
        if correct(sudoku_grid, i, (row, col)):
            sudoku_grid[row][col] = i
# after possible num added, call solve function to check if correct
            if solve(sudoku_grid):
                return True
# if the solve function dose not return true reset the last number
            sudoku_grid[row][col] = 0
# num = zero, find zero function will run again and input more possible nums
    return False


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
    square_x = pos[1] // 3
    square_y = pos[0] // 3
    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            if sudoku_grid[i][j] == num and (i, j) != pos:
                return False

    return True



def print_grid(grid):
    """
    function to print sudoku grid
    """
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("--------------------")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

print_grid(sudoku_grid)

def find_zero(grid):
    """
    function to find zero in grid,
    zero will be used to represent an empty space
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)
# if no zeros are left on the grid
    return None


#print("your puzzel.------------------------")
users_grid = input('type your grid here:')
print_grid(users_grid)
print('your Grid, ' + users_grid)
#solve(users_grid)

#print(solved)
#print("solution.---------------------")
#print_grid(sudoku_grid)
