from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def pay(self, amount):
        pass

    def printOperaion(self):
        print("non abstract method called")


class creditCard(Payment):
    def pay(self, amount):
        print("Payment using Credit card")

class UPI(Payment):
    def pay(self, amount):
        print("Payment using UPI")


credit_card = creditCard("Arun")
credit_card.pay(10000)
credit_card.printOperaion()