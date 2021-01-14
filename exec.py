import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)

client = gspred.authorize(creds)

sheet = client.open('PythonSheets').sheet1

# acess data
print(sheet.get_all_records())
