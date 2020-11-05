from fastapi import APIRouter


router = APIRouter()

@router.get("/ping")
def ping_pong():
    """ Retorna View de exemplo teste {"ping":"pong!"} """
    return {"ping":"pong!"}

@router.get("/foo")
async def foo_bar():
    """ Retorna View de exemplo teste {"foo":"bar!"} """
    return {"foo":"bar!"}
