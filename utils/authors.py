#display authors
def allAuthors(sqlserver):
    cur = sqlserver.cursor()
    cur.execute("exec all_authors")
    authorsData = cur.fetchall()
    authorsData = list(authorsData)
    sqlserver.commit()
    cur.close()
    return authorsData

#delete authors
def delete_Authors(sqlserver, author_id):
    cur = sqlserver.cursor()
    try:
        cur.execute("exec delete_authors ?", author_id)

        result = 1
    except:
        result = 0

    sqlserver.commit()
    cur.close()
    return result

#delete Book Author
def deleteBook_authors(sqlserver, author_id, book_id):
    cur = sqlserver.cursor()
    try:
        cur.execute("DELETE FROM book_author WHERE author_id = ? AND book_id = ?", author_id, book_id)
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return result

#add new authors
def addAuthors(sqlserver, author_name):
    cur = sqlserver.cursor()
    try:
        #add Genre in Author table
        cur.execute("exec insert_authors ?", author_name)
        result = 1
    except:
        result = 0
    
    sqlserver.commit()
    cur.close()
    return result

#search book by author
def findBook_author(sqlserver, author_id):
    cur = sqlserver.cursor()
    cur.execute("select b.* from books as b join book_author as ba on b.book_id = ba.book_id where ba.author_id = ?", author_id)
    book_authorData = cur.fetchall()
    book_authorData = list(book_authorData)
    sqlserver.commit()
    cur.close()
    return book_authorData

def find_author(sqlserver, author_id):
    cur = sqlserver.cursor()
    cur.execute("select * from authors where author_id = ?", author_id)
    book_authorData = cur.fetchall()
    book_authorData = list(book_authorData)
    sqlserver.commit()
    cur.close()
    return book_authorData

def add_new_book_author(sqlserver, author_id, book_id):
    cur = sqlserver.cursor()
    try:
        cur.execute("exec insert_book_author ?, ?", author_id, book_id)
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return result

