
from ExportTools import Sheets
from BovadaData import BovadaData
import logging
import yaml

class Main:
    def __init__( self ): #webpage, spread_title, sheet_name):

        with open(r'config.yaml') as f:

            config = yaml.load(f, Loader=yaml.FullLoader)


        self.logger = logging.getLogger('bovada_scrape')
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
     
        remote_selenium_url = "{}:{}/wd/hub".format(config['remote_selenium_name'], config['port'])

        self.bv = BovadaData( remote_selenium_url )

        self.sheet = Sheets()

        # update next 2 vars to reflect names of spreadsheet & sheet within
        self.url = config['google_sheet_url'] #"https://docs.google.com/spreadsheets/d/1HnGtA8NJffGePtZn-KqZUl7PH9uR_lOA3EdN-Jxh7xg/edit?usp=sharing"
        self.sheet_name = config['google_sheet_tab']

    def run(self):

            bets_dat = self.bv.bovada_scrape("https://www.bovada.lv/sports/soccer")
            self.sheet.input(bets_dat , self.url, self.sheet_name)

            self.logger.info("scraped bovada soccer, find results in sheet: {}, for url: {}".format(self.sheet_name, self.url))


if __name__ == '__main__':
    Main().run()