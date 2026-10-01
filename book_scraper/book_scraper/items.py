# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import dataclass


@dataclass
class BooksItem:
    title: str | None = None
    price: float| None = None
    rating: int | None = None
    availability: str | None = None
    url: str | None = None
