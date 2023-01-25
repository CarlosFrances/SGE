import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"] # conexion a las apis necesarias
creds = ServiceAccountCredentials.from_json_keyfile_name("claves.json",scope) # recoger la clave JSON del archivo claves.json
client = gspread.authorize(creds) #autorizar con la clave JSON 
sheet = client.open("puntuacion_profesores").sheet1 # sheet1 elige la primera hoja de excel

# acceso a datos
#records=sheet.get_all_records() saca toda la hoja excel en formato [{}]
#records = sheet.col_values(1) saca los valores de la columna 1.  print(records[1:]) saca solo los valores
records = sheet.col_values(3)
records = records[1:]
#records = [int(records) for records in records] transforma el array de strings a enteros
def mediaNotas(arr):
    return sum(arr) / len(arr)


print(mediaNotas(records))