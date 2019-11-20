import scrapy
import pandas as pd 

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):


        nba_urls = []

        for i in range(11):
            nba_urls.append('https://www.basketball-reference.com/leagues/NBA_20' + str(i + 10) +'_per_game.html')

        for nba_url in nba_urls:
            yield scrapy.Request(url=nba_url, callback=self.load_nba)



    def load_nba(self, response):
        filename = "advancedstats.html"

        # with open(filename, "wb") as f:
        #     f.write(response.body)
        html = response.css("tr")
        for player_row in html:
            print()
            print(player_row.css("th::text").get())
            print(player_row.css("td").css("a::text").get())
            # print(player_row.css("td::text").get())
            for stats in player_row.css("td::text"):
                print(stats.get())
            print()