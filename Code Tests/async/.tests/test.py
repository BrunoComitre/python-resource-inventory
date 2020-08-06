import signal
import sys
import asyncio
import aiohttp
import json


loop = asyncio.get_event_loop()

client = aiohttp.ClientSession(loop = loop)

async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()
        
async def get_reddit_top(subreddit, client):
    data1 = await get_json(client,
    'https://reddit.com/r/' + subreddit + '/top.json?sort=now') #&limit=3')
    
    j = json.loads(data1.decode('utf-8'))
    for i in j['data']['children']:
        score = i['data']['score']
        title = i['data']['title']
        link = i['data']['url']
        test = i['data']['author']
        print(str(score) + ': ' + title + ' (' + link + ') ' + test + '')
        
    print('DONE:', subreddit + '\n')   
    
def signal_handler(signal, frame):
    loop.stop()
    client.close()
    sys.exit()
    
signal.signal(signal.SIGINT, signal_handler)

# asyncio.ensure_future(get_reddit_top('brasil', client))
# asyncio.ensure_future(get_reddit_top('InternetBrasil', client))
# asyncio.ensure_future(get_reddit_top('desabafos', client))
# loop.run_forever()


loop = asyncio.get_event_loop()
try:
    asyncio.ensure_future(get_reddit_top('brasil', client))
    asyncio.ensure_future(get_reddit_top('InternetBrasil', client))
    asyncio.ensure_future(get_reddit_top('desabafos', client))
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Fechando Loop")
    loop.close()