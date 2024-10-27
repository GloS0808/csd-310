#!/usr/bin/env python3
"""
Seth Glover
Date: 9/23/2024
Title: Module 8.2 Assignment
Purpose: MySQL Python Script performing various updates and deletes
"""
import mysql.connector
from mysql.connector import errorcode

# Method to display films with an inner join query
def show_films(cursor, title):
    # Inner join query to get data from film, genre, and studio tables
    cursor.execute("""
        SELECT 
            film_name AS 'Name', 
            film_director AS 'Director', 
            genre_name AS 'Genre', 
            studio_name AS 'Studio Name' 
        FROM film 
        INNER JOIN genre ON film.genre_id = genre.genre_id 
        INNER JOIN studio ON film.studio_id = studio.studio_id;
    """)

    # Get the results from the cursor object
    films = cursor.fetchall()

    # Display the title
    print("\n -- {} --".format(title))

    # Iterate over the film dataset and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

# Main database connection code
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
    
    # Call the show_films method to display the films
    show_films(cursor, "DISPLAYING FILMS")

    # Insert a new record into the film table
    insert_query = """
    INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) 
    VALUES('Ad Astra', '2019', '124', 'James Gray', 
    (SELECT studio_id FROM studio WHERE studio_name = '20th Century Fox'),
    (SELECT genre_id FROM genre WHERE genre_name = 'SciFi'));
    """     
    cursor.execute(insert_query)
    db.commit()  # Make sure to commit the transaction

    # Call the show_films method to display the films after insert
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
    
    # Call the show_films method to display the films
    insert_query = """
    UPDATE film
    SET genre_id = 1
    WHERE film_name = 'Alien'
    LIMIT 1;
    """
    cursor.execute(insert_query)
    db.commit() 
    
    # Call the show_films method to display the films after update
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Delete Gladiator
    insert_query = """
    DELETE FROM film WHERE film_name = 'Gladiator' LIMIT 1;
    """
    cursor.execute(insert_query)
    db.commit()
    
    # Call the show_films method to display the films after delete
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

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
