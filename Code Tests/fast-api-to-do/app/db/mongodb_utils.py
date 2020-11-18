import logging

from motor.motor_asyncio import AsyncIOMotorClient
from ..core.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from .mongodb import db


async def connect_to_mongo():
    logging.info("Connecting...")
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                   maxPoolSize=MAX_CONNECTIONS_COUNT,
                                   minPoolSize=MIN_CONNECTIONS_COUNT)
    logging.info("Connected")

async def disconnect_to_mongo():
    logging.info("Disconnecting...")
    db.client.close()
    logging.info("Disconnected")


## TESTAR ##
# async def register_db(app: FastAPI):
#     @app.on_event('startup')
#     def connect_to_mongo():
#         db.client = AsyncIOMotorClient(str(MONGODB_URL),
#         maxPoolSize=MAX_CONNECTIONS_COUNT,
#         minPoolSize=MIN_CONNECTIONS_COUNT)
#         logging.info("Connected"))

#     @app.on_event('shutdown')
#     def disconnect_to_mongo():
#         logging.info("Disconnecting...")
#         db.client.close()
#         logging.info("Disconnected")
