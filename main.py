from scraper import fetch_nse_data
from gsheet_exporter import export_to_gsheet

SHEET_NAME = "NSE_MARKET_MOVERS"

def main():
    data = fetch_nse_data()
    export_to_gsheet(data, SHEET_NAME)
    print("Google Sheet updated successfully")

if __name__ == "__main__":
    main()
