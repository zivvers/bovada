
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By 
from datetime import datetime

from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd
from pytz import timezone
from bs4 import BeautifulSoup



class BovadaData:
    def __init__(self):
        
        #self.initURL = initURL

        self.driver = webdriver.Remote(
            command_executor='remote-webdriver:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME )

        #self.bovada_scrape(self.initURL)

    # takes beautifulsoup event group, returns dat for games
    def scrape_group(self, group, scrape_time):
    
        group_title = group.find('a', {'class' : 'league-header-collapsible__description'}).get_text().strip()
        print(f"LEAGUE: {group_title}")
        games = group.find_all("sp-coupon")
        print(f"# games to scrape: {len(games)}")
        
        poten_winners = [ elem.get_text() for elem in group.find_all('h4', {'class':['competitor-name']}) ]

        bets = [ elem.get_text() for elem in group.find_all("span", {"class":"bet-price"}) ]

        game_times = [elem.parent.get_text().strip() for elem in group.find_all('time', {'class':'clock'})[::2]]
        
        teams = list(zip(poten_winners[::2], poten_winners[1::2]))
        odds = list(zip(bets[2::7], bets[3::7], bets[4::7]))

        print(f'# teams: {len(teams)}')
        print(f'# odds: {len(odds)}')
        print(f'# game_times: {len(game_times)}')
        #assert(len(teams) == len(odds))

        rows = []
        for i in range(len(teams)):

            try:
                # "scrape_time", "league_name", "game_time", team_1", "team_2", "odds_team_1", "odds_team_2", "odds_draw"
                row = [scrape_time, group_title, game_times[i], teams[i][0], teams[i][1], odds[i][0], odds[i][1], odds[i][2]]
                
                rows.append( row )
                
                #print(f"SUCCESS: {row}")
            except:

                print(f"could not parse game in {group_title}")

        return rows





        #for game in games:
        #
        #    print( game.find_all('h4', {'class':'competitor-name'}).apply(lambda x: x.get_text()) )
        #
        #    team_1, team_2  = game.find_all('h4', {'class':'competitor-name'}).apply(lambda x: x.get_text())
        #    print(f"{team_1} vs. {team_2}")

    def bovada_scrape(self, url="https://www.bovada.lv/sports/soccer"):

        self.driver.get(url)
        #self.driver.implicitly_wait(5)
        
        #try:
        print("awaiting load...")

        happening_elem = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.next-events-bucket"))
        )

        # selenium elemet grabbing a bit slow... let's grab HTML & parse
        soup = BeautifulSoup(happening_elem.get_attribute('innerHTML'), features="html.parser")
        scrape_time = datetime.now(timezone('US/Eastern')).strftime("%m/%d/%Y, %H:%M:%S")
        grouped_events = soup.find_all('div', {'class':'grouped-events'})

        print(f"# grouped events: {len(grouped_events)}")

        all_bets = [["scrape_time", "league_name", "game_time", "team_1", "team_2", "odds_team_1", "odds_team_2", "odds_draw"]]

        # loop through all the grouped events (leagues)
        for grouped_event in grouped_events:



            group = grouped_event
            self.group = group
            all_bets = all_bets + self.scrape_group( grouped_event, scrape_time )

        return all_bets