
from ExportTools import Sheets
from BovadaData import BovadaData
import logging

class Main:
    def __init__( self ): #webpage, spread_title, sheet_name):
        self.logger = logging.getLogger('bovada_scrape')
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
     
        self.bv = BovadaData()

        self.sheet = Sheets()

        # update next 2 vars to reflect names of spreadsheet & sheet within
        self.url = "https://docs.google.com/spreadsheets/d/13SFoQusyqTlx6ghqyvHZ7G3UsE9wjmZ3y0jGJ_ULaII/edit#gid=0"#"https://docs.google.com/spreadsheets/d/1HnGtA8NJffGePtZn-KqZUl7PH9uR_lOA3EdN-Jxh7xg/edit?usp=sharing"
        self.sheet_name = "Test2"

    def run(self):

            bets_dat = self.bv.bovada_scrape("https://www.bovada.lv/sports/soccer")
            self.sheet.input(bets_dat , self.url, self.sheet_name)

            self.logger.info("scraped bovada soccer, find results in sheet: {}, for url: {}".format(self.sheet_name, self.url))


if __name__ == '__main__':
    Main().run()