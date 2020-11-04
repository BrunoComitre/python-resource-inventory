from fastapi import APIRouter

from .endpoints.notes import router as notes_router
from .endpoints.test_conn_doc import router as test_conn_doc_router
from .endpoints.gensim import router as gensim_router

router = APIRouter()
router.include_router(notes_router)
router.include_router(test_conn_doc_router)
router.include_router(gensim_router)
