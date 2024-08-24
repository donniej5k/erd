import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('bookhaven.db')
cursor = conn.cursor()

# Task 1: Database Schema Design
# Creating tables for the database

# Create the Authors table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Authors (
    AuthorID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Biography TEXT
)
''')

# Create the Books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Books (
    BookID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    AuthorID INTEGER NOT NULL,
    Genre TEXT,
    Price REAL NOT NULL,
    PublishedDate DATE,
    ISBN TEXT UNIQUE NOT NULL,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
)
''')

# Create the Customers table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    PhoneNumber TEXT,
    Address TEXT
)
''')

# Create the Transactions table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Transactions (
    TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER NOT NULL,
    BookID INTEGER NOT NULL,
    TransactionDate DATE NOT NULL,
    Quantity INTEGER NOT NULL,
    TotalPrice REAL NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (BookID) REFERENCES Books(BookID)
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully.")

# Task 2: Entity-Relationship Diagram (ERD) Creation
# The ERD is typically created using visual tools, but here we describe it.

print("""
Entity-Relationship Diagram (ERD):

1. Books Table:
   - BookID (Primary Key)
   - Title
   - AuthorID (Foreign Key references Authors.AuthorID)
   - Genre
   - Price
   - PublishedDate
   - ISBN

2. Authors Table:
   - AuthorID (Primary Key)
   - FirstName
   - LastName
   - Biography

3. Customers Table:
   - CustomerID (Primary Key)
   - FirstName
   - LastName
   - Email
   - PhoneNumber
   - Address

4. Transactions Table:
   - TransactionID (Primary Key)
   - CustomerID (Foreign Key references Customers.CustomerID)
   - BookID (Foreign Key references Books.BookID)
   - TransactionDate
   - Quantity
   - TotalPrice

Relationships:
- One-to-Many: An Author can write multiple Books.
- One-to-Many: A Customer can make multiple Transactions.
- One-to-Many: A Book can be sold in multiple Transactions.
""")
