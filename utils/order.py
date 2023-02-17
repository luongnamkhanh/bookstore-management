import pyodbc

#all orders
def allOrders(sqlserver):
    cur = sqlserver.cursor()
    ordersData = cur.execute("SELECT * FROM orders")
    ordersData = list(ordersData)
    sqlserver.commit()
    cur.close()
    return ordersData

#delete/approve order
def approve_deleteOrders(sqlserver, order_id, new_status):
    cur = sqlserver.cursor()
    try:
        cur.execute("exec update_status_by_orderid ?, ?", order_id, new_status)
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return result

#order Data
def orderData(sqlserver, order_id):
    cur = sqlserver.cursor()
    orderData = cur.execute("SELECT * from orders where order_id = ?", order_id)
    orderData = list(orderData)
    data = orderData[0]
    sqlserver.commit()
    cur.close()
    return data

#check order status
def check_order_status(sqlserver, order_id):
    cur = sqlserver.cursor()
    status_data = cur.execute("SELECT status from orders where order_id = ?", order_id)
    status_data = list(status_data)
    data = status_data[0][0]
    sqlserver.commit()
    cur.close()
    return data

#list all orderlines by order id
def allOrderlines(sqlserver, order_id):
    cur = sqlserver.cursor()
    orderlinesData = cur.execute("SELECT ol.* FROM orderlines AS ol JOIN orders AS o ON o.order_id = ol.order_id WHERE ol.order_id = ?", order_id)
    orderlinesData = list(orderlinesData)
    sqlserver.commit()
    cur.close()
    return orderlinesData

def addOrderlines(sqlserver, order_id, orderline_id, book_id, quantity):
    cur = sqlserver.cursor()
    try:
        cur.execute("exec insert_orderlines ?, ?, ?, ?", orderline_id, order_id, book_id, quantity)
        result = 1
    except pyodbc.Error:
        result = 0
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return result

def check_book_instock(sqlserver, book_id):
    cur = sqlserver.cursor()
    data = cur.execute("SELECT quantity FROM books WHERE book_id = ?", book_id)
    data =list(data)
    data = data[0][0]
    sqlserver.commit()
    cur.close()
    return data

def deleteOrderlines(sqlserver, order_id, orderline_id):
    cur = sqlserver.cursor()
    try:
        cur.execute("exec delete_orderlines ?, ?", order_id, orderline_id)
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return result
