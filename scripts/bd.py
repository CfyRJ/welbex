import psycopg2
import psycopg2.extras
import logging

from dotenv import load_dotenv
import os


load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')


def create_connection() -> psycopg2.extensions.connection:
    return psycopg2.connect(DATABASE_URL)


def close(conn: psycopg2.extensions.connection) -> None:
    conn.close()


def add_location(conn: psycopg2.extensions.connection, date: list):
    with conn.cursor() as cur:

        try:
            cur.execute("""
                INSERT INTO location_locations (
                        zip,
                        lat,
                        lng,
                        city,
                        state_name
                )
                VALUES (%s, %s, %s, %s, %s);
                """,
                        (*date,))
            conn.commit()
            logging.info('The addition was successful.', exc_info=True)
        except psycopg2.Error:
            logging.error(
                "An error occurred while adding to the database 'location_locations'.",
                exc_info=True)

    return None
