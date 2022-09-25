# Login Form

```python
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotetutorialItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/login'
    ]
    def parse(self, response):
        token = response.css('form input::attr(values)').extract()
        return FormRequest.from_response(response,formdata={
            'csrf_token' : token,
            'username' : 'example@gmail.com',
            'password' : '1234'
        }, callback = self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
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
    ```        

### LOGIN FORM AUTOMATICALLY GENERATED
![image](https://user-images.githubusercontent.com/80588277/192127313-62df0ff9-9041-4ae2-9297-d2b7847ad417.png)

### INSPECTION LOGIN FORM
![image](https://user-images.githubusercontent.com/80588277/192127371-2ae013e2-1df0-49ac-8324-f39f0281a3fb.png)


![image](https://user-images.githubusercontent.com/80588277/192127401-e31e4b32-73db-45f7-8964-1e640b6346b5.png)




