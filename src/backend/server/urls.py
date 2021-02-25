class UrlHandler:
    def __init__(self, urls):
        self.urls = {}
        for i in urls:
            self.urls[i] = "./views/{}.html".format(urls[i])

