# Store data using Pipelines

scraped data -> Item containers -> pipelines -> SQL/Mongo databases

### pipelines.py
```pyhton
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from itemadapter import ItemAdapter


class QuotetutorialPipeline:
    def process_item(self, item, spider):
        print("Pipelines: "+ item['title'][5])
        return item

```
