"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query
import fire


def main(query_statement):
    # Extract
    print("Extracting data...")
    head_query()
    insert_query()

    # Transform and load
    print("Transforming data...")
    load()

    print("Querying data...")
    query(query_statement)


# Following below are sample CRUD Operations
# """SELECT general_name FROM GroceryDB WHERE count_products > 10"""
# """ DELETE FROM GroceryDB WHERE general_name LIKE 'locust bean gum' """
# """SELECT general_name FROM GroceryDB WHERE general_name LIKE '%bean%'"""

# main(sql_statement)
if __name__ == "__main__":
    fire.Fire(main)
