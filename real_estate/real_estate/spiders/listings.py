import scrapy
from real_estate.items import RealEstateItem # import items from RealEstateItem class
# now we have access to all the fields in the RealEstateItems class
# name = scrapy.Field()
# description = scrapy.Field()
# price = scrapy.Field()
# agency = scrapy.Field()

# this ListingsSpider class inherits from the scrapy.Spider class (OOP concept)
# ie. ListingsSpider has built-in functionality that is taken from the parent scrapy.Spider
# so there are functions defined in scrapy.Spider that we can also use in this class
class ListingsSpider(scrapy.Spider):
    name = "listings"
    # restrict spider to go to specific domains
    # useful when a website places links to other websites (eg. ads) 
    allowed_domains = ["arizonarealestate.com"]
    # URL that spider starts scraping from
    start_urls = [
        "https://arizonarealestate.com/maricopa",
        "https://arizonarealestate.com/goodyear",
        "https://arizonarealestate.com/tempe"
        ]

    # where the scraping logic takes place
    # where we write xpath codes
    def parse(self, response):
        gallery = response.xpath('//div[@class="si-listings-column"]') # list of div nodes
        for listing in gallery:
            # listing_details = dict() # use fields defined in items.py instead and populate those fields
            item = RealEstateItem()

            item['name'] = listing.xpath('.//div[@class="si-listing__title-main"]/text()').get()
            item['description'] = listing.xpath('.//div[@class="si-listing__title-description"]/text()').get()
            item['price'] = listing.xpath('.//div[@class="si-listing__photo-price"]/span/text()').get()
            item['agency'] = listing.xpath('.//div[@class="si-listing__footer"]/div/text()').get()

            # return data to scrapy
            # note we don't use return item, as this will return only the first listing data per page
            # return stops the function's execution after the first result is extracted
            yield item
