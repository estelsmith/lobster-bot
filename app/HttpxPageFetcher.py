import httpx
from typing import Optional
from abc import ABC, abstractmethod

class PageFetcher(ABC):
    """Abstract base class for fetching web pages."""

    @abstractmethod
    async def fetch_page(self, url: str) -> Optional[str]:
        pass

class HttpxPageFetcher(PageFetcher):
    """
    Fetch web pages using httpx.

    @see https://www.python-httpx.org/
    """

    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    async def fetch_page(self, url: str) -> Optional[str]:
        try:
            return (await self.client.get(url)).raise_for_status().text
        except httpx.HTTPError as e:
            return None
