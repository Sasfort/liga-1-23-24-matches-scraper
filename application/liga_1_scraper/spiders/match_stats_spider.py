import scrapy
from scrapy_selenium import SeleniumRequest
from liga_1_scraper.items import MatchStatsItem

class MatchStatsSpider(scrapy.Spider):
    name = "match_stats"
    allowed_domains = ["ligaindonesiabaru.com"]
    start_urls = ["https://ligaindonesiabaru.com/fixtures/index/BRI_LIGA_1_2023-2024/1/0"]

    def parse(self, response):
        matches = response.css('a.table-row')
        for match in matches:
            # match_url = match.attrib['href']

            # yield response.follow(match_url, callback = self.open_match)

            yield {
                'home': match.css('td b::text')[0].get(),
                'away': match.css('td b::text')[1].get(),
                'score': match.css('span.badge::text').get()[1:],
                'stadium': match.css('td::text')[10].get().strip(),
                'url': match.attrib['href']
            }

        next_page = response.css('form a::attr(href)')[1].get()

        if next_page != '#':
            yield response.follow(next_page, callback = self.parse)

    # def open_match(self, response):
    #     yield response.follow()

    # def parse_match(self, response):
    #     pass
