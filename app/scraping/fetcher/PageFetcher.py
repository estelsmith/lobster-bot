from abc import ABC, abstractmethod
from typing import Optional

from app.pages import Page

class PageFetcher(ABC):
    """Abstract base class for fetching web pages."""

    @abstractmethod
    def fetch_page(self, url: str) -> Optional[Page]:
        pass
