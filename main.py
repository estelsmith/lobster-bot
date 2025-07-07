import inspect
import json
import sys

import fire

from app.config import get_container
from app.scraping.fetcher import CachedPageFetcher
from app.scraping.scraper import OpenAIScraper

container = get_container()

def scrape(url: str):
    """
    Scrape a URL and clean its content for analyzing with an LLM.

    Example: python main.py scrape 'https://www.thelobsterguy.com/134to2pounlo.html'
    """

    page_fetcher = container.get(CachedPageFetcher)
    openai_scraper = container.get(OpenAIScraper)

    page = page_fetcher.fetch_page(url)
    page_info = openai_scraper.scrape(page)
    print(page_info.model_dump_json(indent=4))
    pass

if __name__ == '__main__':
    # Available commands are every function defined in this particular module
    commands = [obj for i, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isfunction(obj)]

    # Fire expects a dictionary of command_name => function, so create a dict where the key is the function's name
    command_obj = {i.__name__: i for i in commands}

    # Defer command handling to Fire
    fire.Fire(command_obj)
