from pydantic import BaseModel, Field


class NoteSchema(BaseModel):
    title: str = Field(..., min_length=3, mas_lenght=20)
    description: str = Field(..., min_length=3, mas_lenght=50)

class NoteDB(NoteSchema):
    id: int
