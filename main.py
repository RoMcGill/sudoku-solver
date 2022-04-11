import gspread
from google.oauth2.service_account import Credentials
import pyfiglet
import pandas as pd


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3')
ws = SHEET.worksheet('puzzel')
name_worksheet = SHEET.worksheet('name')

def get_name_data():
    """
    Get name figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    print("Please enter your name .")
   
    data_str = input("Enter your data here: ")
    

    update_name_worksheet(name_data)
    
    

    

def update_name_worksheet(data):
    """
    Update name worksheet, add new row with the list data provided
    """
    print("Updating name worksheet...\n")
    name_worksheet = SHEET.worksheet("name")
    name_worksheet.append_row(data)
    print("name worksheet updated successfully.\n")




def get_puzzel_data():
    """
    Get puzzel figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 9 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """

    count = 0
    while True:
        print("Please enter your puzzel data.")
        print("Data should be 9 numbers, separated by commas.")
        print("Example: 1,0,0,4,7,3,9,8,7\n")

        data_str = input("Enter your data here: ")

        puzzel_data = data_str.split(",")

        if validate_data(puzzel_data):
            print("puzzel is valid!")
            count = count + 1

        update_puzzel_worksheet(puzzel_data)
        print(count)

        if count == 9:
            break
            

def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 9 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 9:
            raise ValueError(
                f"Exactly 9 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_puzzel_worksheet(data):
    """
    Update puzzel worksheet, add new row with the list data provided
    """
    
    print("Updating puzzel worksheet...\n")
    puzzel_worksheet = SHEET.worksheet("puzzel")
    puzzel_worksheet.append_row(data)


    print("puzzel worksheet updated successfully.\n")


def solve(grid): 
    """
    function to loop through numbers 1 to 9 and call the solve function,
    if sove function return false, reset current number to zero and try again
    """
    print('solving')
    find = find_zero(grid)
# if this is true the grid has been solved as the function cannot find zero

    if not find:
        return True
        print('did not find zero')
    else:
        row, col = find
        print('no zero found')
# loop throught 1 to 9, inputing each number
    for i in range(1, 10):
        print('looping thru')
# if number is possible in position add it to the grid
        if correct(grid, i, (row, col)):
            grid[row][col] = i
            print('adding numbers')
# after possible num added, call solve function to check if correct
            if solve(grid):
                return True
                print_grid(grid)
# if the solve function dose not return true reset the last number
            grid[row][col] = 0
            print('trying new number')
# num = zero, find zero function will run again and input more possible nums
    return False

def correct(grid, num, pos):
    """
    finds if the current game is correct or valid
    """
    print('validating grid')
    # check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # check square
    square_x = pos[1] // 3
    square_y = pos[0] // 3
    for i in range(square_y * 3, square_y * 3 + 3):
        for j in range(square_x * 3, square_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

def print_grid(grid):
    """
    function to print sudoku grid
    """
    print('printing grid')
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("--------------------------------")
            

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="" +",")



def find_zero(grid):
    """
    function to find zero in grid,
    zero will be used to represent an empty space
    """
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)
                print('found zero')
# if no zeros are left on the grid
    return None











def main():
    #get_name_data()
    #update_name_worksheet(name_data)
    get_puzzel_data()
    grid = ws.get('A1:I9')
    print_grid(grid)
    solve(grid)
    #print_grid(grid)
    


txt = pyfiglet.figlet_format("Sudoku Solver", font="big")
solved = pyfiglet.figlet_format("solved", font="big")
print(txt)

main()