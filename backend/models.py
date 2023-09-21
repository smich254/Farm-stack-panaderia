from pydantic import BaseModel
from typing import Optional


class Task:
    id: Optional[str]
    title: str
    description: Optional[str] = None
    complete: bool = False
