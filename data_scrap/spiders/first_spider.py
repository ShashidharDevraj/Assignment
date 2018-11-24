import scrapy

class FirstSpider(scrapy.Spider):
    name = "test1"

    def start_requests(self):
    	'''
    		Request to parse the given data from the website. 
    	'''
    	urls = ['http://www.bbc.com/']

    	for url in urls:
    		yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
    	'''
    		Parse Headline. 	
    	'''
    	headline = {}
    	headlines = response.css("a.media__link::text").extract()
    	for text in headlines:
    		text = (" ".join(text.split()))
    		scrap = {
    			"headline": text
    		}
    		yield(scrap)

