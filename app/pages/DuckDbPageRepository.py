from typing import Optional

from duckdb.duckdb import DuckDBPyConnection

from app.pages import Page, PageRepository

class DuckDbPageRepository(PageRepository):
    _table: str = 'pages'

    def __init__(self, connection: DuckDBPyConnection):
        self._connection = connection
        self._set_up()

    def _set_up(self):
        """Set up database tables necessary to work the repository."""
        self._connection.sql(
            f"""
            CREATE TABLE IF NOT EXISTS {self._table} (
                url TEXT PRIMARY KEY,
                content TEXT,
                created_at DATETIME,
                updated_at DATETIME
            )
            """
        )

    def get_page(self, url: str) -> Optional[Page]:
        self._connection.execute(
            f"""
            SELECT * FROM {self._table} WHERE url=?
            """,
            [url]
        )
        result = self._connection.fetchone()
        return None if not result else Page(*result)

    def save_page(self, page: Page):
        # During ON CONFLICT, re-defined created_at to be the same value it was before. Otherwise it will assume the value
        # of NOW() since that was its last defined value in the statement.
        self._connection.execute(
            f"""
            INSERT INTO {self._table}
            (url, content, created_at)
            VALUES(?, ?, NOW())
            ON CONFLICT DO UPDATE SET created_at=created_at, updated_at=NOW()
            """,
            [
                page.url,
                page.content,
            ]
        )
        pass

    def remove_page(self, url: str):
        self._connection.execute(f'DELETE FROM {self._table} WHERE url=?', [url])
