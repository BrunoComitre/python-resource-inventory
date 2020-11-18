from tornado.httpclient import HTTPClient, AsyncHTTPClient
from tornado import gen
from tornado.concurrent import Future


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body

#cprint(synchronous_fetch("https://www.tornadoweb.org/en/stable/guide/async.html"))


async def asynchronous_fetch(url):
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(url)
    return response.body

# print(asynchronous_fetch("https://www.tornadoweb.org/en/stable/guide/async.html"))


@gen.coroutine
def async_fetch_gen(url):
    http_client = AsyncHTTPClient()
    response = yield http_client.fetch(url)
    raise gen.Return(response.body)

# print(async_fetch_gen("https://www.tornadoweb.org/en/stable/guide/async.html"))


def async_fetch_manual(url):
    http_client = AsyncHTTPClient()
    my_future = Future()
    fetch_future = http_client.fetch(url)
    def on_fetch(f):
        my_future.set_result(f.result().body)
    fetch_future.add_done_callback(on_fetch)
    return my_future

print(async_fetch_manual("https://www.tornadoweb.org/en/stable/guide/async.html"))
