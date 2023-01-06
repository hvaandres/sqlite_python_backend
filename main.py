import sqlite3

connection = sqlite3.connect("Books.db")
# Create a cursor object
cursor = connection.cursor()

cursor.execute("create table books (release_year integer, book_name text, author text)")


list_books = [
    (2022, "The survivalists", "Kasahana Cauley"),
    (2022, "Spare", "Prince Harry"),
    (2022, "The faraway world", "Patricia Engel"),
    (2022, "Central places", "Delia Cal"),
    (2022, "Love pamela", "Pamela Anderson"),
    (2022, "Save whats left", "Elizabeth Castellano")
]

cursor.executemany(" insert into books values (?,?,?)", list_books)


# Print database rows
for row in cursor.execute("select * from books"):
    print(row)

# Select specific rows
print("***********************")
cursor.execute("select * from books where author=:c", {"c": "Pamela Anderson"},)
books_search = cursor.fetchall()
print(books_search)


cursor.execute("create table releaseMonth (release_year integer, release_month text)")

bookRelease = [
    (2022, "February"),
    (2022, "March"),
    (2022, "June"),
    (2022, "July"),
    (2022, "June"),
    (2022, "February")
]

cursor.executemany("insert into releaseMonth values (?,?)", bookRelease)
cursor.execute("select * from releaseMonth where release_month=:c", {"c": "February"},)
release_month_search = cursor.fetchall()
print(release_month_search)

print("***********************")

for i in books_search:
    change = [books_search[0][0] if value==bookRelease[0][0] else value for value in i]
    print(change)

connection.close()