#Homework done by Judekerly DELY and Marvens Dave AMAZAN

from datetime import datetime, timezone
from dataclasses import field, dataclass
from enum import Enum


def _now() -> datetime:
    return datetime.now(timezone.utc)

class WalletStatus(Enum):
    """The different status of an user's Walllet"""

    ACTIVE = "active"
    SUSPENDED = "suspended"
    DELETED = "deleted"
    BLOCKED = "blocked"
    

class TransactionStatus(Enum):
    """The different status of a transaction in the system"""

    SUCCESSFUl = "successful"
    UNSUCCESSFUL = "unsuccessful"
    PROCESSING = "processing"
    REFUNDED = "refunded"


@dataclass(frozen=True)
class Wallet:

    """
    ============================================
    This class represents the wallet of an user. 
    ============================================
    """

    id_user : int
    id_wallet: int
    balance : int = 0
    realized_at: datetime = field(default_factory=_now)
    update_at: datetime = field(default_factory=_now)
    status_wallet: WalletStatus = field(default_factory = WalletStatus.ACTIVE)

    def activate(self) -> bool:
        if self.status_wallet == WalletStatus.ACTIVE or self.status_wallet == WalletStatus.BLOCKED:
            raise ValueError (
                "This wallet can not be activated"
            )
        self.realized_at = _now()
        self.status_wallet = WalletStatus.ACTIVE

    def is_suspended(self) -> bool:
        self.update_at = _now()
        return self.status_wallet == WalletStatus.SUSPENDED

    def is_deleted(self) -> bool:
        self.update_at = _now()
        return self.status_wallet == WalletStatus.DELETED

    def is_blocked(self) -> bool:
        self.update_at = _now()
        return self.status_wallet == WalletStatus.BLOCKED
    
    
@dataclass(frozen=True)
class Transaction():

    """
    ===================================================
    This class represents the transactions of a wallet
    ===================================================
    """

    id_wallet = int
    id_transaction : int
    status_transaction : TransactionStatus = field()
    amount : int
    
    def validated(self, amount : int):
        if self.status_transaction == TransactionStatus.SUCCESSFUl:
            self.status_transaction = TransactionStatus.UNSUCCESSFUL
            raise ValueError (
                "Your transaction is already validated"
            )

        if not isinstance(amount, int) or amount < 0:
            self.status_transaction = TransactionStatus.UNSUCCESSFUL
            raise ValueError (
                "Unvalid amount"
            )
        self.status_transaction = TransactionStatus.SUCCESSFUl

    def transactionSuccessful(self) -> bool:
        return self.status_transaction == TransactionStatus.SUCCESSFUl

    def transactionUnsuccessful(self)-> bool:
        return self.status_transaction == TransactionStatus.UNSUCCESSFUL

    def transactionProcessing(self) -> bool:
        return self.status_transaction == TransactionStatus.PROCESSING

    def transactionRefunded(self) -> bool:
        return self.status_transaction == TransactionStatus.REFUNDED

    
