use scrapy command to create a boilerplate for a spider

remember to include the domain to extract the data from
eg. 
scrapy genspider listings arizonarealestate.com



after coding the spider, we can start crawling

scrapy crawl listings

then store the data
scrapy crawl listings -O listings.csv