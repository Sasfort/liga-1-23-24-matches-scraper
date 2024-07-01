from typing import Iterable
import scrapy
from scrapy_selenium import SeleniumRequest
from liga_1_scraper.items import MatchStatsItem

class MatchStatsSpider(scrapy.Spider):
    name = 'match_stats'
    allowed_domains = ['ligaindonesiabaru.com']
    start_urls = [
        'https://ligaindonesiabaru.com/fixtures/index/BRI_LIGA_1_2023-2024/1/0'
    ]

    def parse(self, response):
        matches = response.css('a.table-row')
        for match in matches:
            match_url = match.attrib['href']

            yield SeleniumRequest(
                url = match_url, 
                callback = self.parse_match_stats,
                meta = {
                    'week': response.url.split(sep = '/')[6]
                },
                wait_time = 10,
                script = "document.querySelectorAll('#myTab a')[2].click()"
            )

        next_page = response.css('form a::attr(href)')[1].get()

        if next_page != '#':
            yield response.follow(next_page, callback = self.parse)

    def parse_match_stats(self, response):
        match_stat = MatchStatsItem()

        result = response.css('.result-match::text')[0].get().split(sep = ':')
        stadium = response.css('.result-location ul li::text')[3].get().split(sep = ',')
        stats = response.css('#matchstats div .col-lg-12 ul li span::text')

        match_stat['week'] = response.meta['week']
        match_stat['stadium'] = stadium[0].strip() + ', ' + stadium[1].strip()

        match_stat['home_team'] = response.css('.team a::text')[1].get().strip()
        match_stat['home_score'] = result[0].strip()
        match_stat['home_possession'] = stats[0].get()
        match_stat['home_shot_on_target'] = stats[3].get()
        match_stat['home_shot'] = stats[6].get()
        match_stat['home_shot_accuracy'] = stats[9].get()
        match_stat['home_pass_success'] = stats[12].get()
        match_stat['home_pass_fail'] = stats[15].get()
        match_stat['home_corner_kick'] = stats[18].get()
        match_stat['home_tackle_success'] = stats[21].get()
        match_stat['home_offside'] = stats[24].get()
        match_stat['home_foul'] = stats[27].get()
        match_stat['home_yellow_card'] = stats[30].get()
        match_stat['home_red_card'] = stats[33].get()
        
        match_stat['away_team'] = response.css('.team a::text')[2].get().strip()
        match_stat['away_score'] = result[1].strip()
        match_stat['away_possession'] = stats[2].get()
        match_stat['away_shot_on_target'] = stats[5].get()
        match_stat['away_shot'] = stats[8].get()
        match_stat['away_shot_accuracy'] = stats[11].get()
        match_stat['away_pass_success'] = stats[14].get()
        match_stat['away_pass_fail'] = stats[17].get()
        match_stat['away_corner_kick'] = stats[20].get()
        match_stat['away_tackle_success'] = stats[23].get()
        match_stat['away_offside'] = stats[26].get()
        match_stat['away_foul'] = stats[29].get()
        match_stat['away_yellow_card'] = stats[32].get()
        match_stat['away_red_card'] = stats[35].get()

        yield match_stat
