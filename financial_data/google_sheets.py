import gspread
from oauth2client.service_account import ServiceAccountCredentials


def authenticate_google_sheets(credentials_path):
    """
    Authenticates and returns a Google Sheets client.

    Parameters:
    credentials_path (str): Path to the JSON credentials file.

    Returns:
    gspread.Client: Authenticated Google Sheets client.
    """
    scope = ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(credentials)
    return client


def dump_to_sheet(df, column_range, target_rows, sheet):
    """
    Dumps rows and columns from a DataFrame to a Google Sheets spreadsheet.

    :param df: The pandas DataFrame containing the data.
    :param column_range: Tuple specifying the start and end column indexes (0-based).
    :param target_rows: List of target row numbers in the spreadsheet (1-based).
    :param sheet: The gspread sheet object where the data will be written.
    """
    
    # Iterate over the extracted data and write it to the specified target rows in the sheet
    for idx, (index, row) in enumerate(df.iterrows()):
        target_row = target_rows[idx]
        cell_range = gspread.utils.rowcol_to_a1(target_row, column_range[0] + 1)
        # Convert the row to a list and adjust for 1-based column index in Google Sheets
        sheet.update(cell_range, [row.values.tolist()])

