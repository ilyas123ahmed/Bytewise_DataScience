# Storing Data in MYSQL Database

### pipelines.py
```pyhton
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector


class QuotetutorialPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Ilyasahmed/215',
            database='myquotes'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(
                            title text,
                            author text,
                            tag text
                            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb values (%s,%s,%s)""",
        (
            item['title'][0],
            item['author'][0],
            item['tag'][0])
        )
        self.conn.commit()
```

### quotes_spider.py

```pyhton
import scrapy
from ..items import QuotetutorialItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):

        items = QuotetutorialItem()

        all_div_quotes = response.css("div.quote")

        for quotes in all_div_quotes:
            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
            yield items

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

        title = all_div_quotes.css("span.text::text").extract()
        author= all_div_quotes.css(".author::text").extract()
        tag = all_div_quotes.css(".tag::text").extract()

        yield {
            'title': title,
            'author': author,
            'tag': tag
        }
```

### Output of database stored in MYSQL
![image](https://user-images.githubusercontent.com/80588277/192128549-8d964db0-1d0a-4d68-b6e7-6b852be875ec.png)
![image](https://user-images.githubusercontent.com/80588277/192128557-afdb88f8-e5b2-40d7-9290-5b825732afb4.png)

