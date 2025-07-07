import httpx

from app.ioc import Container
from app.pages import DuckDbPageRepository
from app.scraping import HttpxPageFetcher
from app.scraping.fetcher.CachedPageFetcher import CachedPageFetcher

def register_provider(container: Container):
    container.register(httpx.Client, container.share(lambda: httpx.Client()))
    container.register(HttpxPageFetcher, container.share(lambda: HttpxPageFetcher(container.get(httpx.Client))))

    container.register(CachedPageFetcher, container.share(
        lambda: CachedPageFetcher(
            container.get(DuckDbPageRepository),
            container.get(HttpxPageFetcher)
        )
    ))
