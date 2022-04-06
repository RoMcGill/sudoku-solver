import gspread
from google.oauth2.service_account import Credentials

import pyfiglet

txt = pyfiglet.figlet_format("Sudoku Solver", font="big")
solved = pyfiglet.figlet_format("solved", font="big")
print(txt)

SCOPE = [    
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",    
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('sudoku')

def get_name_data():
    """
    Get name figures input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    print("Please enter your name .")
    data_str = input("Enter your name here: ")

       
def update_name_worksheet(data):
    """
    Update name worksheet, add new row with the list data provided
    """
    print("Updating name worksheet...\n")
    name_worksheet = SHEET.worksheet("name")
    name_worksheet.append_row(data)
    print("name worksheet updated successfully.\n")


data = get_name_data()
update_name_worksheet(data)

