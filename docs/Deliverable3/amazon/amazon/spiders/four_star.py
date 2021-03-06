import scrapy

class AmazonScrapy(scrapy.Spider):
    name = "four_star"
    def start_requests(self):
        urls = [
        ('https://www.amazon.com/Mosiso-Plastic-Keyboard-Protector-MacBook/product-reviews/B01IGNP124/ref=cm_cr_getr_d_paging_btm_next_'+
        str(i)+'?pageNumber='+ str(i) + '&filterByStar=four_star') for i in range(1,71)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('=')[-2].split('&')[0]
        filename = 'FourStarReviews-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)