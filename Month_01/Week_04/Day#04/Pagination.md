# Pagination

```python
import scrapy
from ..items import QuotetutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    page_number = 2
    start_urls = [
        "https://quotes.toscrape.com/page/1/"
    ]
    def parse(self, response):
            items = QuotetutorialItem()
            all_div_quotes = response.css('div.quote')
            for quotes in all_div_quotes:
                title = quotes.css('span.text::text').extract()
                author = quotes.css('.author::text').extract()
                tag = quotes.css(".tag::text").extract()

                items['title'] = title
                items['author'] = author
                items['tag'] = tag

                yield items

            next_page = "https://quotes.toscrape.com/page/" + str(QuotesSpider.page_number) + '/'
            print(next_page)
            if QuotesSpider.page_number < 11:
                QuotesSpider.page_number += 1
                yield response.follow(next_page, callback = self.parse)
```
### Random Output
![image](https://user-images.githubusercontent.com/80588277/192128850-f6d35ff4-a549-4cfa-bc12-38cc06f6abf9.png)

