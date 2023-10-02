import sqlite3

def test_connection():
    assert sqlite3.connect("GroceryDB.db")
