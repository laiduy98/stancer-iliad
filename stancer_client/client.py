import httpx
from typing import Optional, List
from .models import Token, UserIdentity, Account, Balance, Transaction
from .exceptions import AuthenticationError, APIRequestError
from .config import settings


class StancerClient:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.token: Optional[Token] = None
        self.client = httpx.Client(base_url=settings.api_base_url)

    def authenticate(self):
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
            "scope": "stet",
        }
        try:
            response = self.client.post("/oauth/token", data=data)
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise AuthenticationError(
                f"Authentication failed: {e.response.text}"
            ) from e
        except httpx.RequestError as e:
            raise AuthenticationError(f"Authentication request error: {str(e)}") from e

        self.token = Token(**response.json())
        self.client.headers["Authorization"] = f"Bearer {self.token.access_token}"

    def _request(self, method: str, url: str, **kwargs):
        if not self.token:
            self.authenticate()
        try:
            response = self.client.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise APIRequestError(f"API error: {e.response.text}") from e
        except httpx.RequestError as e:
            raise APIRequestError(f"Request error: {str(e)}") from e

    def get_identity(self) -> UserIdentity:
        data = self._request("GET", "/stet/identity")
        return UserIdentity(**data)

    def get_accounts(self) -> List[Account]:
        data = self._request("GET", "/stet/account")
        return [Account(**acc) for acc in data]

    def get_account(self, account_id: str) -> Account:
        data = self._request("GET", f"/stet/account/{account_id}")
        return Account(**data)

    def get_balances(self, account_id: str) -> List[Balance]:
        data = self._request("GET", f"/stet/account/{account_id}/balance")
        return [Balance(**bal) for bal in data]

    def get_transactions(
        self, account_id: str, page: int = 1, count: int = 10
    ) -> List[Transaction]:
        data = self._request(
            "GET",
            f"/stet/account/{account_id}/transaction",
            params={"page": page, "count": count},
        )
        return [Transaction(**tran) for tran in data]
