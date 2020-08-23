from aioredis.pubsub import Receiver
from aioredis.abc import AbcChannel


mpsc = Receiver(loop=loop)

async def reader(mpsc):
    async for channel, msg in mpsc.iter():
        assert isinstance(channel, AbcChannel)
        print("Got {!r} in channel {!r}".format(msg, channel))


asyncio.ensure_future(reader(mpsc))
await redis.subscribe(mpsc.channel('channel:1'),
                      mpsc.channel('channel:3'),
                      mpsc.channel('channel:5'))
await redis.psubscribe(mpsc.pattern('hello'))
# publishing 'Hello world' into 'hello-channel'
# will print this message:

# when all is done:
await redis.unsubscribe('channel:1', 'channel:3', 'channel:5')
await redis.punsubscribe('hello')
mpsc.stop()
# any message received after stop() will be ignored.
