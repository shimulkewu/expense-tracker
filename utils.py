import csv

FILE = "data.csv"


# 🔹 Save expense to CSV
def save_expense(date, name, category, amount):
    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, name, category, amount])


# 🔹 Read all expenses
def read_expenses():
    data = []
    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data


# 🔹 Calculate total expense
def calculate_total(data):
    total = 0
    for row in data:
        total += float(row[3])
    return total


# 🔹 Filter by category
def filter_by_category(data, category):
    return [row for row in data if row[2].lower() == category.lower()]


# 🔹 Validate amount
def is_valid_amount(amount):
    try:
        return float(amount) > 0
    except:
        return False