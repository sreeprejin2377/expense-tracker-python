import csv
import os

FILE_NAME = "expenses.csv"


def initialize_file():
    """Create the CSV file if it doesn't already exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Date", "Category", "Description", "Amount"])


def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    description = input("Enter description: ")

    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        rows = list(csv.DictReader(file))

    new_id = len(rows) + 1

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([new_id, date, category, description, amount])

    print("Expense added successfully!")


def view_expenses():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if not expenses:
        print("No expenses found.")
        return

    print("\n--- All Expenses ---")

    for expense in expenses:
        print(
            f"ID: {expense['ID']} | "
            f"Date: {expense['Date']} | "
            f"Category: {expense['Category']} | "
            f"Description: {expense['Description']} | "
            f"Amount: ₹{expense['Amount']}"
        )


def total_expenses():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        total = sum(float(row["Amount"]) for row in reader)

    print(f"\nTotal Expenses: ₹{total:.2f}")


def search_by_category():
    category = input("Enter category to search: ").strip().lower()

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        found = False

        print("\n--- Search Results ---")

        for expense in reader:
            if expense["Category"].lower() == category:
                print(
                    f"ID: {expense['ID']} | "
                    f"Date: {expense['Date']} | "
                    f"Description: {expense['Description']} | "
                    f"Amount: ₹{expense['Amount']}"
                )
                found = True

    if not found:
        print("No expenses found for this category.")


def delete_expense():
    expense_id = input("Enter expense ID to delete: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    updated_expenses = [
        expense for expense in expenses
        if expense["ID"] != expense_id
    ]

    if len(updated_expenses) == len(expenses):
        print("Expense ID not found.")
        return

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["ID", "Date", "Category", "Description", "Amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(updated_expenses)

    print("Expense deleted successfully.")


def main():
    initialize_file()

    while True:
        print("\n==============================")
        print("       EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Search by Category")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            search_by_category()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    