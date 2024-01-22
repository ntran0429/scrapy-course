import scrapy
from scrapy.crawler import CrawlerProcess
import json

class PythonListingSpider(scrapy.Spider):
    name = 'pythonlistingssspider'

    start_urls = [
    "https://arizonarealestate.com/maricopa",
    "https://arizonarealestate.com/goodyear",
    "https://arizonarealestate.com/tempe"
    ]
    found_listings = []

    # where the parsing takes place
    def parse(self, response):
        # reponse is the HTML of the page defined under start_urls list
        # the reponse object contains the HTML of the page
        
        # use .xpath to extract values from XML documents
        # .xpath can also be used for HTML since the syntax are similar
        
        #populate gallery with all the div nodes pertaining to all listings
        gallery = response.xpath('//div[@class="si-listings-column"]') # list of div nodes
        for listing in gallery:
            listing_details = dict()
            
            listing_details['name'] = listing.xpath(
                # starting with a dot means start the path from the current tag
                './/div[@class="si-listing__title-main"]/text()').get()
            
            listing_details['description'] = listing.xpath(
                './/div[@class="si-listing__title-description"]/text()').get()
            
            listing_details['price'] = listing.xpath(
                # start at the parent node then move onto its child
                # to ensure uniqueness
                './/div[@class="si-listing__photo-price"]/span/text()').get()
            
            listing_details['agency'] = listing.xpath(
                './/div[@class="si-listing__footer"]/div/text()').get()
            
            # append each listing in the form of dict to the list found_listings
            self.found_listings.append(listing_details)


if __name__ == "__main__":
    process = CrawlerProcess({'LOG_LEVEL': 'ERROR'})
    process.crawl(PythonListingSpider)
    spider = next(iter(process.crawlers)).spider
    process.start()
    # convert list of dicts to a json array
    print(json.dumps(PythonListingSpider.found_listings, indent=4))