from fastapi import APIRouter, HTTPException, Path, Body, Depends, Query

from starlette.exceptions import HTTPException
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

from typing import List, Optional

from app.payloads import notes
from app.models.notes import NoteSchema, fix_item_id
from ....db.mongodb import AsyncIOMotorClient, get_database


router = APIRouter()


@router.post("/", response_model=NoteSchema, status_code=HTTP_201_CREATED)
async def create_note(*, db:AsyncIOMotorClient = Depends(get_database), payload:NoteSchema):
    """[summary]
    View inserts item in the note list.

    [description]
    Endpoint to retrieve an specific item.
    """
    the_item = await notes.post(db, payload)
    return fix_item_id(the_item)

@router.get("/{id_}/")
async def read_note(id_: str, db:AsyncIOMotorClient = Depends(get_database)):
    """[summary]
    Get one item by ID.

    [description]
    Endpoint to retrieve an specific item.
    """    
    note = await notes.get(id_, db)

    if note:
        return fix_item_id(note)
    else:
        raise HTTPException(status_code=404, detail="Note not found")

@router.get("/")
async def read_all_notes(limit: int = 0, skip: int = 0, db: AsyncIOMotorClient = Depends(get_database)):
    """[summary]
    Get all item by ID.

    [description]
    Endpoint to retrieve an specific item.
    """  
    if limit > 0:
        note = limit
    else:
        note = await notes.get_all(db)

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")    

    return list(map(fix_item_id, note))

@router.put("/{id_}/")
async def update_item(id_: str, payload: NoteSchema, db:AsyncIOMotorClient = Depends(get_database)):
    """[summary]
    Get alter item by ID.

    [description]
    Endpoint to retrieve an specific item.
    """  
    note = await notes.put(id_, payload, db)

    if note:
        return fix_item_id(note)
    else:
        raise HTTPException(status_code=404, detail="Note not found")

@router.delete("/{id_}/", response_model=NoteSchema)
async def delete_note(id_: str, db:AsyncIOMotorClient = Depends(get_database)):
    """[summary]
    Get delete item by ID.

    [description]
    Endpoint to retrieve an specific item.
    """  
    note = await notes.get(id_, db)

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    await notes.delete(id_, db)

    return note
