from pydantic import BaseModel
from datetime import date, datetime
from enum import Enum


class UserPrefix(str, Enum):
    DOCT = "DOCT"
    MADM = "MADM"
    MISS = "MISS"
    MIST = "MIST"


class AccountType(str, Enum):
    CACC = "CACC"
    CARD = "CARD"


class AccountUsage(str, Enum):
    PRIV = "PRIV"
    ORGA = "ORGA"


class BalanceType(str, Enum):
    CLBD = "CLBD"
    XPCD = "XPCD"
    VALU = "VALU"
    ITAV = "ITAV"
    PRCD = "PRCD"
    OTHR = "OTHR"


class TransactionCreditDebitIndicator(str, Enum):
    CRDT = "CRDT"
    DBIT = "DBIT"


class TransactionStatus(str, Enum):
    BOOK = "BOOK"
    PDNG = "PDNG"
    FUTR = "FUTR"
    INFO = "INFO"


class Token(BaseModel):
    access_token: str
    token_type: str


class UserIdentity(BaseModel):
    id: str
    prefix: UserPrefix
    first_name: str
    last_name: str
    date_of_birth: date


class Account(BaseModel):
    id: str
    type: AccountType
    usage: AccountUsage
    iban: str
    name: str
    currency: str


class Balance(BaseModel):
    id: str
    name: str
    amount: int
    currency: str
    type: BalanceType


class Transaction(BaseModel):
    id: str
    label: str
    amount: int
    crdt_dbit_indicator: TransactionCreditDebitIndicator
    status: TransactionStatus
    currency: str
    date_operation: datetime
    date_processed: datetime


# body_get_token...
