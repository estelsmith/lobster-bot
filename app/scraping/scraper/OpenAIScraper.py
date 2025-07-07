from typing import Optional

from openai import OpenAI
from openai.types.chat import ParsedChatCompletion
from pydantic import BaseModel

from app.pages import Page
from app.scraping.scraper.PageScraper import PageScraper

class PageInfo(BaseModel):
    page_title: str
    name_of_product: str
    current_price: str
    sale_price: Optional[str]
    description: str
    shipping_info: str
    pass

class OpenAIScraper(PageScraper):
    def __init__(self, client: OpenAI, model: str):
        self._client = client
        self._model = model

    def scrape(self, page: Page):
        prompt = """
        Review the HTML of the page given in the `user` message. Extract information matching the given schema to the best
        of your ability.
        """

        messages = [
            {
                'role': 'system',
                'content': prompt,
            },
            {
                'role': 'user',
                'content': page.content,
            },
        ]

        completion = self._client.chat.completions.parse(
            model=self._model,
            messages=messages,
            response_format=PageInfo,
        )

        return self._get_parsed(completion)

    def _get_parsed(self, completion: ParsedChatCompletion) -> PageInfo:
        return completion.choices[0].message.parsed
