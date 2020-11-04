from typing import List, Dict, Any, Optional, Union
from enum import Enum

from ..db.mongodb import AsyncIOMotorClient
from ..core.config import database_name, analyze_collection_name
from ..models.notes import NoteSchema, fix_item_id
from bson.objectid import ObjectId


async def post(conn: AsyncIOMotorClient, payload: NoteSchema) -> NoteSchema:
    comment_doc = payload.dict()
    comment_doc = await conn[database_name][analyze_collection_name].insert_one(payload.dict())
    the_doc = await conn[database_name][analyze_collection_name].find_one(
        {"_id": comment_doc.inserted_id}
        )
    return fix_item_id(the_doc)

async def get(id_: NoteSchema, conn: AsyncIOMotorClient) -> NoteSchema:
    return await conn[database_name][analyze_collection_name].find_one({"_id": ObjectId(id_)})

async def get_all(conn: AsyncIOMotorClient) -> List[NoteSchema]:
    cursor = conn[database_name][analyze_collection_name].find({}).sort('_id')
    return [document async for document in cursor]

async def put(id_: str, payload: NoteSchema, conn: AsyncIOMotorClient) -> NoteSchema:
    id_ = ObjectId(id_)
    item_op = await conn[database_name][analyze_collection_name].update_one(
        {"_id": id_}, {"$set": payload.dict()}
        )
    if item_op.modified_count:
        item = await conn[database_name][analyze_collection_name].find_one({"_id": id_})
        return fix_item_id(item)
    else:
        raise HTTPException(status_code=304)

async def delete(id_: NoteSchema, conn: AsyncIOMotorClient):
    item_op = await conn[database_name][analyze_collection_name].delete_one(
        {"_id": ObjectId(id_)}
        )
    if item_op.deleted_count:
        return {"status": f"deleted count: {item_op.deleted_count}"}
