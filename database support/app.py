import mysql.connector
from mysql.connector import Error

db_config = {
    "host": "localhost",  # Replace with your MySQL host address
    "user": "katie.hucker",       # Replace with your MySQL username
    "password": "mp6",   # Replace with your MySQL password
    "database": "movies"    # Replace with your MySQL database name
}

try:
    # Establish a connection to the database
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("Connected to MySQL database")

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Example query: Select all movies from the 'movies' table
        query = "SELECT * FROM movies;"
        cursor.execute(query)

        # Fetch all rows from the result set
        movies = cursor.fetchall()

        # Process and print the results
        for movie in movies:
            print(movie)

except Error as e:
    print("Error: ", e)

finally:
    # Close the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
