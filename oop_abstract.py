from abc import abstractmethod, ABC


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CashPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"You've paid {amount}")


cash = CashPayment()
cash.pay(100)
