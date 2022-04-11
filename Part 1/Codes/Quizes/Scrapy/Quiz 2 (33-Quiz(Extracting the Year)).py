import scrapy
class Quiz(scrapy.Spider):
    name='quiz2'
    start_urls = ['https://www.imdb.com/chart/top/']

    def parse(self, response):
        for td in response.css('.titleColumn'):
            dict = {
                'Movie' : td.css('a::text').get(),
                'Year': td.css('span::text').get()
            }
            url = td.css('a::attr(href)').get()
            yield response.follow(url, callback=self.parseMovie, meta=dict)

    def parseMovie(self, response):
        duration = response.css('.subtext time::text').get().strip()
        movie = response.meta['Movie']
        year = response.meta['Year']

        yield {
            'Movie': movie,
            'Year': year,
            'Duration': duration
        }
