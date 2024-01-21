
## create a new project
start by creating a virtual env with scrapy install

create a directory using scrapy commands
eg. scrapy startproject real_estate


in a project, we can write multiple spiders for different scraping logic
eg. one for property listing, one for blog posts, one for images, etc.


settings.py configure how the spiders look and behave



## robots.txt
honoring robots.txt is optional

medium discourages bots to access URLs with with the specified tokens

medium.com example

User-Agent: *
Disallow: /m/
Disallow: /me/
Disallow: /@me$
Disallow: /@me/
Disallow: /*/edit$
Disallow: /*/*/edit$
Disallow: /media/
Disallow: /p/*/share
Disallow: /r/
Disallow: /trending
Disallow: /search?q$
Disallow: /search?q=
Disallow: /*/search?q=
Disallow: /*/search/*?q=
Disallow: /*/*source=
Allow: /_/
Allow: /_/api/users/*/meta
Allow: /_/api/users/*/profile/stream
Allow: /_/api/posts/*/responses
Allow: /_/api/posts/*/responsesStream
Allow: /_/api/posts/*/related
Sitemap: https://medium.com/sitemap/sitemap.xml
User-Agent: GPTBot
Disallow: /

## settings.py

### CONCURRENT_REQUESTS
define how many requests to send to the website per second

### DEFAULT_REQUEST_HEADERS
Override the default request headers
sometimes websites expect certain headers in the request, otherwise it will block requests
we use this to set the user agent header

eg. Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36

obtain this in Inspect of a website, remember to reload/refresh
then go to robots.txt, Headers, scroll down to find User Agent


## items.py
contains items/fields we want to scrape


## middlewares.py
works on the data inside a pipeline
applies logic to process the data before going to the website
most common use case is proxies in making web requests
a proxy is for using multiple IP addresses (when scraping)



## pipelines.py
how and where to save the extracted data