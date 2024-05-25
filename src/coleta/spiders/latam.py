import scrapy


class LatamSpider(scrapy.Spider):
    name = "latam"
    start_urls = ["https://www.latamairlines.com/br/pt"]

    def parse(self, response):
        ida_hora = "span.sc-bczRLJ.llDzZl.latam-typography.latam-typography--heading-04.sc-gsnTZi.cardFlightstyle__TextHourFlight-sc__sc-1fa5kbc-18.jnFvAE.JXvbY"
        bloco = "div.bodyFlightsstyle__ListItemAvailableFlights-sc__sc-1g00tx2-5.cNdlNa"
        conteudo = "div.cardFlightstyle__WrapperCardShadow-sc__sc-1fa5kbc-0.cFjvbF"

        placeholder="Brasília, DF"