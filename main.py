import inspect
import sys

import fire

from app.config import get_config

def scrape():
    """
    Scrape a URL and clean its content for analyzing with an LLM.
    """
    print('TODO!')

if __name__ == '__main__':
    get_config()

    # Available commands are every function defined in this particular module
    commands = [obj for i, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isfunction(obj)]

    # Fire expects a dictionary of command_name => function, so create a dict where the key is the function's name
    command_obj = {i.__name__: i for i in commands}

    # Defer command handling to Fire
    fire.Fire(command_obj)
