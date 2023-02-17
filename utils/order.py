#all orders
def allOrders(sqlserver):
    cur = sqlserver.cursor()
    ordersData = cur.execute("SELECT * FROM orders")
    ordersData = list(ordersData)
    sqlserver.commit()
    cur.close()
    return ordersData

#delete order
def deleteOrders(sqlserver, order_id):
    cur = sqlserver.cursor()
    try:
        cur.execute("DELETE FROM orders where order_id = ?", order_id)
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return result