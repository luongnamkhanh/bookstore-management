# display total sale by month  
def totalSalebyMonth(sqlserver, month, year):
    cur = sqlserver.cursor()
    try:
        cur.execute("exec sale_by_month ?, ?", month, year)
        saleData = cur.fetchall()
        saleData = list(saleData)
        n = len(saleData)
        totalAmount = 0
        for i in range(n):
            totalAmount += saleData[i][4]
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return saleData, totalAmount, result

#display total sale by year
def totalSalebyYear(sqlserver, year):
    cur = sqlserver.cursor()
    try:
        cur.execute("exec sale_by_year ?", year)
        saleData = cur.fetchall()
        saleData = list(saleData)
        n = len(saleData)
        totalAmount = 0
        for i in range(n):
            totalAmount += saleData[i][4]
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return saleData,totalAmount,result

#display total sale by day
def totalSalebyDay(sqlserver, day, month, year):
    cur = sqlserver.cursor()
    try:
        cur.execute("exec sale_by_day ?, ?, ?", day, month, year)
        saleData = cur.fetchall()
        saleData = list(saleData)
        n = len(saleData)
        totalAmount = 0
        for i in range(n):
            totalAmount += saleData[i][4]
        result = 1
    except:
        result = 0
    sqlserver.commit()
    cur.close()
    return saleData,totalAmount, result

#
