import threading

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
#This initializes the bank account with a balance of 0 and creates a lock to ensure that only one thread can modify the balance at a time
  
    def deposit(self, amount):
        with self.lock:
            old_balance = self.balance
            new_balance = old_balance + amount
            self.balance = new_balance
            print(f"Deposited {amount}, new balance is {self.balance}")
#This monitors the balance and then adds the amount to the balance and then prints out the new balance

    def withdraw(self, amount):
        with self.lock:
            old_balance = self.balance
            if old_balance >= amount:
                new_balance = old_balance - amount
                self.balance = new_balance
                print(f"Withdrew {amount}, new balance is {self.balance}")
            else:
                print(f"Insufficient funds for withdrawal of {amount}, current balance is {self.balance}")
#This monitors the balance and then checks if there is enough money to withdraw the amount and if there is it will subtract the amount from the balance and print out the new balance

if __name__ == "__main__":
    bank_account = Bank()
    threads = []

    for _ in range(5):
        t1 = threading.Thread(target=bank_account.deposit, args=(200,))
        t2 = threading.Thread(target=bank_account.withdraw, args=(100,))
        t3 = threading.Thread(target=bank_account.withdraw, args=(50,))
        threads.append(t1)
        threads.append(t2)
        threads.append(t3)
        t1.start()
        t2.start()
        t3.start()
#This creates 3 threads that will deposit 200, withdraw 100, and withdraw 50 from the bank account and then starts the threads
 
    for t in threads:
        t.join()

    print(f"Final balance is {bank_account.balance}")
#This waits for all the threads to finish and then prints out the final balance of the bank account