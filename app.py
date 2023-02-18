from flask import Flask,render_template,request,redirect,url_for,flash,session
from datetime import datetime

import pyodbc

from utils.home import *
from utils.book import *
from utils.search import *
from utils.order import *
from utils.login import *
from utils.genres import *
from utils.authors import *
from utils.customers import *
from utils.staff import *
from utils.sale import *

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
            session["password"] = password
            return redirect(url_for('homeRoute'))
        else: #login failed
            flash("Login failed!", "error")
    return render_template("login.html")

# home page route
@app.route("/home")
def homeRoute():
    return render_template("home.html")

# genre page route
@app.route("/genre",methods = ['GET', 'POST'])
def genresRoute():
    # genresData = allGenres(sqlserver)
    # return render_template("genres.html", genresData=genresData)
    if (request.method == 'GET'):
        genresData = allGenres(sqlserver)
        return render_template("genres.html", genresData=genresData)
    if (request.method == 'POST'):
        genre_name = request.form["genre_name"]
        genresData = searchGenre(sqlserver, genre_name)
        return render_template("genres.html", genresData=genresData)

# genre page route
@app.route('/bookgenre/<int:id>', methods=['GET', 'POST'])
def book_genreRoute(id):
    if (request.method == 'GET'):
        book_genreData = findBook_genre(sqlserver,id)
        genresData = find_genre(sqlserver, id)
        return render_template("bookgenre.html", genresData=genresData, book_genreData=book_genreData)
    if (request.method == 'POST'):
        genresData = find_genre(sqlserver, id)
        title = request.form["title"]
        book_genreData = searchTitleGenre(sqlserver, title, id)
        return render_template("bookgenre.html",  genresData=genresData,book_genreData=book_genreData)
# author page route
@app.route("/author",methods = ['GET','POST'])
def authorsRoute():
    # authorsData = allAuthors(sqlserver)
    # return render_template("authors.html", authorsData = authorsData)
    if (request.method == 'GET'):
        authorsData = allAuthors(sqlserver)
        return render_template("authors.html", authorsData = authorsData)
    if (request.method == 'POST'):
        author_name = request.form["author_name"]
        authorsData = searchAuthor(sqlserver, author_name)
        return render_template("authors.html", authorsData = authorsData)
# author page route
@app.route('/bookauthor/<int:id>', methods=['GET','POST'])
def book_authorRoute(id):
    if (request.method == 'GET'):
        book_authorData = findBook_author(sqlserver,id)
        authorsData = find_author(sqlserver, id)
        return render_template("bookauthor.html", authorsData=authorsData, book_authorData = book_authorData)
    if (request.method == 'POST'):
        authorsData = find_author(sqlserver, id)
        title = request.form["title"]
        book_authorData = searchTitleAuthor(sqlserver, title, id)
        return render_template("bookauthor.html",  authorsData=authorsData,book_authorData=book_authorData)
#book route
@app.route("/book",methods = ['GET','POST'])
def bookRoute():
    # booksData = allBooks(sqlserver)
    # booksData = searchTitle(sqlserver, "")
    # return render_template("book.html", booksData=booksData)
    if request.method == 'GET':
        booksData = allBooks(sqlserver)
        return render_template("book.html", booksData=booksData)
    if request.method == 'POST':
        search = request.form["search"]
        # title = request.form["title"]
        # booksData = searchTitle(sqlserver, title)
        # return render_template("book.html", booksData=booksData)
        if search == "title":
            title = request.form["query"]
            booksData = searchTitle(sqlserver, title)
            return render_template("book.html", booksData=booksData, search=search)
        if search == "publisher_name":
            publisher = request.form["query"]
            booksData = searchPublisher(sqlserver,publisher)
            return render_template("book.html",booksData = booksData, search=search)

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
        return render_template("addbookgenre.html", genre= cr[0], book_genreData = findBook_genre(sqlserver,genre_id))
    if request.method == 'POST':
        book_id = request.form["book_id"]
        response = add_new_book_genre(sqlserver, genre_id, book_id)
        if response == 1:
            flash("Add book genre successfully!")
            return redirect(url_for('addbookgenre', genre_id = genre_id))
        else:
            flash("Failed", "error")
            return redirect(url_for('addbookgenre', genre_id = genre_id))
        
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
        return render_template("addbookauthor.html", author= cr[0], book_authorData = findBook_author(sqlserver, author_id))
    if request.method == 'POST':
        book_id = request.form["book_id"]
        response = add_new_book_author(sqlserver, author_id, book_id)
        if response == 1:
            flash("Add book author successfully!")
            return redirect(url_for('addbookauthor', author_id=author_id))
        else:
            flash("Failed", "error")
            return redirect(url_for('addbookauthor', author_id=author_id))

