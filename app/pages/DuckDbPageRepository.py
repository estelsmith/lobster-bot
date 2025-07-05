from typing import Optional

from duckdb.duckdb import DuckDBPyConnection

from app.pages import Page, PageRepository

class DuckDbPageRepository(PageRepository):
    def __init__(self, connection: DuckDBPyConnection):
        self._connection = connection
        self._set_up()

    def _set_up(self):
        """Set up database tables necessary to work the repository."""
        self._connection.sql(
            """
            CREATE TABLE IF NOT EXISTS pages (
                url TEXT,
                content TEXT,
                created_at DATETIME
            )
            """
        )

    def get_page(self, url: str) -> Optional[Page]:
        pass

    def save_page(self, page: Page):
        pass

    def remove_page(self, url: str):
        pass
