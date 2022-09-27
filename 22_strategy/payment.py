

from abc import ABC
from enum import Enum, auto


class PayStrategy(ABC):
    def pay(self, amount): pass
    def refund(self, amount): pass


class PayByCreditCard(PayStrategy):
    def pay(self, amount):
        print(f"Pay with Credit Card method with amount {amount}")
        return True

    def refund(self, amount):
        print(f"Refund your money: {amount}")


class PayByGooglePay(PayStrategy):
    def pay(self, amount):
        print(f"Pay with Google Pay method with amount {amount}")
        return True

    def refund(self, amount):
        print(f"Refund your money: {amount}")


class PaymentMethod(Enum):
    GOOGLE_PAY = auto()
    CREDIT_CARD = auto()


class Payment():
    def __init__(self, pay_strategy=PayByCreditCard()) -> None:
        self.pay_strategy = pay_strategy

    def process_payment(self, amount):
        strategy = self.pay_strategy
        res = strategy.pay(amount)
        if res:
            print('Payment is sucessful')

    def process_refund(self, amount):
        self.pay_strategy.refund(amount)

    def set_payment_method(self, method):
        if method == PaymentMethod.CREDIT_CARD:
            self.pay_strategy = PayByCreditCard()
        elif method == PaymentMethod.GOOGLE_PAY:
            self.pay_strategy = PayByGooglePay()


if __name__ == '__main__':
    payment = Payment()
    payment.process_payment(100)
    payment.set_payment_method(PaymentMethod.GOOGLE_PAY)
    payment.process_payment(654654)
    payment.process_refund(100)
