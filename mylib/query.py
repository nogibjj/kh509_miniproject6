"""Query the database"""

import sqlite3
from prettytable import PrettyTable


def head_query():
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB LIMIT 5")
    rows = cursor.fetchall()
    conn.close()

    table = PrettyTable()
    table.field_names = [description[0] for description in cursor.description]
    for row in rows:
        table.add_row(row)

    print("Top 5 rows of the GroceryDB table:")
    print(table)
    return "Success"

def insert_query():
    """Query the Database to add a row with Electricity information."""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()

    # Sample data for insertion, replace these values with actual data
    grocery_data = (1, 'Item Name', 'Category', 10.99, 'Brand')
    try:
        cursor.execute("""
            INSERT INTO TableName (id, item_name, category, price, brand)
            VALUES (?, ?, ?, ?, ?)
        """, grocery_data)
        conn.commit()
        print("Row inserted successfully.")

    except sqlite3.Error as e:
        print("Error:", e)
        conn.rollback()

    finally:
        conn.close()

