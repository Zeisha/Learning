import os.path as record
import random
class Bank:
    def __init__(self, accountnumber):
        if record.exists(f"{accountnumber}.txt"):
            # read data to variables from record
            with open(f"{accountnumber}.txt", "r") as reader:
               values = reader.readlines()
            self.firstname , self.lastname = values[0].split(" ")
            self.accountnumber = accountnumber
            self.balance = 0.0
            self.transaction = []

        else:
            #put values to record from user input
            self.firstname = input("Please enter first name: ")
            self.lastname =  input("Please enter Last name: ")
            self.accountnumber = random.random()
            self.balance = 0.0
            self.transaction = []
            with open(f"{self.accountnumber}.txt", "w") as writer:
                writer.write(self.firstname)
                writer.write(self.lastname)
                writer.write(f"\n{self.accountnumber}")
                print("Your AccountNumber is:" + str(self.accountnumber))
                writer.write(f"\n{self.balance}")


    def deposit(self, amount):
        print(f"Adding money {amount} to  existing balance {self.balance}")
        self.balance += amount
        with open(f"{self.accountnumber}.txt", "r+") as  depositentry:
            f1 = depositentry.readlines()
            f1[2] = str(self.balance)
        #with open(f"{self.accountnumber}.txt", "w") as writer:
            depositentry.writelines(f1)

        self.transaction.append(amount)

    def withdraw(self, amount):
        if amount >= self.balance :
            print(f"Removing money {amount} from current balance {self.balance}")
            self.balance = self.balance - amount
            with open(f"{self.accountnumber}.txt", "r+") as  withdrawentry:
                f1 = withdrawentry.readlines()
                f1[2] = str(self.balance)
            #with open(f"{self.accountnumber}.txt", "w") as writer:
                withdrawentry.writelines(f1)
            self.transaction.append(-amount)
        else:
            print("You do not have sufficient balance to withdraw")

    def recent_transaction(self):
        print(f"Current Balance is {self.balance}")
        print("Recent 2 transactions are ")
        self.transaction.reverse()
        for tran in self.transaction:
          print(tran)


if __name__ == "__main__":

    b = Bank("Memo1006885")
    b.deposit(100)
    b.withdraw(200)
    b2 = Bank("German104")
    b2.deposit(40000)
    b2.withdraw(10000)

