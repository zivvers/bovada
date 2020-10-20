
import pickle
import os.path

from oauth2client.service_account import ServiceAccountCredentials
import gspread


class Sheets():

    def __init__(self):

        credential = ServiceAccountCredentials.from_json_keyfile_name("creds/credentials.json",
                                                              ["https://spreadsheets.google.com/feeds"
                                                              , "https://www.googleapis.com/auth/spreadsheets"
                                                              , "https://www.googleapis.com/auth/drive.file"
                                                              , "https://www.googleapis.com/auth/drive"])

        self.client = gspread.authorize(credential)

 
    def input(self, data, spread_url, sheet_name):
        gsheet = self.client.open_by_url(spread_url)
        
        if sheet_name:
            sh = gsheet.worksheet(sheet_name)
        else:
            sh = gsheet.get_worksheet(0)

        sh.insert_rows(data, value_input_option='USER_ENTERED')


