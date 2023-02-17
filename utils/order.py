#all orders
def allOrders(sqlserver):
    cur = sqlserver.cursor()
    ordersData = cur.execute("SELECT * FROM orders")
    ordersData = list(ordersData)
    sqlserver.commit()
    cur.close()
    return ordersData

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