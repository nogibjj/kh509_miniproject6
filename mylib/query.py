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

    grocery_data = (
        'folgers coffee',
        11,
        0.21,
        0.2254401549508692,
        4.3,
        15.2222,
        None,
        None
    )
    try:
        cursor.execute("""
            INSERT INTO GroceryDB 
            (general_name, count_products, ingred_FPro, avg_FPro_products, 
            avg_distance_root, ingred_normalization_term, 
            semantic_tree_name, semantic_tree_node)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, grocery_data)
        conn.commit()
        print("Row inserted successfully.")

    except sqlite3.Error as e:
        print("Error:", e)
        conn.rollback()

    finally:
        conn.close()

