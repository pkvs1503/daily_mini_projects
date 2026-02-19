import os
# this module lets us allow do file operations provides file handling methods.

FILE = "records.txt"
# i am using this as my file name i stored it a variable called FILE which i need for to use in file methods.

def add_income():
    amount = float(input("Enter income amount: "))
    # i am asking user to enter the amount.
    with open(FILE, "a") as f:
        # with this above file method standard i will write the recieved input in it as follows.
        f.write(f"Income,{amount}\n")
    print("Income added successfully!\n")

def add_expense():
    amount = float(input("Enter expense amount: "))
    # same logic is applied but now asking for expense amount.
    with open(FILE, "a") as f:
        f.write(f"Expense,{amount}\n")
    print("Expense added successfully!\n")

def show_records():
    if not os.path.exists(FILE):
        print("No records found!\n")
        return
        # for showing recors first os module or os must see file exists or not, if no file then simply return. first error check.
    with open(FILE, "r") as f:
        print("\n--- All Records ---")
        print(f.read())

def calculate_balance():
    if not os.path.exists(FILE):
        print("No records found!\n")
        return
        # for calculating balacne the concept used is, i will take file line and used strip for that splitted by , and store it in type, and amount.
    income = 0
    expense = 0
    # then there is two type income and expense, so i need two variables for them.
    with open(FILE, "r") as f:
        # opening file in read mode and as f and for each line in the file ie f , the above concept logic i implemented.
        for line in f:
            type_, amount = line.strip().split(",")
            if type_ == "Income":
                income += float(amount)
            else:
                expense += float(amount)
    print(f"\nTotal Income: {income}")
    print(f"Total Expense: {expense}")
    # then this simple math logic.
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

