from enum import Enum


class Methods(Enum):
    GET = 10
    POST = 20
    PUT = 30


class Codes(Enum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500
