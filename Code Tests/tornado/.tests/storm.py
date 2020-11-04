#!/usr/bin/env python3
#
# -*- coding: utf-8 -*-
#
# Copyright 2020 
# #
#Create First Tornado Test Web Application
#

import json
import asyncio
import unittest
# from blah import get_http_result
# from mayo import get_http_result

from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient
from tornado.testing import AsyncTestCase, gen_test
from tornado.options import define, options, parse_command_line
from tornado.web import (
    Application,
    RequestHandler,
)


define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")


class MessageBuffer(object):
    ''' '''
    def __init__(self):
        """
        """
        pass

    def get_messages_since(self, cursor):
        """
        """
        pass

    def add_message(self, message):
        """
        """
        pass


class MainHandler(RequestHandler):
    ''' '''
    def get(self):
        """
        """
        self.write("Hello, World")

class MessageNewHandler(RequestHandler):
    """Post a new message to the chat room."""
    def post(self):
        """
        """
        pass


class MessageUpdatesHandler(RequestHandler):
    """ """
    async def post(self):
        """
        """
        pass

    def on_connection_close(self):
        """
        """
        pass


def main():
    # parse_command_line()
    # app = tornado.web.Application(
    #     [
    #         (r"/", MainHandler),
    #         (r"/a/message/new", MessageNewHandler),
    #         (r"/a/message/updates", MessageUpdatesHandler),
    #     ],
    #     cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    #     template_path=os.path.join(os.path.dirname(__file__), "templates"),
    #     static_path=os.path.join(os.path.dirname(__file__), "static"),
    #     xsrf_cookies=True,
    #     debug=options.debug,
    # )
    # app.listen(options.port)
    # tornado.ioloop.IOLoop.current().start()

    return Application([
        (r"/", MainHandler),
    ])
    
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()


if __name__ == "__main__":
    main()
    
'''
class MainHandler(AsyncTestCase):

    @gen_test    
    async def get_pull_result():
        url = (
            'https://google.com'
            '/backstage/functions/mastar/package.json'
        )
        response = await AsyncHTTPClient().fetch(url,
                                                 validate_cert=False)
        data = json.loads(response.body)  
        return{
            'heey': data['name'],
        }

app = Application([
    (r"/", MainHandler),
])
app.listen(8888)
IOLoop.current().start()
'''
