import inspect
import sys

import duckdb
import fire
import httpx

from app.config import get_config
from app.pages import DuckDbPageRepository
from app.scraping import HttpxPageFetcher

def scrape():
    """
    Scrape a URL and clean its content for analyzing with an LLM.
    """
    client = httpx.Client()
    fetcher = HttpxPageFetcher(client)
    response = fetcher.fetch_page('https://news.ycombinator.com/')
    print(f'{response!r}')

def test():
    config = get_config()
    connection = duckdb.connect(f'{config.APP_DATA_DIRECTORY}/{config.PAGES_REPOSITORY_FILE}')
    repository = DuckDbPageRepository(connection)

if __name__ == '__main__':
    get_config()

    # Available commands are every function defined in this particular module
    commands = [obj for i, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isfunction(obj)]

    # Fire expects a dictionary of command_name => function, so create a dict where the key is the function's name
    command_obj = {i.__name__: i for i in commands}

    # Defer command handling to Fire
    fire.Fire(command_obj)
