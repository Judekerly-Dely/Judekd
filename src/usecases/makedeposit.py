from usecases.interfaces.wallet_repository import WalletRepository
from src.entities.wallet_transaction import Wallet, Transaction

class DepositInput():
    id_wallet: int
    amount: float

class DepositOutput():
    new_balance: float
    message: str
    id_transaction: int

class MakeDepositUseCase:
    def __init__(self, walletRepo: WalletRepository) -> DepositOutput:
        self.walletRepo = walletRepo

    def execute(self, Input: DepositInput, amount: float):
        wallet = self.walletRepo.get_wallet(Input.id_wallet)
        if wallet is None:
            raise ValueError("Wallet not found")
        if not wallet.is_activated():
            pass
        if not wallet.income(Input.amount):
            pass

        tx = Transaction()
        tx = self.walletRepo.saveDeposit(wallet, tx)

        return DepositOutput(id_transaction = tx.id_transaction, new_balance=wallet.balance, message="Deposit successful")