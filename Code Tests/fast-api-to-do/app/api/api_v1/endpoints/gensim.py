from fastapi import APIRouter, HTTPException, Path, Body, Depends, Query

from starlette.exceptions import HTTPException
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

# from typing import List, Optional

# from app.payloads import notes
# from app.models.notes import NoteSchema, fix_item_id
# from ....db.mongodb import AsyncIOMotorClient, get_database
import gensim
import pprint

router = APIRouter()

document = """ Shall I compare thee to a summer’s day? Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May, And summer’s lease hath all too short a date:
Sometime too hot the eye of heaven shines, And often is his gold complexion dimmed,
And every fair from fair sometime declines, By chance, or nature’s changing course untrimmed:
But thy eternal summer shall not fade, Nor lose possession of that fair thou ow’st,
Nor shall death brag thou wand’rest in his shade, When in eternal lines to time thou grow’st,
So long as men can breathe or eyes can see, So long lives this, and this gives life to thee. """

text_corpus = [
    "Human machine interface for lab abc computer applications",
    "A survey of user opinion of computer system response time",
    "The EPS user interface management system",
    "System and human system engineering testing of EPS",
    "Relation of user perceived response time to error measurement",
    "The generation of random binary unordered trees",
    "The intersection graph of paths in trees",
    "Graph minors IV Widths of trees and well quasi ordering",
    "Graph minors A survey",
]

stoplist = set('for a of the and to in or a'.split(' '))

texts =  [[word for word in document.lower().split() if word not in stoplist]
for document in text_corpus]

# count word frequencies
from collections import defaultdict

@router.post("/text/", status_code=HTTP_201_CREATED)
async def create_note():
    """[summary]
    View inserts item in the note list.

    [description]
    Endpoint to retrieve an specific item.
    """
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] +=1

    processed_corpus = [[token for token in text if frequency[token] > 1 ]
    for text in texts]
    return processed_corpus
