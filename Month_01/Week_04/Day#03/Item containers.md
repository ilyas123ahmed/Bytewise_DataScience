#   Items Container

- Items are containers used to store data.
- These are temporary locations.

### quotes_spider.py
```python
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
```

### items.py
```python
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()
   

```

### Terminal Output 
![image](https://user-images.githubusercontent.com/80588277/192129428-dbb00a4e-1a0d-4cbc-956a-2c10d3f057df.png)
