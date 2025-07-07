from openai import OpenAI

from app.ioc import Container
from app.scraping.scraper import OpenAIScraper

def register_provider(container: Container):
    from app.config import AppConfig

    config = container.get(AppConfig)

    container.register(OpenAI, container.share(
        lambda: OpenAI(
            base_url=config.OPENAI_BASE_URL,
            api_key=config.OPENAI_API_KEY if config.OPENAI_API_KEY else '',
        )
    ))

    container.register(OpenAIScraper, container.share(lambda: OpenAIScraper(container.get(OpenAI), config.OPENAI_MODEL)))
