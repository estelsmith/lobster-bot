import duckdb
from duckdb import DuckDBPyConnection

from app.config import get_config
from app.ioc import Container
from app.pages import DuckDbPageRepository

provider = Container()
config = get_config()

provider.register('duckdb_connection_string', provider.share(lambda: f'{config.APP_DATA_DIRECTORY}/{config.PAGES_REPOSITORY_FILE}'))
provider.register(DuckDBPyConnection, provider.share(lambda: duckdb.connect(str(provider.get('duckdb_connection_string')))))
provider.register(DuckDbPageRepository, provider.share(lambda: DuckDbPageRepository(provider.get(DuckDBPyConnection))))
