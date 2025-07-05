import fire
import httpx

from app.HttpxPageFetcher import HttpxPageFetcher

async def scrape():
    """
    Scrape a URL and clean its content for analyzing with an LLM.
    """
    client = httpx.AsyncClient()
    fetcher = HttpxPageFetcher(client)
    response = await fetcher.fetch_page('https://news.ycombinator.com/')
    print(f'{response!r}')

if __name__ == '__main__':
    fire.Fire({'scrape': scrape})
