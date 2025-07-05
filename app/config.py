import functools

from dotenv import load_dotenv

@functools.cache
def load_config():
    """
    Loads the application configuration a single time.
    """
    load_dotenv()
