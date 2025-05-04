import datetime
expenses = []

def add_expense():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category (e.g., food, travel, misc): ")
    date = datetime.date.today().strftime("%Y-%m-%d")
    expenses.append({"amount": amount, "category": category, "date": date})
    print("✅ Expense added!\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    print("\nYour Expenses:")
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. ₹{expense['amount']} - {expense['category']} on {expense['date']}")
    print()

def delete_expense():
    view_expenses()
    if expenses:
        try:
            idx = int(input("Enter the number of the expense to delete: ")) - 1
            removed = expenses.pop(idx)
            print(f"🗑️ Removed ₹{removed['amount']} - {removed['category']}\n")
        except (IndexError, ValueError):
            print("❌ Invalid choice.\n")

def main():
    while True:
        print("📒 Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            print("Thank you for using the Expense Tracker. 👋")
            break
        else:
            print("Invalid input. Please choose between 1-4.\n")

if __name__ == "__main__":
    main()
