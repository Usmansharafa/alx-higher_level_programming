#!/usr/bin/python3
"""This module defines a function that safely displays all values in states
table of a database that matches the argument"""


def main():
    """This function displays all values in the states table of a database
    that matches the argument"""

    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    sql_query = """SELECT cities.id, cities.name AS city, states.name AS state
FROM cities
INNER JOIN states ON cities.state_id = states.id;
"""
    cur.execute(sql_query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
