# Spider Crawler

```python
import scrapy
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        title = response.css('title::text').extract()
        yield {"Titletext": title}
```
### Output
![image](https://user-images.githubusercontent.com/80588277/192130331-21f12f43-f201-4085-94ab-595ec6c9216e.png)

