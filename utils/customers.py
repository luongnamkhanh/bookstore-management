#display all customers
def allCustomers(sqlserver):
    cur = sqlserver.cursor()
    cur.execute("exec all_customers")
    customersData = cur.fetchall()
    customersData = list(customersData)
    sqlserver.commit()
    cur.close()
    return customersData

#add customers
def addCustomers(sqlserver, customer_id, first_name, last_name, gender, dob, email, phone_number, address, staff_id):
    cur = sqlserver.cursor()
    try:
        cur.execute("exec insert_customers ?, ?, ?, ?, ?, ?, ?, ?,?", customer_id, first_name, last_name, gender, dob, email, phone_number, address, staff_id)
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return result

#def delete customer by id
def deleteCustomers(sqlserver, customer_id):
    cur = sqlserver.cursor()
    try:
        cur.execute("DELETE FROM dbo.customers WHERE customer_id = ?", customer_id)
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return result

#update customer
def updateCustomers(sqlserver, customer_id, first_name, last_name, gender, dob, email, phone_number, address):
    cur = sqlserver.cursor()
    try:
        cur.execute("UPDATE customers SET first_name = ?, last_name = ?, gender = ?, dob = ?, email = ?, phone_number=?, address = ? WHERE customer_id = ? ",first_name, last_name, gender, dob, email, phone_number, address, customer_id)
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return result
