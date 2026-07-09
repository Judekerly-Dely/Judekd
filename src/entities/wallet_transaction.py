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

class TransactionType(Enum):
    """the different type of transactions in the system"""

    PLACEMENT = "placement"
    PAYMENT = "payment"
    WITHDRAW =  "withdaw"
    TRANSFER = "transfer"
    REFUNDED = "refunded"

class Wallet:

    """
    ============================================
    This class represents the wallet of an user. 
    ============================================
    """

    def __init__(self, id_user: int, id_wallet: int, balance: int = 0, realized_at: datetime = field(default_factory=_now), update_at: datetime = field(default_factory=_now), status_wallet: WalletStatus = field(default_factory = WalletStatus.ACTIVE)):
        self.id_user = id_user
        self.id_wallet = id_wallet
        self.balance = balance
        self.realized_at = realized_at
        self.update_at = update_at
        self.status_wallet = status_wallet
        
    def __post_init__(self):
        if self.balance < 0:
            return False
        return True

    def activate(self) -> bool:
        if self.status_wallet == WalletStatus.ACTIVE or self.status_wallet == WalletStatus.BLOCKED:
            return False
        self.realized_at = _now()
        self.status_wallet = WalletStatus.ACTIVE
        return True

    def income(self, amount: int) -> bool:
        if not self.validate(amount):
            return False
        self.balance += amount
        self.update_at = _now()
        return True

    def outcome(self, amount : int) -> bool:
        if not self.validate(amount):
            return False
        self.balance -= amount
        self.update_at = _now()
        return True
    
    def suspended(self) -> bool:
        return self.status_wallet == WalletStatus.SUSPENDED
    
    def validate(amount) -> bool:
        if amount < 5:
            return False
        else:
            return True

    def checkdelete(self) -> bool:
        return self.status_wallet == WalletStatus.DELETED

    def checkblock(self) -> bool:
        return self.status_wallet == WalletStatus.BLOCKED
    
 
class Transaction():

    """
    ===================================================
    This class represents the transactions of a wallet
    ===================================================
    """

    def __init__(self, transactiontype: TransactionType, source_id: int, destination_id: int, id_transaction: int, status_transaction: TransactionStatus = field(default_factory = TransactionStatus.PROCESSING), amount: int = field()):
        self.transactiontype = transactiontype  
        self.source_id = source_id 
        self.destination_id = destination_id 
        self.id_transaction = id_transaction
        self.status_transaction = status_transaction 
        self.amount = amount
    
    def __post_init__(self) -> None:
        if self.amount < 5:
            raise Exception("unvalid amount")
        if not self.source_id or not self.destination_id:
            raise Exception (
                "the wallets can not be empty"
            )
        self.amount = self.amount
        self.source_id = self.source_id
        self.destination_id = self.destination_id
        
    def validated(self):
        if self.status_transaction == TransactionStatus.SUCCESSFUl: 
            return False
        self.status_transaction = TransactionStatus.SUCCESSFUl
        return True

    def is_successful(self) -> bool:
        return self.status_transaction == TransactionStatus.SUCCESSFUl

    def is_unsuccessful(self)-> bool:
        return self.status_transaction == TransactionStatus.UNSUCCESSFUL

    def is_processing(self) -> bool:
        return self.status_transaction == TransactionStatus.PROCESSING

    

    
