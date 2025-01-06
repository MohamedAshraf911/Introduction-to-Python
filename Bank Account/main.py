class BankAccount:
    global current_id

    def __init__(self, name, accountType, balance=0):
        global current_id
        self.id = current_id
        self.name = name
        self.accountType = accountType
        self.balance = balance
        current_id += 1
        self.filename = str(self.id)+"_"+self.accountType+"_"+self.name+".txt"
        with open(self.filename, 'w') as file:
            file.write(f"Account created for {self.name} with balance {self.balance}\n")

    def deposit(self, amount):
        self.balance += amount
        try:
            with open(self.filename, 'a') as file:
                file.write(f"Deposited {amount}. Balance: {self.balance}\n")
        except IOError:
            print("File not found")
        except Exception as e:
            print("An error occurred: ", e)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            try:
                with open(self.filename, 'a') as file:
                    file.write(f"Withdrew {amount}. Balance: {self.balance}\n")
            except IOError:
                print("File not found")
            except Exception as e:
                print("An error occurred: ", e)
        else:
            print("Insufficient balance")

    def get_Balance(self):
        return self.balance
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_accountType(self):
        return self.accountType
    
    def get_History(self):
        try:
            with open(self.filename, 'r') as file:
                return file.read()
        except IOError:
            print("File not found")
        except Exception as e:
            print("An error occurred: ", e)
        
# Example usage
if __name__ == "__main__":
    current_id = 1
    account1 = BankAccount("Ahmed", "Savings", 1000)
    account2 = BankAccount("Hamdy", "chequing", 500)
    account3 = BankAccount("Ali", "Savings", 2000)
    
    account1.deposit(500)
    account2.withdraw(200)
    account3.withdraw(1000)
    
    print(account1.get_Balance())
    print(account2.get_Balance())
    print(account3.get_Balance())
    
    print(account1.get_id())
    print(account2.get_id())
    print(account3.get_id())
    
    print(account1.get_name())
    print(account2.get_name())
    print(account3.get_name())
    
    print(account1.get_accountType())
    print(account2.get_accountType())
    print(account3.get_accountType())
    
    print(account1.get_History())
    print(account2.get_History())
    print(account3.get_History())