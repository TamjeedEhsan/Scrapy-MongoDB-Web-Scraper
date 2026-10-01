import scrapy

from book_scraper.items import BooksItem

RATING_MAP = {
            "One": 1,
            "Two": 2,
            "Three": 3,
            "Four": 4,
            "Five": 5,
    }

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        
        books = response.css("article.product_pod")

        for book in books:
            title = book.css("h3 a::text").get()
            price = book.css("p.price_color::text").get()
            if price:
                price = float(price.replace("£", ""))
            rating = book.css("p.star-rating::attr(class)").get()
            if rating:
                rating = rating.split()
                rating = rating[1]
                rating = RATING_MAP[rating]
            availability = "".join(
                book.css("p.instock.availability::text").getall()
            ).strip() or None
            url = response.urljoin(book.css("h3 a::attr(href)").get())

            yield BooksItem(
                title=title,
                price=price,
                rating=rating,
                availability=availability,
                url=url,
            )

        next_page = response.css("li.next a::attr(href)").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)