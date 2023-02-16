#all orders
def allOrders(sqlserver):
    cur = sqlserver.cursor()
    ordersData = cur.execute("SELECT * FROM orders")
    ordersData = list(ordersData)
    sqlserver.commit()
    cur.close()
    return ordersData