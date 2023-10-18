import requests

from urllib.parse import urljoin

# Decorator tools
from functools import wraps

# Types for function annotations
# PEP 3107 (https://www.python.org/dev/peps/pep-3107/)
from requests.models import Response
from typing import Dict


from bisellium.lib.api_clients.exceptions import APIEndpointException


def send_request(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.ConnectionError:
            raise APIEndpointException("Could not connect to the API endpoint.")
        except requests.exceptions.Timeout:
            raise APIEndpointException(
                "Request timed out while trying to connect to the API endpoint."
            )
        except requests.exceptions.RequestException:
            raise APIEndpointException(
                "Unexpected error while trying to connect to the API endpoint."
            )
        except:
            raise APIEndpointException("Unknown error.")

    return decorated_func


class BaseAPI:
    def __init__(
        self, base_url: str, status_path: str = "/status", status_isjson: bool = True
    ):
        self.base_url = base_url
        self.status_path = status_path
        self.status_isjson = status_isjson

    def __join_url(self, path: str) -> str:
        """Join path to the base URL."""
        return urljoin(self.base_url, path)

    @send_request
    def head(self, path: str, **kwargs) -> Response:
        """Send HTTP HEAD method request."""
        return requests.head(self.__join_url(path), **kwargs)

    @send_request
    def get(self, path: str, **kwargs) -> Response:
        """Send HTTP GET method request."""
        return requests.get(self.__join_url(path), **kwargs)

    @send_request
    def post(self, path: str, **kwargs) -> Response:
        """Send HTTP POST method request."""
        return requests.post(self.__join_url(path), **kwargs)

    @send_request
    def put(self, path: str, **kwargs) -> Response:
        """Send HTTP PUT method request."""
        return requests.put(self.__join_url(path), **kwargs)

    @send_request
    def patch(self, path: str, **kwargs) -> Response:
        """Send HTTP PATCH method request."""
        return requests.patch(self.__join_url(path), **kwargs)

    @send_request
    def delete(self, path: str, **kwargs) -> Response:
        """Send HTTP DELETE method request."""
        return requests.delete(self.__join_url(path), **kwargs)

    def status(self) -> Dict[bool, str]:
        """Get status of the API server."""
        status = dict(ishealthy=False, error_message=None)
        try:
            response = self.get(self.status_path, timeout=1)
            status["error_message"] = (
                response.json()["status"] if self.status_isjson else response.text
            )
        except APIEndpointException as e:
            status["error_message"] = e
        if str(status["error_message"]).lower() in ("up", "ok", "pass"):
            status["ishealthy"] = True
        return status
