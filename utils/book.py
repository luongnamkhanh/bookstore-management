# add book function
def addBook(sqlserver,book_id,title,price,publisher_name,publication_date,quantity):
    cur = sqlserver.cursor()
    try:
        # add book in Books table
        cur.execute("exec insert_books ?, ?, ?, ?, ?, ? ",book_id,title,price,publisher_name,publication_date,quantity)
    
        result = 1 # book added successfully
    except:
        result = 0 # book failed to add
    
    sqlserver.commit()
    cur.close()

    return result

# update book function
def updateBook(sqlserver,book_id,title,price,publisher_name,publication_date,quantity):
    cur = sqlserver.cursor()

    try:
        cur.execute("UPDATE dbo.books SET title = ?, price = ?, publisher_name = ?,publication_date =?, quantity=? WHERE book_id = ?", title, price, publisher_name,publication_date, quantity, book_id)
        result = 1 # book updated successfully
     
    except:
        result = 0 # book failed to update

    sqlserver.commit()
    cur.close()

    return result

# delete book function
def deleteBook(sqlserver,book_id):
    cur = sqlserver.cursor()
    try:
        cur.execute("exec delete_books ?", book_id)
        
        result = 1 # book deleted successfully 
    
    except:
        result = 0 # book failed to delete

    sqlserver.commit()
    cur.close()

    return result

# function to get all books
def allBooks(sqlserver):
    cur = sqlserver.cursor()
    cur.execute("exec all_books")
    booksData = cur.fetchall()
    booksData = list(booksData)
    sqlserver.commit()
    cur.close()
    return booksData