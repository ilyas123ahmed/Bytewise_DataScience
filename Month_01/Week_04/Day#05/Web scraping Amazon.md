# Amazon Scraping

```python
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    # allowed_domains = ['amazon.com']
    start_urls = [
          'https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A3248684011&dc&ds=v1%3AI91B%2BdZTSA96JFKRasp6HXQXmnwcDXjnGP3sdGiHpdM&qid=1663938140&ref=sr_ex_n_1'
       ]

    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css('.a-size-base-plus::text').extract()
        product_price = response.css('.a-size-base-plus').css('::text').extract()
        product_imagelink = response.css('.s-height-equalized .s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

```

### Terminal Output
![image](https://user-images.githubusercontent.com/80588277/192127604-41e910ca-6af6-4bfe-a692-84adf58b8066.png)

![image](https://user-images.githubusercontent.com/80588277/192127653-18d12e39-2ca8-4b7c-a46d-119dfb9b4cab.png)

