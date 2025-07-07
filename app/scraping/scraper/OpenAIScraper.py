from openai import OpenAI
from openai.types.chat import ParsedChatCompletion
from pydantic import BaseModel

from app.pages import Page
from app.scraping.scraper.PageScraper import PageScraper

class PageInfo(BaseModel):
    page_title: str
    name_of_product: str
    all_prices: list[str]
    """A list of all product prices shown on the page."""
    product_description: str
    frequently_asked_questions: list[str]
    """A list of frequently asked questions regarding the product."""
    shipping_information: str
    """Any shipping information provided for the product."""
    reviews: list[str]
    """A list of reviews left by users, if any."""
    pass

class OpenAIScraper(PageScraper):
    def __init__(self, client: OpenAI, model: str):
        self._client = client
        self._model = model

    def scrape(self, page: Page):
        prompt = """
        Review the HTML of the page given in the `user` message. Extract information matching the given schema to the best
        of your ability.
        
        Only extract information that is readily available from the HTML. Do not come up with information in order to match
        the schema.
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
