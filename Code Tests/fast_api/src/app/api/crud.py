from app.api.schemas.notes import  NoteSchema
from app.api.models.notes import notes, database


##################################### POST #####################################

async def post(payload: NoteSchema):
    query = notes.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)

##################################### GET ######################################

async def get(id: int):
    query = notes.select().where(id == notes.c.id)
    return await database.fetch_one(query=query)

################################### GET ALL ####################################

async def get_all():
    query = notes.select()
    return await database.fetch_all(query=query)

##################################### PUT ######################################

async def put(id: int, payload: NoteSchema):
    query = (
        notes
        .update()
        .where(id == notes.c.id)
        .values(title=payload.title, description=payload.description)
        .returning(notes.c.id)
    )
    return await database.execute(query=query)

#################################### DELETE ####################################

async def delete(id: int):
    query = notes.delete().where(id == notes.c.id)
    return await database.execute(query=query)
