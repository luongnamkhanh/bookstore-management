# function to get all books
def allBooks(sqlserver):
    cur = sqlserver.cursor()
    cur.execute("exec all_books")
    booksData = cur.fetchall()
    booksData = list(booksData)
    sqlserver.commit()
    cur.close()
    return booksData