import pymysql

def Insert(news):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='mysql!1234', db='navernews_test', charset='utf8')
    cursor = conn.cursor()
    
    query = """insert into newses (headnews) 
            values (%s)
            """
    cursor.execute(query, (news,))
    conn.commit()
    conn.close()
    print(conn)
  