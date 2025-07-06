from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Page:
    url: str
    content: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
