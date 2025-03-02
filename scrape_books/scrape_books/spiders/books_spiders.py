import scrapy

class BookScrapy(scrapy.Spider):
    name = "books"
    start_urls = [
        "https://books.toscrape.com",
        "https://books.toscrape.com/catalogue/page-2.html"
    ]

    def parse(self, response):
        for book in response.css("product_pod"):
            yield {
                "title": book.css("div.col-sm-6.product_main::text").get(),
                "price": book.css("p.price_color::text").get(),
                "amount_in_stock": book.css("p.instock.availability::text").get(),
                "rating": book.css("p.star-rating::attr(class)").get().split()[-1],
                "category": book.css("li:nth-child(3)::text").get(),
                "description": book.css("#product_description + p::text").get(),
                "upc": book.css("#content_inner + tr::text").get(),
            }