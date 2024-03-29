#!/usr/bin/env bash

from read_file import read_file_csv
from bd import create_connection, close, add_location


def main():
    date = read_file_csv('date/uszips.csv')

    conn = create_connection()

    for line in date[1:]:
        add_location(conn, line)
    
    close(conn)


if __name__ == '__main__':
    main()