#delete book genre
@app.route('/deletebookgenre/<int:genre_id>/<int:book_id>')
def deleteBook_genre(genre_id,book_id):
    response = deleteBook_genres(sqlserver, genre_id, book_id)
    if response == 1:
        flash("Deleted successfully!")
        return redirect(url_for('book_genreRoute', id = genre_id))
    else:
        flash("Failed", "error")
        return redirect(url_for('book_genreRoute', id = genre_id))

#delete book author
@app.route('/deletebookauthor/<int:author_id>/<int:book_id>')
def deleteBook_author(author_id,book_id):
    response = deleteBook_authors(sqlserver, author_id, book_id)
    if response == 1:
        flash("Deleted successfully!")
        return redirect(url_for('book_authorRoute', id = author_id))
    else:
        flash("Failed", "error")
        return redirect(url_for('book_authorRoute', id = author_id))

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
    
#display all customer route
@app.route('/customer',methods=['GET','POST'])
def customersRoute():
    # customersData = allCustomers(sqlserver)
    # return render_template("customer.html", customersData = customersData) 
    if request.method == 'GET':
        cusData = allCustomers(sqlserver)
        return render_template("customer.html",customersData=cusData)
    if request.method == 'POST':
        search = request.form["search"]
        if search == "phone_number":
            phone_number= request.form["query"]
            cusData = searchCustomerPhone(sqlserver,phone_number)
            return render_template("customer.html",customersData=cusData, search=search)
        elif search == "email":
            email= request.form["query"]
            cusData = searchCustomerEmail(sqlserver,email)
            return render_template("customer.html",customersData=cusData, search=search)

#add customers route
@app.route('/addcustomer', methods=['GET', 'POST'])
def addCustomersRoute():
    if request.method == 'GET':
        return render_template("addcustomer.html", customer = None)
    if request.method == 'POST':
        customer_id =  int(request.form['customer_id'])
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = int(request.form['gender'])
        dob = request.form['dob']
        email = request.form['email']
        phone_number = request.form['phone_number']
        address = request.form['address']
        response = addCustomers(sqlserver,customer_id, first_name, last_name, gender, dob, email, phone_number, address)
        if response == 1:
            flash("Add customer successfully!")
            return redirect(url_for('customersRoute'))
        else: 
            flash("Failed", "error")
            return (redirect(url_for('addCustomersRoute')))
    
#delete Customer Route
@app.route('/deletecustomer/<int:id>')
def deleteCustomer(id):
    response = deleteCustomers(sqlserver, id)
    if response == 1:
        flash("Deleted successfully!")
        return redirect(url_for('customersRoute'))
    else:
        flash("Failed to delete", "error")
        return redirect(url_for('customersRoute'))
    
# Update Book Route
@app.route('/updatecustomer/<int:id>',methods = ['GET','POST'])
def updatecustomer(id):
    if request.method == 'GET':
        cr = []
        conn = connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.customers WHERE customer_id = ?", id)
        for row in cursor.fetchall():
            cr.append({"customer_id": row[0], "first_name": row[1], "last_name": row[2], "gender": row[3], "dob": row[4], "email": row[5], "phone_number":row[6], "address":row[7]})
        conn.close()
        return render_template("addcustomer.html", customer = cr[0])
    if request.method == 'POST':
        customer_id =  int(request.form['customer_id'])
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = int(request.form['gender'])
        dob = request.form['dob']
        email = request.form['email']
        phone_number = request.form['phone_number']
        address = request.form['address']
        response = updateCustomers(sqlserver, customer_id, first_name, last_name, gender, dob, email, phone_number, address)
        if response == 1: #book updated successfully
            flash("Book updated successfully!")
            return redirect(url_for('customersRoute'))
        else: #book failed to update
            flash("Book failed to update!", "error")
            return redirect(url_for('addCustomersRoute', id = id))
        return redirect('/book')

