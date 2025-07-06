from dataclasses import dataclass
from datetime import datetime

@dataclass
class Page:
    url: str
    content: str
    created_at: datetime
    updated_at: datetime
