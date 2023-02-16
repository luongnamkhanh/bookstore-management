#search book by title
def search_by_title(sqlserver, title):
    cur = sqlserver.cursor()
    cur.execute("exec search_by_title ?", title)
    data = cur.fetchall()
    data = list(data)
    sqlserver.commit()
    cur.close()
    return data

#search book by author name
def search_by_author(sqlserver, name):
    cur = sqlserver.cursor()
    cur.execute("exec search_by_author ?", name)
    data = cur.fetchall()
    data = list(data)
    sqlserver.commit()
    cur.close()
    return data
    