class StancerClientError(Exception):
    """Base exception"""

    pass


class AuthenticationError(StancerClientError):
    """Authentication fails."""

    pass


class APIRequestError(StancerClientError):
    """Non-auth API errors."""

    pass
