import gspread
from google.oauth2.service_account import Credentials
import pyfiglet



SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project3')


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




def main():
    get_puzzel_data()

txt = pyfiglet.figlet_format("Sudoku Solver", font="big")
solved = pyfiglet.figlet_format("solved", font="big")
print(txt)

main()