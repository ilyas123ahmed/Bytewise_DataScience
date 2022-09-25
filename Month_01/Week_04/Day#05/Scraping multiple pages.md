# Scraping multiple pages in amazon
```python
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = ['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A3248684011&dc&ds=v1%3AI91B%2BdZTSA96JFKRasp6HXQXmnwcDXjnGP3sdGiHpdM&qid=1663938140&ref=sr_ex_n_1']

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css('.a-size-base-plus::text').extract()
        product_price = response.css('.a-size-base-plus').css('::text').extract()
        product_image = response.css('.s-height-equalized .s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_image'] = product_image

        yield  items
        next_page = 'https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A3248684011&dc&page='+ str(AmazonSpiderSpider.page_number) + '&qid=1663950585&ref=sr_pg_2'
        if AmazonSpiderSpider.page_number <= 100:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page,callback=self.parse)
```
