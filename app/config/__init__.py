import functools
import os

from dotenv import dotenv_values

import app.pages.di
import app.scraping.di
from .AppConfig import AppConfig
from ..ioc import Container

@functools.cache
def get_config() -> AppConfig:
    """Loads application configuration a single time."""
    config = AppConfig(**dotenv_values())

    try:
        os.mkdir(config.APP_DATA_DIRECTORY)
    except:
        pass

    return config

@functools.cache
def get_container() -> Container:
    """Initializes the DI container and registers the application service providers."""
    container = Container()
    container.register(AppConfig, container.share(lambda: get_config()))

    app.pages.di.register_provider(container)
    app.scraping.di.register_provider(container)

    return container
