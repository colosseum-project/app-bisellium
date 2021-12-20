import requests

from functools import wraps

from urllib.parse import urljoin

from bisellium.lib.api_clients.exceptions import APIException


def requests_call(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            raise APIException("Cannot connect to API server.")
        except requests.exceptions.Timeout:
            raise APIException("API server has timed out.")
        except requests.exceptions.RequestException:
            raise APIException(
                "Unexpected error while trying to connect to API server."
            )
        return func(*args, **kwargs)

    return wrapper_func


class BaseAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def __join_url(self, path):
        return urljoin(self.base_url, path)

    @requests_call
    def head(self, path, **kwargs):
        return requests.head(self.__join_url(path), **kwargs)

    @requests_call
    def get(self, path, **kwargs):
        return requests.get(self.__join_url(path), **kwargs)

    @requests_call
    def post(self, path, **kwargs):
        return requests.post(self.__join_url(path), **kwargs)

    @requests_call
    def put(self, path, **kwargs):
        return requests.put(self.__join_url(path), **kwargs)

    @requests_call
    def patch(self, path, **kwargs):
        return requests.patch(self.__join_url(path), **kwargs)

    @requests_call
    def delete(self, path, **kwargs):
        return requests.delete(self.__join_url(path), **kwargs)
