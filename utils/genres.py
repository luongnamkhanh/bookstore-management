#display genres
def allGenres(sqlserver):
    cur = sqlserver.cursor()
    cur.execute("exec all_genres")
    genresData = cur.fetchall()
    genresData = list(genresData)
    sqlserver.commit()
    cur.close()
    return genresData

#delete genres
def delete_Genres(sqlserver, genre_id):
    cur = sqlserver.cursor()
    try:
        cur.execute("exec delete_genres ?", genre_id)

        result = 1
    except:
        result = 0

    sqlserver.commit()
    cur.close()
    return result

#delete Book Genre
def deleteBook_genres(sqlserver, genre_id, book_id):
    cur = sqlserver.cursor()
    try:
        cur.execute("DELETE FROM book_genre WHERE genre_id = ? AND book_id = ?", genre_id, book_id)
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return result

#add new genres
def addGenres(sqlserver, genre_name):
    cur = sqlserver.cursor()
    try:
        #add Genre in Genre table
        cur.execute("exec insert_genres ?", genre_name)
        result = 1
    except:
        result = 0
    
    sqlserver.commit()
    cur.close()
    return result

#search book by genre
def findBook_genre(sqlserver, genre_id):
    cur = sqlserver.cursor()
    cur.execute("select b.* from books as b join book_genre as bg on b.book_id = bg.book_id where bg.genre_id = ?", genre_id)
    book_genreData = cur.fetchall()
    book_genreData = list(book_genreData)
    sqlserver.commit()
    cur.close()
    return book_genreData

def find_genre(sqlserver, genre_id):
    cur = sqlserver.cursor()
    cur.execute("select * from genres where genre_id = ?", genre_id)
    book_genreData = cur.fetchall()
    book_genreData = list(book_genreData)
    sqlserver.commit()
    cur.close()
    return book_genreData

def add_new_book_genre(sqlserver, genre_id, book_id):
    cur = sqlserver.cursor()
    try:
        cur.execute("exec insert_book_genre ?, ?", genre_id, book_id)
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return result

