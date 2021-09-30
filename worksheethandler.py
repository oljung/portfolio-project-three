import gspread
from google.oauth2.service_account import Credentials


class WorksheetHandler:
    """
    This is a utility class to handle fetching data from and updating
    a worksheet
    """
    SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
    CREDS = Credentials.from_service_account_file('creds.json')
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open('highscore_table')

    def get_worksheet_data(name):
        """
        This method gets all the values from the desired worksheet
        """
        worksheet = WorksheetHandler.SHEET.worksheet(name)
        data = worksheet.get_all_values()
        return data

