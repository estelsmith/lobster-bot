from typing import Optional

from app.pages import PageRepository
from app.scraping import PageFetcher

class CachedPageFetcher(PageFetcher):
    def __init__(self, repository: PageRepository, wrapped: PageFetcher):
        self.repository = repository
        self.wrapped = wrapped
        pass

    def fetch_page(self, url: str) -> Optional[str]:
        page = self.repository.get_page(url)
        if not page:
            page = self.wrapped.fetch_page(url)
            self.repository.save_page(page) if page else None

        return page
