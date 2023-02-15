from flask import Flask,render_template,request,redirect,url_for,flash,session

import pyodbc

from utils.home import *
from utils.book import *
from utils.search import *
from utils.order import *
from utils.login import *
from utils.genres import *
from utils.authors import *

app = Flask(__name__)
def connection():
    s = '' #Your server name 
    d = 'bookstore' 
    u = 'sa' #Your login
    p = '' #Your login password
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+s+';DATABASE='+d+';UID='+u+';PWD='+ p
    conn = pyodbc.connect(cstr)
    return conn

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # all the session data is encrypted in the server so we need a secret key to encrypt and decrypt the data
sqlserver = connection()

# login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        account = request.form.get('account')
        password = request.form.get('password')

        response = login1(sqlserver,account,password)
        if response == 1: #login success
            flash("Login success!")
            session["account"] = account # creating a session of the username
            return redirect(url_for('homeRoute'))
        else: #login failed
            flash("Login failed!", "error")
    return render_template("login.html")

# home page route
@app.route("/home")
def homeRoute():
    return render_template("home.html")

# genre page route
@app.route("/genre")
def genresRoute():
    genresData = allGenres(sqlserver)
    return render_template("genres.html", genresData=genresData)

# genre page route
@app.route('/bookgenre/<int:id>', methods=['GET'])
def book_genreRoute(id):
    if (request.method == 'GET'):
        book_genreData = findBook_genre(sqlserver,id)
        genresData = find_genre(sqlserver, id)
        return render_template("bookgenre.html", genresData=genresData, book_genreData=book_genreData)
    
# author page route
@app.route("/author")
def authorsRoute():
    authorsData = allAuthors(sqlserver)
    return render_template("authors.html", authorsData = authorsData)

# author page route
@app.route('/bookauthor/<int:id>', methods=['GET'])
def book_authorRoute(id):
    if (request.method == 'GET'):
        book_authorData = findBook_author(sqlserver,id)
        authorsData = find_author(sqlserver, id)
        return render_template("bookauthor.html", authorsData=authorsData, book_authorData = book_authorData)

#book route
@app.route("/book")
def bookRoute():
    booksData = allBooks(sqlserver)
    return render_template("book.html", booksData=booksData)

# Add Book Route
@app.route("/addbook", methods = ['GET','POST'])
def addbook():
    if request.method == 'GET':
        return render_template("addbook.html", book = None)
    if request.method == 'POST':
        book_id = int(request.form["book_id"])
        title = request.form["title"]
        price = float(request.form["price"])
        publisher_name = request.form["publisher_name"]
        publication_date = request.form["publication_date"]
        quantity = int(request.form["quantity"])
        response = addBook(sqlserver,book_id,title,price,publisher_name,publication_date,quantity)
        if response == 1: #book added successfully
            flash("Book added successfully!")
            return redirect(url_for('bookRoute'))
        else: #book failed to add
            flash("Book failed to add!", "error")
            return redirect(url_for('addbook', book = request.form))
        return redirect('/book')

# Update Book Route
@app.route('/updatebook/<int:id>',methods = ['GET','POST'])
def updatebook(id):
    
    if request.method == 'GET':
        cr = []
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.books WHERE book_id = ?", id)
        for row in cursor.fetchall():
            cr.append({"book_id": row[0], "title": row[1], "price": row[2], "publisher_name": row[3], "publication_date": row[4], "quantity": row[5]})
        conn.close()
        return render_template("addbook.html", book = cr[0])
    if request.method == 'POST':
        title = request.form["title"]
        price = float(request.form["price"])
        publisher_name = request.form["publisher_name"]
        publication_date = request.form["publication_date"]
        quantity = int(request.form["quantity"])
        
        response = updateBook(sqlserver,id,title,price,publisher_name,publication_date,quantity)
        if response == 1: #book updated successfully
            flash("Book updated successfully!")
            return redirect(url_for('bookRoute'))
        else: #book failed to update
            flash("Book failed to update!", "error")
            return redirect(url_for('updatebook', id = id))
        return redirect('/book')

# Delete Book Route
@app.route('/deletebook/<int:id>')
def deletebook(id):
    response = deleteBook(sqlserver,id)
    if response == 1:
        flash("Book deleted successfully!")
        return redirect(url_for('bookRoute'))
    else:
        flash("Book failed to delete!", "error")
        return redirect(url_for('bookRoute'))


