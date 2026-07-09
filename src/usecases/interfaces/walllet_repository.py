from abc import ABC, abstractmethod
from src.intities.wallet_transacion import Wallet, Transaction


class WalletRepository (ABC):

    @abstractmethod
    def getWallet (wallet : int) -> Wallet:
        ...

    @abstractmethod
    def saveDeposit(wallet: Wallet, tx: Transaction) -> Transaction:
        ...