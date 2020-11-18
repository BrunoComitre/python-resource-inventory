from app.api import crud
from app.api.schemas.notes import NoteDB, NoteSchema
from typing import List
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()

##################################### POST #####################################

@router.post("/", response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema):
    note_id = await crud.post(payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object

##################################### GET ######################################

@router.get("/{id}/", response_model=NoteDB)
async def read_note(id: int = Path(..., gt=0),):
    note = await crud.get(id)

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    return note

################################### GET ALL ####################################

@router.get("/", response_model=List[NoteDB])
async def read_all_notes():
    # note = await crud.get_all()

    # if not note:
    #     raise HTTPException(status_code=404, detail="NoteS not found")
    # return note
    return await crud.get_all()

##################################### PUT ######################################

@router.put("/{id}/", response_model=NoteDB)
async def update_note(payload: NoteSchema,id: int = Path(..., gt=0),):
    note = await crud.get(id)

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note_id = await crud.put(id, payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }
    return response_object

#################################### DELETE ####################################

@router.delete("/{id}/", response_model=NoteDB)
async def delete_note(id: int = Path(..., gt=0),):
    note = await crud.get(id)

    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    await crud.delete(id)

    return note
