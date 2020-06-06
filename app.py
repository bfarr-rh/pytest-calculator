# The data set used in this example is from http://archive.ics.uci.edu/ml/datasets/Wine+Quality
# P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis.
# Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.

import os
import warnings
import sys
import tornado
from io import StringIO

from tornado import websocket, web, ioloop
import json, os
import calc
from calc import calculator


class IndexHandler(web.RequestHandler):
	'''Handle requests on / '''
	def get(self):
		self.render("index.html")

class AddHandler(web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
    def get(self, *args):
        sum = calculator.add(int(args[0]),int(args[1]))
        self.write(str(sum))
        self.finish()

def make_app():
    return tornado.web.Application([
        (r"/", IndexHandler),
        (r'/add/([^/]+)?/([^/]+)?', AddHandler)
    ])



if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    for item, value in os.environ.items():
        print('{}: {}'.format(item, value))

    tornado.ioloop.IOLoop.current().start()
