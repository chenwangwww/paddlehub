import pymysql

def connDb(func):
    def wrapper(self, *args, **kw):
        if not self.conn.open:
            self.conn.connect()
        ret = func(self, *args, **kw)
        return ret
    return wrapper

class MysqlCtr(object):
    def __init__(self):
        self.conn = pymysql.Connect(host="localhost", user="root", password="123", database="test", charset="utf8")
        self.cursor = self.conn.cursor()

    #插入数据
    @connDb
    def insertData(self, tb, info):
        sql = "INSERT INTO " + tb + "(id, sequence)VALUES(%s, %s)"
        try:
            self.cursor.execute(sql, [info['id'], pymysql.Binary(info['sequence'])])
            self.conn.commit()
        except Exception as identifier:
            print(identifier)
            self.conn.rollback()
        finally:
            pass

    #创建数据表
    @connDb
    def createTb(self, tb):
        sql = "CREATE TABLE IF NOT EXISTS " + tb + "(id VARCHAR(50) NOT NULL,sequence BLOB) ENGINE=InnoDB DEFAULT CHARSET=utf8"
        self.cursor.execute(sql)

    #删除数据表
    @connDb
    def dropTb(self, tb):
        sql = "DROP TABLE IF EXISTS " + tb
        self.cursor.execute(sql)

    #删除数据
    @connDb
    def deleteData(self, tb, id=None):
        sql = "DELETE FROM " + tb
        sql += (" WHERE id = " + id) if id is not None else ''
        result = None
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            result = True
        except:
            self.conn.rollback()
            print('delete data fail!') 
        finally:
            return result

    #查询数据
    @connDb
    def queryData(self, tb, id=None):
        sql = "SELECT * FROM " + tb
        sql += (" WHERE id = '" + id + "'") if id is not None else ''
        results = None
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
        except:
            print("query data error!")
        finally:
            return results

    #清空数据表
    @connDb
    def truncateTb(self, tb):
        sql = "TRUNCATE TABLE " + tb
        try:
            self.cursor.execute(sql)
        except:
            print("truncate fail!")

    #更新数据
    @connDb
    def updateData(self, tb, id, info):
        sql = "UPDATE " + tb + " SET sequence=%s where id=%s"
        try:
            self.cursor.execute(sql, [pymysql.Binary(info), id])
            self.conn.commit()
        except:
            print("update data failed!")
            self.conn.rollback()

ctr = MysqlCtr()
