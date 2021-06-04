import scrapy

class IntroSpider(scrapy.Spider):
    name = "introduccion_spider_fybeca"

    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self,response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )
        precio = response.xpath(
            '//*[@id="container-result"]/div/ul/li[16]/div/div[1]/div/div[2]'
        )
        
        print(precio)



