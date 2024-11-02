from dotenv import load_dotenv
import os

load_dotenv()

SPREADSHEETS_FILE_URL = os.getenv("SPREADSHEET_URL")
TL_SHEET_NAME = "ТЛ Асанали"
