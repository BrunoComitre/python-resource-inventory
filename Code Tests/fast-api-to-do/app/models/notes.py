from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional, Union
from enum import Enum


class OperationStatus(str, Enum):
    to_do = "A Fazer"
    doing = "Fazendo"
    done = "Feito"

class NoteSchema(BaseModel):
    title: str = Field(..., min_length=3, max_lenght=20)
    description: str = Field(..., min_length=3, max_lenght=50)
    status: Optional[OperationStatus]

def fix_item_id(item):
    if item.get("_id", False):
        item["_id"] = str(item["_id"])
        return item
    else:
        raise ValueError(
            f"No `_id` found! Unable to fix item ID for item: {item}")
