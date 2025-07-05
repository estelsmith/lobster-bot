from dataclasses import dataclass
from typing import Optional

from app.pages import Page

@dataclass
class Link:
    text: Optional[str]
    url: str
    page_synopsis: Optional[str]
    """Brief summary of the linked page's purpose, and what type of information can be found on it."""

@dataclass
class Image:
    url: str
    size: Optional[tuple[int, int]]
    synopsis: Optional[str]

@dataclass
class ScrapedPage:
    page: Page
    links: list[Link]
    synopsis: str
    """Brief summary regarding the page's purpose, and what type of information can be found on it."""

class ProductListPage(ScrapedPage):
    pass

@dataclass
class Review:
    rating: Optional[int]
    out_of: Optional[int]
    """Rating is out of how many? 5 stars, 10, etc?"""
    title: Optional[str]
    description: Optional[str]
    by_who: Optional[str]
    created_at: Optional[str]

class ProductPage(ScrapedPage):
    breadcrumbs: list[Link]
    images: list[Image]
    tags: list[str]
    """Tags given by the seller, like "On sale", "Best seller", etc."""
    name: str
    price: str
    original_price: str
    description: str
    frequently_asked_questions: list[str]
    reviews: list[Review]
