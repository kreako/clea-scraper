import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from cleascraper.items import RecipeItem
from markdownify import markdownify
from datetime import datetime


class CleascraperSpider(CrawlSpider):
    name = "cleascraper"
    allowed_domains = ["cleacuisine.fr"]
    start_urls = ["http://www.cleacuisine.fr/"]

    rules = (
        Rule(
            LinkExtractor(restrict_css="#main .post-link"),
            callback="parse_recipe",
            follow=True,
        ),
        Rule(
            LinkExtractor(restrict_xpaths="//span[contains(@class, 'nav-previous')]"),
            callback="parse_recipe",
            follow=True,
        ),
    )

    def _parse_start_url(self, response):
        self.logger.info("parse home page")
        self.logger.info(f"link: {response.css('#main .post-link')}")
        return response.follow_all(
            response.css("#main .post-link"), callback=self.parse_recipe
        )

    def parse_recipe(self, response):
        self.logger.info(f"parse recipe : {response.url}")

        content = response.css("#content")

        item = RecipeItem()
        item["url"] = response.url
        item["title"] = content.css(".single-title::text").get().strip()
        item["categories"] = [
            c.strip() for c in content.css(".category a::text").getall()
        ]
        item["text"] = markdownify(content.css(".content").get(), heading_style="ATX")
        item["dt"] = datetime.fromisoformat(response.css("time::attr(datetime)").get('2005-01-01T06:08:40.813432'))

        return item
