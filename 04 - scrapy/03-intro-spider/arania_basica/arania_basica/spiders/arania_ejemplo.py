import scrapy

class IntroSpider(scrapy.Spider):
    name = "introduccion_spider"

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self,response):
        etiqueta_contenedora = response.css(
            'article.product_pod'
        )
        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()
        imagenes = response.xpath(
            '//a/img[@src]'
        )
        dineros = response.xpath(
            '//li/article/div/p[@class ="price_color"]'
        )
        stocks = response.xpath(
            '//li/article/div/p[@class ="instock availability"]'
        )
        estrellas = response.xpath(
            '//section/div/ol/li/article/p'
        )
        #print(imagenes)1
        print('imagenes')
        for img in imagenes:
            print (img)
        
        print('precios')
        for precio in dineros:
            print(precio)

        print('Stock')
        for stock in stocks:
            print(stock)
        print('Estrellas')
        for estrella in estrellas:
            print(estrella)

