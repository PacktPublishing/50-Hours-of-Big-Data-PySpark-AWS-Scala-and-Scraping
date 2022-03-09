import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']


    def parse(self, response):

        # for quote in response.css('.text::text').getall():
        #     yield {
        #         'quotes': quote
        #     }

        for div in response.css('.quote'):
            quote = div.css('.text::text').get()
            author = div.css('.author::text').get()
            yield {
                'quote':quote.replace('“','').replace('”',''),
                'author':author
            }

        nextPageUrl = response.css('li.next a::attr(href)').get()
        print(nextPageUrl)

        if nextPageUrl:
            yield response.follow(nextPageUrl, callback=self.parse)





































