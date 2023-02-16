#list all staff
def allStaffs(sqlserver):
    cursor = sqlserver.cursor()
    cursor.execute("SELECT staff_id, name, account, role from staffs")
    staffData = cursor.fetchall()
    staffData = list(staffData)
    sqlserver.commit()
    cursor.close()
    return staffData

#add staff
def addStaffs(sqlserver, staff_id, name, account, password, role):
    cur = sqlserver.cursor()
    try:
        cur.execute("insert into dbo.staffs(staff_id, name, account, password, role) values(?,?,?,?,?)", staff_id, name, account, password, role)
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return result

#delete staff
def delelteStaffs(sqlserver, staff_id):
    cur = sqlserver.cursor()
    try:
        cur.execute("DELETE FROM dbo.staffs WHERE staff_id = ?", staff_id)
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return result