#All staff route
@app.route('/staff')
def staffRoute():
    staffsData = allStaffs(sqlserver)
    return render_template("staff.html", staffsData = staffsData)

#Add staff route
@app.route('/addstaff', methods = ['GET', 'POST'])
def addStaffRoute():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT role FROM staffs where account LIKE ? AND password LIKE ?", session["account"], session["password"])
    role_data = cur.fetchall()[0][0]
    cur.close()
    if request.method == 'GET':
        if role_data == 1:
            flash("You have no rights to add the other staffs", "error")
            return redirect(url_for('staffRoute')) 
        if role_data == 2:
            return render_template("addstaff.html")
    if request.method == 'POST':
        staff_id = int(request.form["staff_id"])
        name = request.form["name"]
        account = request.form["account"]
        password = request.form["password"]
        role = int(request.form["role"])
        response = addStaffs(sqlserver, staff_id, name, account, password, role)
        if response == 1:
            flash("You added the new staff successfully!")
            return redirect(url_for('staffRoute'))
        else:
            flash("Failed!", "error")
            return redirect(url_for('addStaffRoute'))
        
#delete staff route
@app.route('/deletestaff/<int:id>')
def deleteStaffRoute(id):
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT role FROM staffs where account LIKE ? AND password LIKE ?", session["account"], session["password"])
    role_data = cur.fetchall()[0][0]
    cur.close()
    cur2 = conn.cursor()
    cur2.execute("SELECT staff_id FROM staffs where account LIKE ? AND password LIKE ?", session["account"], session["password"])
    staff_data = cur2.fetchall()[0][0]
    cur2.close()
    if role_data == 1:
        flash("You have no rights to delete the others!", "error")
        return redirect(url_for('staffRoute'))
    elif role_data ==2:  
        if id == staff_data:
            flash("You can not delete yourself!", "error")
            return redirect(url_for('staffRoute'))
        else:
            response = delelteStaffs(sqlserver, id)
            if response == 1:
                flash("Deleted successfully!")
                return redirect(url_for('staffRoute'))
            else:
                flash('Failed to delete', "error")
                return redirect(url_for('staffRoute')) 
            
#order route
@app.route('/order')
def orderRoute():
    ordersData = allOrders(sqlserver)
    return render_template('order.html', ordersData = ordersData)

#add order route
@app.route('/addorder', methods=['POST', 'GET'])
def addOrdersRoute():
    conn = connection()
    cur1 = conn.cursor()
    cur1.execute("SELECT staff_id FROM staffs where account LIKE ? AND password LIKE ?", session["account"], session["password"])
    staff_data = cur1.fetchall()[0][0]
    cur1.close()
    if request.method == 'GET':
        return render_template("addorder.html")
    if request.method == 'POST':
        cur2 = sqlserver.cursor()
        customer_id = int(request.form['customer_id'])
        order_date = request.form['order_date']
        order_date2 = datetime.strptime(order_date, '%Y-%m-%dT%H:%M')
        try:
            cur2.execute("exec insert_orders ?,?,?", customer_id, order_date2, staff_data)
            result = 1
        except:
            result = 0
        cur2.close()
        if result == 1:
            flash("Add new order successfully!")
            return redirect(url_for('orderRoute'))
        else:
            flash("Failed", "error")
            return redirect(url_for('addOrdersRoute'))
        
#delete order Route
@app.route('/deleteorder/<int:id>')
def deleteOrderRoute(id):
    order_status = check_order_status(sqlserver, id)
    if order_status == 1:
        flash("The order was approved, you cannot delete the order", "error")
        return redirect(url_for('orderRoute'))
    else:
        response = approve_deleteOrders(sqlserver, id, 2)
        if response == 1:
            flash("Deleted the order successfully")
            return redirect(url_for('orderRoute'))
        else:
            flash("Failed to delete the order", "error")
            return redirect(url_for('orderRoute'))
    
