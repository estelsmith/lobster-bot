from abc import ABC, abstractmethod

from app.pages import Page

class PageScraper(ABC):
    @abstractmethod
    def scrape(self, page: Page):
        pass
