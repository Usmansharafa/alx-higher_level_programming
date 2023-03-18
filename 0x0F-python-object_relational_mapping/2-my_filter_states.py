#!/usr/bin/python3
"""This module defines a function that lists the names of states that start
with N in a database"""


def main():
    """This function that lists the names of states that start with N
    in a database"""
    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    sql_query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC;".format(
            argv[4])
    cur.execute(sql_query)
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
