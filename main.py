import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def Google_sheet_to_csv(sheetName,fileName):
    
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("YourOwnCreds.json",scope)
    client = gspread.authorize(creds)

    
    homeSheetName = sheetName
    homeSheet = client.open(homeSheetName).sheet1
    homeData = homeSheet.get_all_records()
    
    hd = pd.DataFrame(homeData)
    
    HomeFileName = fileName
    hd.to_csv(HomeFileName +'.csv',index=False)


