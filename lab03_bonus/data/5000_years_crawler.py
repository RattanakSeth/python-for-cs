
import csv
import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

"""
You can't crawl this, https://www.5000-years.org/robots.txt
"""
class FiveThousandYearSpider(scrapy.Spider):
    name = 'article 5000 years'

    # response = requests.get(url, headers=headers)
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        URL = 'https://www.5000-years.org/kh/read/3225'
        yield scrapy.Request(url=URL, headers=headers,  callback=self.response_parser)

    def response_parser(self, response):
        for selector in response.css('div.font_full_description'):  # Adjust selector to target the correct elements
            paragraphs = selector.css('span::text').getall()  # Get all text content from <p> elements
            yield {
                'title': ' '.join(paragraphs)  # Combine all paragraph texts into a single string
            }

        # next_page_link = response.css('li.next a::attr(href)').extract_first()
        # if next_page_link:
        #     yield response.follow(next_page_link, callback=self.response_parser)



def book_spider_result():
    results = []

    def crawler_results(item):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)
    crawler_process = CrawlerProcess()
    crawler_process.crawl(FiveThousandYearSpider)
    crawler_process.start()
    return results


if __name__ == '__main__':
    books_data=book_spider_result()
    text = ""
    for d in books_data:
        text += d['title'] + "\n"
    # print(books_data)
    # keys = books_data[0].keys()
    # print(keys
    #       )
    with open('data/five_thousand_year_1.txt', 'w', newline='') as output_file_name:
        output_file_name.write(text)
        output_file_name.close()
        # writer = csv.DictWriter(output_file_name, keys)
        # writer.writeheader()
        # writer.writerows(books_data)

