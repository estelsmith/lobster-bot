from typing import Literal

from html_to_markdown import convert_to_markdown
from openai import OpenAI
from openai.types.chat import ChatCompletionSystemMessageParam, ChatCompletionUserMessageParam, ParsedChatCompletion
from pydantic import BaseModel

from app.pages import Page
from app.scraping.scraper.PageScraper import PageScraper

class Price(BaseModel):
    price_type: Literal['regular', 'sale']
    price_value: str
    """Price in dollars. Example: $9.99"""

class PageInfo(BaseModel):
    page_title: str
    name_of_product: str
    product_prices: list[Price]
    """A list of all product prices shown on the page."""
    product_description: str
    """Product description, or any information about the product itself."""
    frequently_asked_questions: list[str]
    """A list of frequently asked questions regarding the product."""
    shipping_information: str
    """Any shipping information provided for the product. Like is there weight range, how is it shipped, etc?"""
    buyer_review: list[str]
    """A list of reviews left by other buyers of the product."""
    pass

class OpenAIScraper(PageScraper):
    def __init__(self, client: OpenAI, model: str):
        self._client = client
        self._model = model

    def scrape(self, page: Page):
        # prompt = """
        # Review the HTML of the page given in the `user` message. Extract information matching the given schema to the best
        # of your ability.
        #
        # Only extract information that is readily available from the HTML. Do not come up with information in order to match
        # the schema.
        # """

        prompt = """
        You will be given an HTML page in the next message. Create and return a CSS selector that, when executed,
        will find the price of the main product on that page.
        
        Do not offer any explanation about the CSS selector. Simply return the CSS selector.
        """

        content = page.content
        # content = convert_to_markdown(content)
        print(f'content:\n{content}')
        print(f'\n\nlen: {len(content) / 1024} kB')
        print('\n\n--- --- ---\n\n')
        print(f'prompt:\n{prompt}')
        print('\n\n--- --- ---\n\n')

        messages = [
            ChatCompletionSystemMessageParam(content=prompt, role='system'),
            ChatCompletionUserMessageParam(content=content, role='user'),
        ]

        completion = self._client.chat.completions.create(
            model=self._model,
            messages=messages,
            # response_format=PageInfo,
        )

        return completion.choices[0].message.content
        # return self._get_parsed(completion)

    def _get_parsed(self, completion: ParsedChatCompletion) -> PageInfo:
        return completion.choices[0].message.parsed
