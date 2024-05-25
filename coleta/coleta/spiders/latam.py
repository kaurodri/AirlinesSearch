import scrapy


class LatamSpider(scrapy.Spider):
    name = "latam"
    start_urls = ["https://www.latamairlines.com/br/pt/oferta-voos/?origin=UDI&inbound=null&outbound=2024-06-20T12%3A00%3A00.000Z&destination=THE&adt=1&chd=0&inf=0&trip=OW&cabin=Economy&redemption=false&sort=PRICE%2Casc"]

    def parse(self, response):
        pass
