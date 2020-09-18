import pymysql

def Insert(ss):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='mysql!1234', db='navernews_test', charset='utf8')
    cursor = conn.cursor()
    
    query = """insert into samsunglionsnews (title) 
            values (%s)
            """
    cursor.execute(query, (ss,))
    conn.commit()
    conn.close()
    print(conn)
  