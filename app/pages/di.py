import duckdb
from duckdb import DuckDBPyConnection

from app.ioc import Container
from app.pages import DuckDbPageRepository

def register_provider(container: Container):
    from app.config import AppConfig

    config = container.get(AppConfig)

    container.register('duckdb_connection_string', container.share(
        lambda: f'{config.APP_DATA_DIRECTORY}/{config.PAGES_REPOSITORY_FILE}'
    ))

    container.register(DuckDBPyConnection, container.share(
        lambda: duckdb.connect(str(container.get('duckdb_connection_string')))
    ))

    container.register(DuckDbPageRepository, container.share(
        lambda: DuckDbPageRepository(container.get(DuckDBPyConnection))
    ))
