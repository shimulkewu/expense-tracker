import csv # For handling CSV file operations
from datetime import datetime # For getting the current date and time
from utils import save_expense, read_expenses, calculate_total, filter_by_category, is_valid_amount
import pandas as pd
df = pd.read_csv("data.csv")
print(df.groupby("category")["amount"].sum())
FILE = "data.csv" # This is the file where expenses will be stored. Each expense will be saved as a new row in this CSV file.

def add_expense():# This function allows the user to add a new expense. It prompts the user for the expense name, amount, and category. It then gets the current date and saves all this information as a new row in the CSV file.
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    date = datetime.now().strftime("%Y-%m-%d") # This line gets the current date and formats it as a string in the format "YYYY-MM-DD".

    with open(FILE, "a", newline="") as file: # This line opens the CSV file in append mode ("a"), which means that new expenses will be added to the end of the file without overwriting existing data. The "newline="" argument is used to ensure that new lines are handled correctly in the CSV file.
        writer = csv.writer(file) # This creates a CSV writer object that will be used to write data to the file.
        writer.writerow([date, name, category, amount]) # This line writes a new row to the CSV file with the date, name, category, and amount of the expense. The data is passed as a list to the writerow() method, which will format it correctly for the CSV file.

    print("Expense added!")


def view_expenses(): # This function allows the user to view all the expenses that have been added. It reads the CSV file and prints each expense in a formatted manner. If the file does not exist, it catches the FileNotFoundError and informs the user that no data is found.
    try:
        with open(FILE, "r") as file: # This line opens the CSV file in read mode ("r"). If the file does not exist, it will raise a FileNotFoundError, which is handled in the except block.
            reader = csv.reader(file)
            print("\nDate | Name | Category | Amount")
            print("\n\t-" * 40) # This line prints a separator line for better readability of the output.
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No data found.")


def total_expense(): # This function calculates and displays the total amount of expenses. It reads the CSV file, sums up the amounts from each row, and prints the total. If the file does not exist or is empty, it catches any exceptions and informs the user that there is no data.
    total = 0
    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[3]) # This line adds the amount from each row (which is in the 4th column, index 3) to the total variable. The amount is converted to a float before adding it to ensure that the total is calculated correctly.
        print(f"\nTotal Expense: {total} TK")
    except:
        print("No data.")


def main(): # This is the main function that runs the expense tracker application. It displays a menu to the user and prompts them to choose an option. Based on the user's choice, it calls the appropriate function to add an expense, view expenses, calculate total expenses, or exit the application. The loop continues until the user chooses to exit.
    while True:
        print("\n==== EXPENSE TRACKER ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()