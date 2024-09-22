
import csv
import scrapy
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

class FreshNewSpider(scrapy.Spider):
    name = 'books'

    def start_requests(self):
        # URL = 'https://freshnewsasia.com/index.php/en/localnews/356566-2024-09-04-08-01-29.html'
        # URL = 'https://freshnewsasia.com/index.php/en/localnews/356585-2024-09-04-08-54-38.html'
        # URL = 'https://freshnewsasia.com/index.php/en/localnews/356549-2024-09-04-05-45-08.html'
        # URL = 'https://freshnewsasia.com/index.php/en/business/356608-2024-09-04-10-11-49.html'
        URL = 'https://freshnewsasia.com/index.php/en/localnews/356579-2024-09-04-08-37-41.html'
        yield scrapy.Request(url=URL, callback=self.response_parser)

    def response_parser(self, response):
        for selector in response.css('div[itemprop]'):  # Adjust selector to target the correct elements
            paragraphs = selector.css('p::text').getall()  # Get all text content from <p> elements
            yield {
                'title': ' '.join(paragraphs)  # Combine all paragraph texts into a single string
            }

        # next_page_link = response.css('li.next a::attr(href)').extract_first()
        # if next_page_link:
        #     yield response.follow(next_page_link, callback=self.response_parser)



def book_spider_result():
    books_results = []

    def crawler_results(item):
        books_results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)
    crawler_process = CrawlerProcess()
    crawler_process.crawl(FreshNewSpider)
    crawler_process.start()
    return books_results


if __name__ == '__main__':
    books_data=book_spider_result()
    text = ""
    for d in books_data:
        text += d['title'] + "\n"
    # print(books_data)
    # keys = books_data[0].keys()
    # print(keys
    #       )
    with open('data/fresh_new_5.txt', 'w', newline='') as output_file_name:
        output_file_name.write(text)
        output_file_name.close()
        # writer = csv.DictWriter(output_file_name, keys)
        # writer.writeheader()
        # writer.writerows(books_data)

