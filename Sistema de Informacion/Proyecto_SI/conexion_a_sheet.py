import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("claves.json",scope)
client = gspread.authorize(creds)
sheet = client.open("recepcion_formulario").sheet1

# acceso a datos
print(sheet.get_all_records())