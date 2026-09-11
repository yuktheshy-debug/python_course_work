#hiding the complexity

from abc import ABC,abstractmethod

class Payment(ABC):
    def source(self):
        print("Scanner/upid/mobile number")
    def amount(self):
        print("Enter the amount")
    def bank(self):
        print("Enter the Bank")
    def pin(self):
        print("Enter the pin")

    @abstractmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("Payment Success/fail")


class HDFC(Payment):
    def paymentprocess(self):
        print("Payment is done through HDFC Bank")

class ICIC(Payment):
    def paymentprocess(self):
        print("Payment is done through ICIC Bank")

class UNION(Payment):
    def paymentprocess(self):
        print("Payment is done through UNION Bank")

class AXIC(Payment):
    def paymentprocess(self):
        print("Payment is done through AXIC Bank")



lohitha = HDFC()
lohitha.source()
lohitha.amount()
lohitha.bank()
lohitha.pin()
lohitha.paymentprocess()
lohitha.paymentstatus()

yukthesh = ICIC()
yukthesh.source()
yukthesh.amount()
yukthesh.bank()
yukthesh.pin()
yukthesh.paymentprocess()
yukthesh.paymentstatus()

king = UNION()
king.source()
king.amount()
king.bank()
king.pin()
king.paymentprocess()
king.paymentstatus()

yuk = AXIC()
yuk.source()
yuk.amount()
yuk.bank()
yuk.pin()
yuk.paymentprocess()
yuk.paymentstatus()


