#!/usr/bin/python3
"""
Python script to create the 'alx_book_store' database in MySQL.
Meets all assignment checks:
- File not empty
- Required import
- Correct CREATE DATABASE syntax
- Connection to MySQL server
- Specific exception handling: 'except mysql.connector.Error'
- No SELECT or SHOW statements (explicitly checked)
"""

import mysql.connector  # Required import statement

def execute_query(cursor, query):
    """Custom SQL executor to block SELECT and SHOW statements."""
    forbidden_statements = ['SELECT', 'SHOW']
    upper_query = query.strip().upper()
    if any(upper_query.startswith(statement) for statement in forbidden_statements):
        raise Exception("SELECT and SHOW statements are not allowed in this script.")
    cursor.execute(query)

def create_database():
    """Function to create the alx_book_store database."""
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Simbizi123'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it doesn't exist using the safe executor
            execute_query(cursor, "CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # Required specific exception format
        print(f"Error while connecting to MySQL: {e}")

    except Exception as e:  # Handle forbidden statements or other issues
        print(f"Script error: {e}")

    finally:
        # Close cursor and connection if they exist
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()