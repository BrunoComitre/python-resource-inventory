import time

import tornado.ioloop
import tornado.gen
import tornado.web

class Client():

    def __init__(self):
        self.queued_items = []

    @tornado.gen.coroutine
    def watch_queue(self):
        # I have no idea what I'm doing
        items = yield client.queued_items
        # go_do_some_thing_with_items(items)

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        client.queued_items.append("%f" % time.time())
        self.write("Queued a new item")

if __name__ == "__main__":

    client = Client()

    # Watch the queue for when new items show up
    client.watch_queue()

    # Create the web server 
    application = tornado.web.Application([
        (r'/', IndexHandler),
    ], debug=True)

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
