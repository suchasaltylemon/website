from . import urls
from . import handler

import threading
import socket
import http
import urllib.parse as parser


BACKLOG = (-1)
BUFFER = 8124


class Server:
    def __init__(self):
        self.info = (socket.gethostbyname(socket.gethostname()), 80) # Ip, port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.urls = urls.UrlHandler({
            "/": "views/index"
        })
        self.socket.bind(self.info)


    def run(self):
        self.socket.listen(BACKLOG)

        threading.Thread(target=self.handle_requests).start()


    def handle_requests(self):
        while True:
            connection, info = self.socket.accept()
            raw_request = connection.recv(BUFFER).decode("utf-8")

            request = handler.Request(raw_request)
            request.parse()
            print


