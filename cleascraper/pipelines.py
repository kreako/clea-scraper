# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from path import Path
from slugify import slugify


class CleascraperPipeline:
    def open_spider(self, spider):
        self.data = Path.getcwd() / "data"
        self.data.mkdir_p()

    def process_item(self, item, spider):
        dt = item["dt"]
        d = self.data / f"{dt.year}" / f"{dt.month:02d}"
        d.makedirs_p()
        fname = slugify(item["title"]) + ".md"
        with open(d / fname, 'w') as f:
            f.write("---\n")
            f.write(f"title: \"{item['title']}\"\n")
            f.write(f"date: {item['dt'].date().isoformat()}\n")
            f.write(f"url: \"{item['url']}\"\n")
            f.write("categories:\n")
            for category in item["categories"]:
                f.write(f"- {category}\n")
            f.write("---\n")
            f.write(item["text"])
        return item
