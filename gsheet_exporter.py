import gspread
from google.oauth2.service_account import Credentials

def export_to_gsheet(data, sheet_name):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    client = gspread.authorize(creds)

    sheet = client.open(sheet_name).sheet1

    sheet.clear()
    sheet.append_row(list(data[0].keys()))

    for row in data:
        sheet.append_row(list(row.values()))
