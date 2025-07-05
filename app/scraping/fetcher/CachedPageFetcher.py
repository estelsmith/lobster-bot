from typing import Optional

from app.pages import PageRepository
from app.scraping import PageFetcher

class CachedPageFetcher(PageFetcher):
    def __init__(self, repository: PageRepository, wrapped: PageFetcher):
        self._repository = repository
        self._wrapped = wrapped
        pass

    def fetch_page(self, url: str) -> Optional[str]:
        page = self._repository.get_page(url)
        if not page:
            page = self._wrapped.fetch_page(url)
            self._repository.save_page(page) if page else None

        return page
