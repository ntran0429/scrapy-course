## the scrapy shell
to examine html structure



there are different measures to prevent bots from assessing websites
1. if web server detects the client as a bot, it will serve a different html
    eg. captcha
2. return 403 (or similar code) and deny access
3. block IP address the bot is using, banning the client


use scrapy shell to test individual queries of our web scraping code
how to use scrapy shell

from CLI, scrapy shell "https://www.realtor.com"

scrapy will send a request to the website
and store the reponse in an object called Response



response.body to return html content


view(response) to open html


response.status
ideally we want to see 200


response.headers


cookies are important for accessing websites with login



request.headers


request.cookies returns a list of dicts


test the xpath queries in the scrapy shell
eg. response.xpath('//div[@class="si-listings-column"]')

make sure that all listings are in the container gallery by checking the number of listings/nodes
gallery=response.xpath('//div[@class="si-listings-column"]')
len(gallery)


good idea to select a random sample and make sure the nodes give the correct data
see if each node gives us the correct info
gallery[0].xpath('.//div[@class="si-listing__title-main"]/text()').get()