class SavingsAccount:

    # class attributes
    minbal = 5000

    def __init__(self,acno,ahname, balance = 0):
        # object attribute
        self.acno = acno
        self.ahname = ahname
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance - SavingsAccount.minbal >= amount:
            self.balance -= amount
        else:
            raise ValueError('Insufficient funds : ' + str(self.balance))

    def __str__(self):
        return f"{self.acno} - {self.ahname} - {self.balance}"

    def __gt__(self,other):
        return self.balance > other.balance


if __name__ == "__main__":
    a1 = SavingsAccount(1,"Bill",10000)
    a2 = SavingsAccount(2,"Steve")

    a1.deposit(5000)
    a2.deposit(10000)

    # a1.withdraw(5000)
    # a1.withdraw(20000)
    print(a1 > a2)
    print(a1)
