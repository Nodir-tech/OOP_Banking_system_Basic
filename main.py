# Parent class: User
# CHild class: Bank
# Hisobraqamdagi summa
# Olinayotgan summa
# Hisobraqamdan pulni yechish,Hisobraqamni to`1ldirish,Shxsiy ma`lumotlar

# Parent class

class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_info(self):
        print(">>>>>>>>>>>>>>>>>>>>")
        print("SHaxsiy ma`lumotlar")
        print(">>>>>>>>>>>>>>>>>>>>")
        print("Isim", self.name)
        print("Yosh", self.age)
        print("Jins", self.gender)


# CHild class

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Hisob raqam balansi yangilandi: $", self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("HATO! | Hisobraqamingizdagi summa: $", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Hisobraqamingizdagi summa o`zgartirildi: $", self.balance)

    def show_balance(self):
        self.show_info()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Sizning hisobraqamingizda: $", self.balance)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

Ali = Bank("Ali",20,"Erkak")
Ali.deposit(4000)
Ali.withdraw(1000)
Ali.show_balance()