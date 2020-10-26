import gspread
from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()
credentials = credentials.create_scoped(['https://spreadsheets.google.com/feeds'])

client = gspread.authorize(credentials)

sheet = client.open('Covidality_Sheet').sheet1

data = sheet.get_all_records()

print(data)


