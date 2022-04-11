import scrapy
class Quiz(scrapy.Spider):
    name='quiz1'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        for div in response.css('.quote'):
            tags = div.css('.tag::text').getall()
            tags = ' , '.join(tags)
            yield {
                'Quote': div.css('.text::text').get(),
                'Author': div.css('.author::text').get(),
                'Tags' : tags
            }