#add book genre route
@app.route('/addbookgenre/<int:genre_id>', methods=['GET', 'POST'])
def addbookgenre(genre_id): 
    if request.method == 'GET':
        cr = []
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.genres WHERE genre_id = ?", genre_id)
        for row in cursor.fetchall():
            cr.append({"genre_id": row[0], "genre_name": row[1] })
        conn.close()
        return render_template("addbookgenre.html", genre= cr[0])
    if request.method == 'POST':
        book_id = request.form["book_id"]
        response = add_new_book_genre(sqlserver, genre_id, book_id)
        if response == 1:
            flash("Add book genre successfully!")
            return redirect(url_for('genresRoute'))
        else:
            flash("Failed", "error")
            return redirect(url_for('genresRoute'))
        
#add book author route
@app.route('/addbookauthor/<int:author_id>', methods=['GET', 'POST'])
def addbookauthor(author_id): 
    if request.method == 'GET':
        cr = []
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.authors WHERE author_id = ?", author_id)
        for row in cursor.fetchall():
            cr.append({"author_id": row[0], "author_name": row[1] })
        conn.close()
        return render_template("addbookauthor.html", author= cr[0])
    if request.method == 'POST':
        book_id = request.form["book_id"]
        response = add_new_book_author(sqlserver, author_id, book_id)
        if response == 1:
            flash("Add book author successfully!")
            return redirect(url_for('authorsRoute'))
        else:
            flash("Failed", "error")
            return redirect(url_for('authorsRoute'))

#delete book genre
@app.route('/deletebookgenre/<int:genre_id>/<int:book_id>')
def deleteBook_genre(genre_id,book_id):
    response = deleteBook_genres(sqlserver, genre_id, book_id)
    if response == 1:
        flash("Deleted successfully!")
        return redirect(url_for('genresRoute'))
    else:
        flash("Failed", "error")
        return redirect(url_for('genresRoute'))

#delete book author
@app.route('/deletebookauthor/<int:author_id>/<int:book_id>')
def deleteBook_author(author_id,book_id):
    response = deleteBook_authors(sqlserver, author_id, book_id)
    if response == 1:
        flash("Deleted successfully!")
        return redirect(url_for('authorsRoute'))
    else:
        flash("Failed", "error")
        return redirect(url_for('authorsRoute'))

#Add Genre Route
@app.route('/addgenre', methods=['GET', 'POST'])
def addGenre():
    if request.method == 'GET':
        return render_template("addgenre.html", genre=None)
    if request.method == 'POST':
        genre_name = request.form['genre_name']
        response = addGenres(sqlserver, genre_name)
        if response == 1:
            flash("Gerne added successfully!")
            return redirect(url_for('genresRoute'))
        else:
            flash("Genre failed to add!", "error")
            return redirect(url_for('addgenre'), genre=request.form)
        return redirect('/genres')

#Add Author Route
@app.route('/addauthor', methods=['GET', 'POST'])
def addAuthor():
    if request.method == 'GET':
        return render_template("addauthor.html", author=None)
    if request.method == 'POST':
        author_name = request.form['author_name']
        response = addAuthors(sqlserver, author_name)
        if response == 1:
            flash("Author added successfully!")
            return redirect(url_for('authorsRoute'))
        else:
            flash("Author failed to add!", "error")
            return redirect(url_for('addauthor'), author=request.form)
        return redirect('/authors')


#Delele Genre Route
@app.route('/deletegenre/<int:id>')
def deleteGenres(id):
    response = delete_Genres(sqlserver, id)
    if response == 1:
        flash("Genre deleted successfully!")
        return redirect(url_for('genresRoute'))
    else:
        flash("Genre failed to delete!", "error")
        return redirect(url_for('genresRoute'))

#Delele Author Route
@app.route('/deleteauthor/<int:id>')
def deleteAuthors(id):
    response = delete_Authors(sqlserver, id)
    if response == 1:
        flash("Author deleted successfully!")
        return redirect(url_for('authorsRoute'))
    else:
        flash("Author failed to delete!", "error")
        return redirect(url_for('authorsRoute'))

# logout route
@app.route("/logout",methods = ["GET","POST"])
def logoutRoute():
    session.pop("account",None) # removing username from session variable
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
