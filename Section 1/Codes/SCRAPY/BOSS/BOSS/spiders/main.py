import scrapy
from scrapy import Request

class ScratchQuotes(scrapy.Spider):
    name = 'boss'
    start_urls = ['https://www.hugoboss.com/home']


    def parse(self, response):
        cssSel = 'a[href="https://www.hugoboss.com/men-clothing/"] + div .col-xl-offset-1 a::attr(href)'
        print("\n\n\n\n")
        for url in response.css(cssSel).getall():
            yield Request(url, callback=self.parseProducts)

    def parseProducts(self, response):
        cssSel = '.product-tile-default__gallery a::attr(href)'
        for prodUrl in response.css(cssSel).getall():
            yield response.follow(prodUrl, callback=self.parseProduct)

        nextPageCss = '.button--pagingbar.pagingbar__next.font__nav-link::attr(href)'
        nextPageUrl = response.css(nextPageCss).get()
        if nextPageUrl:
            yield Request(nextPageUrl, callback=self.parseProducts)


    def parseProduct(self, response):
        productName = response.css('.stage__header-title::text').get().strip()
        avalColors = response.css('.swatch-list__container .swatch-list__image::attr(title)').getall()
        avalColors = ' , '.join(avalColors)
        picUrls = []
        for i in response.css('.stage__images-thumbnail-image::attr(src)').getall():
            picUrls.append(i.split('?')[0] + '?wid=768&qlt=80')
        picUrls = ' , '.join(picUrls)

        
        careIns = response.css('.care-info__text::text').getall()
        careIns = ' , '.join(careIns)

        pass















        yield {
            'Product Name': productName,
            'Colors': avalColors,
            'Pic Urls': picUrls,
            'Care Instructions' : careIns
        }
