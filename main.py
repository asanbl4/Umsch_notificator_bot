import csv
from cred import client
from dotenv import load_dotenv
import os

load_dotenv()

SPREADSHEETS_FILE_URL = os.getenv("SPREADSHEET_URL")
TL_SHEET_NAME = "ТЛ Асанали"

sheet = client.open_by_url(SPREADSHEETS_FILE_URL).worksheet(TL_SHEET_NAME)

data = sheet.get_all_records()

# Собираем данные в csv файл
with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

