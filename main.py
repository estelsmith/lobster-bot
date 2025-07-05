import inspect
import sys

import fire
import httpx

from app.HttpxPageFetcher import HttpxPageFetcher
from app.config import load_config

async def scrape():
    """
    Scrape a URL and clean its content for analyzing with an LLM.
    """
    client = httpx.AsyncClient()
    fetcher = HttpxPageFetcher(client)
    response = await fetcher.fetch_page('https://news.ycombinator.com/')
    print(f'{response!r}')

def test():
    pass

if __name__ == '__main__':
    load_config()

    # Available commands are every function defined in this particular module
    commands = [obj for i,obj in inspect.getmembers(sys.modules[__name__]) if inspect.isfunction(obj)]

    # Fire expects a dictionary of command_name => function, so create a dict where the key is the function's name
    command_obj = {i.__name__: i for i in commands}

    # Defer command handling to Fire
    fire.Fire(command_obj)
