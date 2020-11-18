from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
def pong():
    return {"ping":"pong!"}

@router.get("/foo")
async def bar():
    # alguma operação assíncrona pode acontecer aqui 
    # exemplo: `notes = waiting get_all_notes()` 
    return {"foo":"bar!"}
