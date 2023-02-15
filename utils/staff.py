#list all staff
def allStaffs(sqlserver):
    cursor = sqlserver.cursor()
    staffData = cursor.execute("SELECT staff_id, name, account, role from staffs")
    staffData = list(staffData)
    sqlserver.commit()
    cursor.close()
    return staffData

