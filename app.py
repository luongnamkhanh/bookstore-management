from flask import Flask,render_template,request,redirect,url_for,flash,session

import pyodbc

from utils.home import *
from utils.book import *
from utils.search import *
from utils.order import *
from utils.login import *

app = Flask(__name__)
def connection():
    s = 'DESKTOP-APQT58G' #Your server name 
    d = 'bookstore' 
    u = 'khanhluong' #Your login
    p = 'khanh692' #Your login password
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
    booksData = allBooks(sqlserver)
    return render_template("home.html", booksData=booksData)

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
            return redirect(url_for('homeRoute'))
        else: #book failed to add
            flash("Book failed to add!", "error")
            return redirect(url_for('addbook', book = request.form))
        return redirect('/home')

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
            return redirect(url_for('homeRoute'))
        else: #book failed to update
            flash("Book failed to update!", "error")
            return redirect(url_for('updatebook', id = id))
        return redirect('/home')

# Delete Book Route
@app.route('/deletebook/<int:id>')
def deletebook(id):
    response = deleteBook(sqlserver,id)
    if response == 1:
        flash("Book deleted successfully!")
        return redirect(url_for('homeRoute'))
    else:
        flash("Book failed to delete!", "error")
        return redirect(url_for('homeRoute'))


# logout route
@app.route("/logout",methods = ["GET","POST"])
def logoutRoute():
    session.pop("account",None) # removing username from session variable
    return redirect(url_for('login'))
if __name__ == '__main__':
    app.run(debug=True)
