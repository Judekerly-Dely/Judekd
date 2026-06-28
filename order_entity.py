#homework done by Dorval Jane Lauramene and Gachette Mitcheyda

from enum import Enum
from datetime import datetime, timedelta

class OrderStatus(Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    EXPIRED = "EXPIRED"
    CANCELLED = "CANCELLED"


class Order:
    def __init__(self, 
                id : int, 
                products: list, 
                hours: int = 12, 
                minutes: int = 0, 
                seconds: int = 0):
        
        if len(products) == 0:
            raise Exception ("An order must contain at lesst one product.")
        
        delay = timedelta (hours = hours, minutes = minutes, seconds = seconds)

        self.id = id
        self.status = OrderStatus.PENDING
        self.creation_date = datetime.now()
        self.expiration_date = self.creation_date + delay
        self.products = products



    def check_expiration (self):
        if self.status == OrderStatus.PENDING and datetime.now() > self.expiration_date:
            self.status = OrderStatus.EXPIRED
    

