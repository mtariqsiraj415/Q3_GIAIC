# -------------------- 4:Class Variables and Class Methods ------------------- #

class Bank:
    bank_name = "UBL Bank"

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name


bank_1:Bank = Bank()
print(bank_1.bank_name)
bank_2:Bank = Bank()
print(bank_2.bank_name)
Bank.change_bank_name("HBL bank")
print(bank_1.bank_name)
print(bank_2.bank_name)

