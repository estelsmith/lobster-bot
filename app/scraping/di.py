from app.ioc import Container
import app.scraping.fetcher.di
import app.scraping.scraper.di

def register_provider(container: Container):
    app.scraping.fetcher.di.register_provider(container)
    app.scraping.scraper.di.register_provider(container)
