#!/usr/bin/python3
"""This module defines a function that safely displays all cities of a
state using the database"""


def main():
    """This function displays all cities of a state using the database"""

    from sys import argv
    import MySQLdb

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    sql_query = """SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %(state_name)s;"""
    cur.execute(sql_query, {'state_name': argv[4]})
    query_rows = cur.fetchall()
    result = [city[0] for city in query_rows]
    print(", ".join(result))
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
