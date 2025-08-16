#!/usr/bin/env python3
"""
MySQLServer.py
Creates the database 'alx_book_store' if it does not already exist.
Reads MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD from environment variables.
"""
import os
import mysql.connector
from mysql.connector import Error

def main():
    host = os.environ.get("MYSQL_HOST", "localhost")
    user = os.environ.get("MYSQL_USER", "root")
    password = os.environ.get("MYSQL_PASSWORD", "")

    connection = None
    cursor = None

    try:
        # Connect to MySQL server (no database specified)
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

        # Use a cursor to execute the create-database statement
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Print clear error message if anything goes wrong
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Always close cursor and connection if opened
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if connection is not None and connection.is_connected():
            try:
                connection.close()
            except Exception:
                pass

if __name__ == "__main__":
    main()
