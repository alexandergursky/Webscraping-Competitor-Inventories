
# ---Creating A Project---
# To begin, navigate in terminal to your chosen directory, then run
# the command 'scrapy startproject name_of_your_project_here' in the terminal
# Once a project has been created, create a .py file in the 'spiders' folder.

# ---Starting A Spider---
# To run the spider, navigate to the terminal and type 'scrapy crawl mycrawler'
# (or whatever you put for the name in the spiders class).
# To export scraped information to a JSON file type 'scrapy crawl mycrawler -o output.json' in terminal.
# To exit the Spider's shell type 'exit()' in terminal.

# ---Interacting With The Spiders---
# To interact with the spider you can run the terminal command 'scrapy shell url_goes_here.com'.
# After this has been ran you can run the command 'response' in terminal to receive the url in a callback.
# Typing 'response.css("css_object_to_call")' will return the css responce. Example would be 'response.css("h1")'.
# Typing 'response.css("css_object_to_call").get()' will respond the actual HTML code.
# Typing 'response.css("h1::text").get()' will respond with the text in header 1.
# The '.get()' method will only return one element. To aquire more use the method '.getall()'.
# Filtering on class is allowed and an example of would be 'response.css(".page-header").get()'.
# XPath can also be used in place of CSS an example of this is 'response.xpath("//a/text()").extract()'.

# ---Proxy Server Settings---
# To feed through a proxy server, uncomment the line containing the local host IPaddress,
# place the proxy IPaddress you would like to use in its place.
# Afterwards travel to '/settings.py' and uncomment the setting 'DOWNLOADER_MIDDLEWARES'
# and place the code " 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1, ".
# Next, travel to '/middlewares.py' and under the class 'name_of_your_project_hereDownloaderMiddleware',
# under the function 'process_request' add the line ' request.meta['proxy'] = "127.0.0.1" ' (change the local host IP here to the proxy server IP you would like to use as well.)

####################################################################################################

# Importing scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# Creating the main spider class
class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["toscrape.com"] # This limits the domains where the spider will travel
    start_urls = ["https://books.toscrape.com"] # This is the starting seed of the spider


    # Uncomment the line below in order to feed through a proxy server
    #PROXY_SERVER = "127.0.0.1"

    # Rules are 'guide rails' for the spider to follow
    rules = (
        Rule(LinkExtractor(allow= "catalogue/category")), # The "," at the end is to make this a tuple and not a single element
        Rule(LinkExtractor(allow= "catalogue", deny= "category"), callback= "parse_item") # Says in plain text: "Select all of the catalogue links that do not have category in them, then refer them to a function we define called 'parse_item'."
    )

    # Function for parsing the information we want
    def parse_item(self, response):
        yield {
            "title" : response.css(".product_main h1::text").get().replace("\u2019", "'"),
            "price" : response.css(".price_color::text").get().replace("\u00a3", ""),
            "availability" : response.css(".availability::text")[1].get().replace("\n","").replace(" ", "")
        }
