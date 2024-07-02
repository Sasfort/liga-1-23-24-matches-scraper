# Liga 1 23/24 Season Match Stats Scraper

## Overview
A web scraping project using Scrapy and Selenium to collect the statistics of every match in the Liga 1 23/24 season from PSSI's website.

## Folder Structure
application/ => Contains the code used to initiate the web scraping and generate the result into CSV\
results/ => Contains the result of the application. The final result is stored in the file named match-stats-final.csv

## How to Run the Code
1. Clone the repository
2. Open the project folder
3. Create and activate a Python virtual environment
4. Navigate to the application/liga_1_scraper folder
5. Run this command: scrapy crawl match_stats
6. The result would be in a file named match-stats.csv
