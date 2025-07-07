from dataclasses import dataclass
import os
from typing import Optional

@dataclass
class AppConfig:
    """Core application configuration"""

    APP_DATA_DIRECTORY: str = f'{os.getcwd()}/data'
    """Directory where data files will be written."""

    PAGES_REPOSITORY_FILE: str = 'pages.db'
    """File where cached pages will be stored."""

    OPENAI_BASE_URL: str = 'http://localhost:11434/v1'
    """
    Base URL for OpenAI-compatible API.

    Defaults to local Ollama endpoint.
    @see https://ollama.com/blog/openai-compatibility
    """

    OPENAI_API_KEY: Optional[str] = None

    OPENAI_MODEL: str = 'gemma3:27b'
    """
    The LLM model to use when handling anything
    """
