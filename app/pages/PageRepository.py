from abc import ABC, abstractmethod
from typing import Optional

from .Page import Page

class PageRepository(ABC):
    @abstractmethod
    def get_page(self, url: str) -> Optional[Page]:
        pass

    @abstractmethod
    def save_page(self, page: Page):
        pass

    @abstractmethod
    def remove_page(self, url: str):
        pass
