#!/usr/bin/env python3
"""
Seth Glover
Date: 9/22/2024
Title: Module 7.2 Assignment
Purpose: MySQL Python Script performing various queries
"""
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "auth_plugin": "mysql_native_password",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    cursor = db.cursor()

    # Query to select all records from the 'studio' table
    query = "SELECT studio_id, studio_name FROM studio;" 

    cursor.execute(query)
    results = cursor.fetchall()

    # Displaying header and formatted results
    print("\n-- DISPLAYING Studio RECORDS --")
    for row in results:
        print(f"Studio ID: {row[0]}")
        print(f"Studio Name: {row[1]}\n")

    # Query to select all records from the 'studio' table
    query = "SELECT genre_id, genre_name FROM genre;" 

    cursor.execute(query)
    results = cursor.fetchall()

    # Displaying header and formatted results
    print("\n-- DISPLAYING Genre RECORDS --")
    for row in results:
        print(f"Studio ID: {row[0]}")
        print(f"Studio Name: {row[1]}\n")    

    # Query to select films under 2h from the 'film' table
    query = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120;" 

    cursor.execute(query)
    results = cursor.fetchall()

    # Displaying header and formatted results
    print("\n-- DISPLAYING Short Film RECORDS --")
    for row in results:
        print(f"Studio ID: {row[0]}")
        print(f"Studio Name: {row[1]}\n")    

    # Query to select directors from the 'film' table
    query = "SELECT film_name, film_director FROM film ORDER BY film_director;" 

    cursor.execute(query)
    results = cursor.fetchall()

    # Displaying header and formatted results
    print("\n-- DISPLAYING Director RECORDS in Order --")
    for row in results:
        print(f"Studio ID: {row[0]}")
        print(f"Studio Name: {row[1]}\n")    
        
    input("\n\nPress any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist.")
    else:
        print(err)

finally:
    if 'db' in locals() and db.is_connected():
        db.close()  # Close the connection only if it was successful
