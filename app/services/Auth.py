from services.Connection import Connection

class Auth:
    
    def __init__(self):
        self.conn = Connection().getConnection()
    
    def sing_in(self, username, password):
        sql = f'select * from service where username = "{username}" and password = "{password}";'
        sql2 =f"select * from user where username ='{username}' and password ='{password}';"
        c = self.conn.cursor()
        c.execute(sql)
        ret =  c.fetchall()
        for row in ret:
            return row
        c.execute(sql2)
        ret =  c.fetchall()
        for row in ret:
            return row