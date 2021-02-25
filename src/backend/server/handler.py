from .ref import Methods

import json


methods = {
    "get": Methods.GET,
    "post": Methods.POST,
    "put": Methods.PUT
}


class _BaseQuery:
    def __init__(self, query: str):
        self.raw_query = query.lower().replace("\r", '')
        self.method: Methods = None
        self.headers = {}
        self.body = ""
        self.target = None


    def parse(self):
        raise NotImplementedError("parse method not overriden")


    def _parse_to_dict(self, string):
        dictionary = {}

        string = string.replace(string.split("\n", 1)[0], '').replace("\n", '', 1)
        lines = string.split('\n')

        keys = [x.split(": ")[0] for x in lines]
        values = [x.split(": ")[1] for x in lines]

        for key, value in zip(keys, values):
            dictionary[key] = value

        return dictionary


class Request(_BaseQuery):
    def parse(self):
        lines = self.raw_query.split("\n")
        portions = self.raw_query.split("\n\n")

        start_line = lines[0]
        body = portions[1] if len(portions) > 1 else None

        start_line_split = start_line.split(' ')

        self.method = methods[start_line_split[0]]
        self.target = start_line_split[1]
        self.version = float(start_line_split[2].replace("http/", ''))

        headers = portions[0]

        self.headers = self._parse_to_dict(headers)


class Response:
    def parse(self):
        pass
