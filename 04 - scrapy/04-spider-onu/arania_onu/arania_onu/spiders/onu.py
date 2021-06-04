import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_onu' #heredado
    allowed_domains = [#heredado
        'un.org'
    ]

    start_urls = [
        'https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    ]

    regla_uno = (
        Rule(
            LinkExtractor(),
            callback = 'parse_page' #funcion a ejecutar para parsear
        ),
        ##segundo parametro vacio
    )

    #rules = regla_uno #heredado

    segmentos_url_permitidos = (
        'funds-programmes-specialized-agencies-and-others'
    )

    regla_dos= (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos
            ), callback = 'parse_page'
        ),
        #parametro_vacio
    )
    #rules = regla_dos #heredado

    segmentos_restringidos = (
        'ar/sections',
        'zh/sections',
        'ru/sections'
    )

    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos,
                deny = segmentos_restringidos
            ), callback = 'parse_page'
        ),
        #parametero vacio
    )

    rules = regla_tres #heredado
    def parse_page(self, response):
        #lista_programas = response.xpath('//div/div/div/div/h4/text()').extract()
        lista_programas = response.css('.field-item>h4::text').extract()
        for agencia in lista_programas:
            with open('onu_agencias.txt', 'a+', encoding = 'utf-8') as archivo:
                archivo.write(agencia +'\n')