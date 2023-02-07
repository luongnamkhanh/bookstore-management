# function for login
def login1(sqlserver,account,password):
    cur = sqlserver.cursor()
    cur.execute("exec login_staff ?, ?",account,password)
    check = cur.fetchall()
    check = list(check)

    if not check:
        result = 0 # login failed
    else:
        result = 1 # login success
    
    sqlserver.commit()
    cur.close()
    return result