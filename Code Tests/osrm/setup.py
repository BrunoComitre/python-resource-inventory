import osrm
import asyncio
from osrm import Client
from osrm import overview
from osrm import AioHTTPClient

# client = Client(host='http://brunocomitre.com')

# response = client.route(
#     coordinates=[[-74.0056, 40.6197], [-74.0034, 40.6333]],
#     overview=overview.full)

# print(response)

loop = asyncio.get_event_loop()

async def request():
    client = AioHTTPClient(host='http://localhost:5000')
    response = await client.route(
        coordinates=[[-74.0056, 40.6197], [-74.0034, 40.6333]],
        overview=overview.full)
    print(response)
    await client.close()

loop.run_until_complete(request())