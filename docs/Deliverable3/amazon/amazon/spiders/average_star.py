import scrapy

class AverageScrapy(scrapy.Spider):
    name = "average_star"
    def start_requests(self):
        url = 'https://www.amazon.com/Mosiso-Plastic-Previous-Generation-MacBook/product-reviews/B00IMQFWSO/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'AverageStar.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)