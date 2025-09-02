from urllib.parse import urlparse


class Url:
    def __init__(self, scheme: str, netloc: str, path: str, params: str, query: str, fragment: str):
        self.scheme = scheme
        self.netloc = netloc
        self.path = path
        self.params = params
        self.query = query
        self.fragment = fragment

    def __repr__(self):
        return (
            f"Url(scheme='{self.scheme}', netloc='{self.netloc}', "
            f"path='{self.path}', params='{self.params}', "
            f"query='{self.query}', fragment='{self.fragment}')"
        )

class UrlBuilder:
    def __init__(self, raw_url: str):
        self.raw_url = raw_url
        self.parsed = urlparse(raw_url)

    def build_scheme(self):
        return self.parsed.scheme

    def build_netloc(self):
        return self.parsed.netloc

    def build_path(self):
        return self.parsed.path

    def build_params(self):
        return self.parsed.params

    def build_query(self):
        return self.parsed.query

    def build_fragment(self):
        return self.parsed.fragment

    def build(self) -> Url:
        return Url(
            scheme=self.build_scheme(),
            netloc=self.build_netloc(),
            path=self.build_path(),
            params=self.build_params(),
            query=self.build_query(),
            fragment=self.build_fragment(),
        )

class UrlDirector:
    def __init__(self, builder: UrlBuilder):
        self.builder = builder

    def construct(self) -> Url:
        return self.builder.build()

class ParseUrl:
    def __init__(self, url: str) -> None:
        self.raw_url = url
        builder = UrlBuilder(url)
        director = UrlDirector(builder)
        self.url_obj = director.construct()

    def get_url(self) -> Url:
        return self.url_obj

