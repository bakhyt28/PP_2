import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="987654321"
)

cur = conn.cursor()

while True:
    print("\n1. Search")
    print("2. Add/Update")
    print("3. Bulk Insert")
    print("4. Pagination")
    print("5. Delete")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pattern = input("Enter search pattern: ")
        cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
        rows = cur.fetchall()
        for row in rows:
            print(row)

    elif choice == "2":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
        conn.commit()

    elif choice == "3":
        names = input("Enter names (comma separated): ").split(',')
        phones = input("Enter phones (comma separated): ").split(',')
        cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
        conn.commit()

    elif choice == "4":
        limit = int(input("Enter limit: "))
        offset = int(input("Enter offset: "))
        cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
        rows = cur.fetchall()
        for row in rows:
            print(row)

    elif choice == "5":
        value = input("Enter name or phone to delete: ")
        cur.execute("CALL delete_contact(%s)", (value,))
        conn.commit()

    elif choice == "0":
        break

cur.close()
conn.close()
import csv

with open("contacts.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)