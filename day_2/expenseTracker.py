import os

FILE = "records.txt"

def add_income():
    amount = float(input("Enter income amount: "))
    with open(FILE, "a") as f:
        f.write(f"Income,{amount}\n")
    print("Income added successfully!\n")

def add_expense():
    amount = float(input("Enter expense amount: "))
    with open(FILE, "a") as f:
        f.write(f"Expense,{amount}\n")
    print("Expense added successfully!\n")

def show_records():
    if not os.path.exists(FILE):
        print("No records found!\n")
        return
    with open(FILE, "r") as f:
        print("\n--- All Records ---")
        print(f.read())

def calculate_balance():
    if not os.path.exists(FILE):
        print("No records found!\n")
        return
    income = 0
    expense = 0
    with open(FILE, "r") as f:
        for line in f:
            type_, amount = line.strip().split(",")
            if type_ == "Income":
                income += float(amount)
            else:
                expense += float(amount)
    print(f"\nTotal Income: {income}")
    print(f"Total Expense: {expense}")
    print(f"Current Balance: {income - expense}\n")

def menu():
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Records")
        print("4. Calculate Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            show_records()
        elif choice == "4":
            calculate_balance()
        elif choice == "5":
            print("Thank You!")
            break
        else:
            print("Invalid choice!\n")

menu()
