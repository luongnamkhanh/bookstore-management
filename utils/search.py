def searchTitle(sqlserver,title):
    cur = sqlserver.cursor()
    cur.execute("exec search_by_title ?", title)	
    booksData = cur.fetchall()
    booksData = list(booksData)
    sqlserver.commit()
    cur.close()
    return booksData

def searchPublisher(sqlserver,publisher):
    cur = sqlserver.cursor()
    cur.execute("exec search_by_publisher ?", publisher)	
    booksData = cur.fetchall()
    booksData = list(booksData)
    sqlserver.commit()
    cur.close()
    return booksData

def searchGenre(sqlserver,genre_name):
    cur = sqlserver.cursor()
    cur.execute("exec search_genres_by_genre_name ?", genre_name)	
    booksData = cur.fetchall()
    booksData = list(booksData)
    sqlserver.commit()
    cur.close()
    return booksData

def searchTitleGenre(sqlserver,title,genre_id):
    cur = sqlserver.cursor()
    cur.execute("exec search_by_genre ?, ?", title, genre_id)	
    booksData = cur.fetchall()
    booksData = list(booksData)
    sqlserver.commit()
    cur.close()
    return booksData

def searchAuthor(sqlserver,author_name):
    cur = sqlserver.cursor()
    cur.execute("exec search_authors_by_author_name ?", author_name)	
    booksData = cur.fetchall()
    booksData = list(booksData)
    sqlserver.commit()
    cur.close()
    return booksData

def searchTitleAuthor(sqlserver,title,author_id):
    cur = sqlserver.cursor()
    cur.execute("exec search_by_author ?, ?", title, author_id)	
    booksData = cur.fetchall()
    booksData = list(booksData)
    sqlserver.commit()
    cur.close()
    return booksData

def searchCustomerPhone(sqlserver,phone_number):
    cur = sqlserver.cursor()
    cur.execute("exec search_customer_by_phone ?", phone_number)
    cusData = cur.fetchall()
    cusData= list(cusData)
    sqlserver.commit()
    cur.close()
    return cusData
def searchCustomerEmail(sqlserver,email):
    cur = sqlserver.cursor()
    cur.execute("exec search_customer_by_email ?", email)
    cusData = cur.fetchall()
    cusData= list(cusData)
    sqlserver.commit()
    cur.close()
    return cusData