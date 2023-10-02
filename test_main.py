import unittest
import sqlite3
from your_module_name import head_query, insert_query  # Replace 'your_module_name' with the actual module name where your functions are defined
from prettytable import PrettyTable

class TestDatabaseFunctions(unittest.TestCase):
    def setUp(self):
        # Set up a temporary database for testing
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        # Create a test table
        self.cursor.execute('''
            CREATE TABLE GroceryDB (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                general_name TEXT,
                count_products INTEGER,
                ingred_FPro REAL,
                avg_FPro_products REAL,
                avg_distance_root REAL,
                ingred_normalization_term REAL,
                semantic_tree_name TEXT,
                semantic_tree_node TEXT
            )
        ''')
        self.conn.commit()

    def tearDown(self):
        # Close the database connection
        self.conn.close()

    def test_head_query(self):
        # Insert test data into the table
        self.cursor.executemany('''
            INSERT INTO GroceryDB 
            (general_name, count_products, ingred_FPro, avg_FPro_products, 
            avg_distance_root, ingred_normalization_term, 
            semantic_tree_name, semantic_tree_node)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', [
            ('item1', 1, 0.1, 0.2, 0.3, 0.4, 'tree1', 'node1'),
            ('item2', 2, 0.2, 0.3, 0.4, 0.5, 'tree2', 'node2'),
            ('item3', 3, 0.3, 0.4, 0.5, 0.6, 'tree3', 'node3'),
        ])
        self.conn.commit()

        # Redirect stdout to capture print output
        import sys
        captured_output = sys.stdout
        sys.stdout = self.buffer = io.StringIO()

        # Call the head_query function
        head_query()

        # Reset stdout
        sys.stdout = captured_output

        # Get the printed output
        printed_output = self.buffer.getvalue()

        # Assert the printed output contains expected content
        self.assertIn("Top 5 rows of the GroceryDB table:", printed_output)
        self.assertIn("item1", printed_output)
        self.assertIn("item2", printed_output)
        self.assertIn("item3", printed_output)

    def test_insert_query(self):
        # Call the insert_query function
        insert_query()

        # Query the database to check if the row was inserted
        self.cursor.execute("SELECT * FROM GroceryDB")
        rows = self.cursor.fetchall()

        # Assert that there is one row in the table
        self.assertEqual(len(rows), 1)

        # Assert the values of the inserted row
        inserted_row = rows[0]
        self.assertEqual(inserted_row[1], 'folgers coffee')
        self.assertEqual(inserted_row[2], 11)
        self.assertEqual(inserted_row[3], 0.21)
        self.assertEqual(inserted_row[4], 0.2254401549508692)
        self.assertEqual(inserted_row[5], 4.3)
        self.assertEqual(inserted_row[6], 15.2222)
        self.assertIsNone(inserted_row[7])
        self.assertIsNone(inserted_row[8])

if __name__ == '__main__':
    unittest.main()

