import scrapy

class SecondSpider(scrapy.Spider):
    name = "test2"

    def start_requests(self):
    	urls = ['http://www.bbc.com/travel/story/20181122-the-nine-ghost-villages-of-northern-france']
    	for url in urls:
    		yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        Author = response.css('span.index-body::text').extract()
        Introduction = response.css('p.introduction::text').extract() 
        scrap = {
            "Author": Author[0],
            "Publish_date": Author[1],
            "Introduction": Introduction[0]
    		}
        yield(scrap)