#approve order Route
@app.route('/approveorder/<int:id>')
def approveOrderRoute(id):
    response = approve_deleteOrders(sqlserver, id, 1)
    if response == 1:
        flash("Approved the orders")
        return redirect(url_for('orderRoute'))
    else:
        flash("Failed to approve the order", "error")
        return redirect(url_for('orderRoute'))
    
# orderline Route
@app.route('/orderline/<int:id>', methods = ['GET', 'POST'])
def orderlineRoute(id):
    if request.method == 'GET':
        order_status = check_order_status(sqlserver, id)
        order = orderData(sqlserver, id)
        orderlinesData = allOrderlines(sqlserver, id)
        return render_template('orderline.html', order = order, orderlinesData = orderlinesData)
    if request.method == 'POST':
        order_status = check_order_status(sqlserver, id)
        if order_status == 1:
            order = orderData(sqlserver, id)
            orderlinesData = allOrderlines(sqlserver, id)
            flash("The order was approved. You cannot add anymore", "error")
            return render_template('orderline.html', order = order, orderlinesData = orderlinesData)
        if order_status == 0:
            orderline_id = int(request.form['orderline_id'])
            book_id = int(request.form['book_id'])
            quantity = int(request.form['quantity'])
            if (quantity <= check_book_instock(sqlserver, book_id)):
                response = addOrderlines(sqlserver, id, orderline_id, book_id, quantity)
                
                if response == 1:
                    order = orderData(sqlserver, id)
                    orderlinesData = allOrderlines(sqlserver, id)
                    flash("Added new orderlines successfully")
                    return render_template('orderline.html', order = order, orderlinesData = orderlinesData)
                else:
                    order = orderData(sqlserver, id)
                    orderlinesData = allOrderlines(sqlserver, id)
                    flash("Failed to add new orderlines", "error")
                    return render_template('orderline.html', order = order, orderlinesData = orderlinesData)
            else:
                order = orderData(sqlserver, id)
                orderlinesData = allOrderlines(sqlserver, id)
                flash("You cannot add more quantity than in the stock", "error")
                return render_template('orderline.html', order = order, orderlinesData = orderlinesData)
            
#delete orderline Route
@app.route('/deleteorderline/<int:order_id>/<int:orderline_id>')
def deleteOrderlinesRoute(order_id, orderline_id):
    order_status = check_order_status(sqlserver, order_id)
    if order_status == 1:
        flash("The order was approved. You cannot delete anymore", "error")
        return redirect(url_for('orderlineRoute', id = order_id))
    if order_status == 0:
        response = deleteOrderlines(sqlserver, order_id, orderline_id)
        if response == 1:
            flash("Deleted orderlines successfully")
            return redirect(url_for('orderlineRoute', id = order_id))
        else:
            flash("Failed to delete orderlines", "error")
            return redirect(url_for('orderlineRoute', id = order_id))

#sale route
@app.route('/sale', methods = ['GET', 'POST'])
def saleRoute():
    if request.method == 'GET':
        return render_template('sale.html')
    if request.method == 'POST':
        day = request.form['day']
        month = request.form['month']
        year = request.form['year']
        if day == "" and month != "" and year != "":
            
            saleData,totalAmount = totalSalebyMonth(sqlserver, month, year)
            return render_template('sale.html', ordersData = saleData,total=totalAmount)
        if day == "" and month == "" and year != "":
            saleData ,totalAmount= totalSalebyYear(sqlserver, year)
            return render_template('sale.html', ordersData = saleData,total=totalAmount)
        if day != "" and month != "" and year != "":
            saleData,totalAmount = totalSalebyDay(sqlserver, day, month, year)
            return render_template('sale.html', ordersData = saleData,total=totalAmount)


# logout route
@app.route("/logout",methods = ["GET","POST"])
def logoutRoute():
    session.pop("account",None) # removing username from session variable
    session.pop("password", None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
