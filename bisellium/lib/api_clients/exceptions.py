class APIException(Exception):
    """Exception raised when an API call fails."""

    pass


class LudusAPIException(APIException):
    """Exception raised when client cannot connect to Ludus API."""

    pass
