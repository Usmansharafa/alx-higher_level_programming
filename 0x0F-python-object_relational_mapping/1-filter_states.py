#!/usr/bin/python3
"""This module defines a function that lists all states with a name
starting with N in a database"""


def main():
    """This function lists all states with a name starting with N in a
    database"""

    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == "N":
            print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
