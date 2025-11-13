import sqlite3

conn = sqlite3.connect('expenses.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Expenses
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              date TEXT,
              category TEXT,
              amount REAL,
              description TEXT)''')

conn.commit()

def add_expense():

    c.execute("INSERT INTO Expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
              (date, category, amount, description))
    
    conn.commit()
    print("Expense added successfully(:")

def view_expenses():

    c.execute("SELECT * FROM Expenses")
    expenses = c.fetchall()

    if not expenses:
        print("No expenses found.")
    else:
        for expense in expenses:
            print(expense)

def update_expense():

    c.execute("UPDATE Expenses SET date=?, category=?, amount=?, description=? WHERE id=?",
              (new_date, new_category, new_amount, new_description, id))
    conn.commit()
    print("Expense updated successfully(:")

def delete_expense():

    c.execute("DELETE FROM Expenses WHERE id=?", (id,))
    conn.commit()
    print("Expense deleted successfully(:")


while True:
    print("Choose an option:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        date = input("Enter the date: ")
        category = input("Enter the category: ")
        amount = float(input("Enter the amount: "))
        description = input("Enter the description: ")
        add_expense(date, category, amount, description)

    elif choice == '2':
        view_expenses()

    elif choice == '3':
        id = int(input("Enter the ID of the expense you want to update: "))
        new_date = input("Enter the new date: ")
        new_category = input("Enter the new category: ")
        new_amount = float(input("Enter the new amount: "))
        new_description = input("Enter the new description: ")
        update_expense(id, new_date, new_category, new_amount, new_description)

    elif choice == '4':
        id = int(input("Enter the ID of the expense you want to delete: "))
        delete_expense(id)

    elif choice == '5':
        break

conn.close()