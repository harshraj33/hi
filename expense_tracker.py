import csv
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.con = True

    def run(self):
        while self.con:
            try:
                user_input = int(input('''\nEnter 1 to add
Enter 2 to view
Enter 3 to delete
Enter 4 to Exit\n'''))

                if user_input == 1:
                    self.add_expense()
                elif user_input == 2:
                    self.view_expenses()
                elif user_input == 3:
                    self.delete_expense()
                elif user_input == 4:
                    self.con = False
                else:
                    print("Wrong input. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        print("Program exited.")

    def add_expense(self):
        description = input("Enter description of the expense (e.g., petrol, pen, CD): ")
        try:
            amount = float(input("Enter expense amount: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            return

        category = input("Enter category of expense: ")
        date = input("Enter date in (dd-mm-yyyy) format or leave blank for today's date: ")

        if not date:
            date = datetime.today().strftime('%Y-%m-%d')

        with open('expense.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([description, amount, category, date])

        print('Expense added successfully!')

    def view_expenses(self):
        try:
            with open('expense.csv', 'r') as file:
                reader = csv.reader(file)
                print("\nExpenses:")
                print("Description\tAmount\tCategory\tDate")
                print("-" * 50)

                for row in reader:
                    if row:
                        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")

        except FileNotFoundError:
            print("No expenses recorded yet.")

    def delete_expense(self):
        try:
            with open('expense.csv', 'r') as file:
                reader = csv.reader(file)
                expenses = list(reader)

                if not expenses:
                    print("No expenses recorded yet.")
                    return

                print("\nCurrent Expenses:")
                print("Index\tDescription\tAmount\tCategory\tDate")
                print("-" * 50)


                for index, row in enumerate(expenses):
                    if row:
                        print(f"{index}\t{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}")


                delete_index = int(input("Enter the index of the expense you want to delete: "))

                if 0 <= delete_index < len(expenses):
                    expenses.pop(delete_index)
                    print("Expense deleted successfully!")
                else:
                    print("Invalid index.")

        except FileNotFoundError:
            print("No expenses recorded yet.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")


        with open('expense.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(expenses)

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
