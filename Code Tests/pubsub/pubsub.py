import aioredis
from fastapi import HTTPException

from app.config.factory import cfg

env = cfg()


class AsyncPubSub:
    def __init__(self):
        self.channel = None
        self.pub = None
        self.sub = None
    
    async def create_connection(self):
        try:
            self.pub = await aioredis.create_redis(f'redis://{env.REDIS_URI}')
            self.sub = await aioredis.create_redis(f'redis://{env.REDIS_URI}')
        except Exception as e:
            print(f'error to connect to redis {str(e)}')
    
    async def subscribe(self, channel: str):
        res = await self.sub.subscribe(channel)
        self.channel = res[0]

    async def publish(self, channel: str, content: str):
        res = await self.pub.publish_json(channel, content)
        # assert res == 1
    
    async def read_messages(self):
        while await self.channel.wait_message():
            try:
                msg = await self.channel.get_json()
                if msg == 'done':
                    print('apk install done')
                    break
                elif msg == 'error':
                    print('error to install apk')
                    raise HTTPException(400, 'error to install apk')
                elif msg == 'in_progress':
                    print('apk install in progress')
            except HTTPException:
                raise
            except Exception as e:
                print(f'ERROR TO READ MESSAGES: {str(e)}')
                raise HTTPException(500, 'error to read pub/sub messages')
            finally:
                self.pub.close()
                self.sub.close()
                print('close pub/sub connections')
    
    async def close(self):
        await self.pub.wait_closed()
        await self.sub.wait_closed()

broadcast = AsyncPubSub()
