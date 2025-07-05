from typing import Optional

import httpx

from .PageFetcher import PageFetcher
from ...pages import Page

class HttpxPageFetcher(PageFetcher):
    """
    Fetch web pages using httpx.

    @see https://www.python-httpx.org/
    """

    def __init__(self, client: httpx.Client):
        self._client = client

    def fetch_page(self, url: str) -> Optional[Page]:
        try:
            return Page(
                url=url,
                content=self._client.get(url).raise_for_status().text,
            )
        except httpx.HTTPError as e:
            return None
