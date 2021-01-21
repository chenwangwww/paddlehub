import pymysql

def connDb(func):
    def wrapper(self, *args, **kw):
        if not self.conn.open:
            self.conn.connect()
        ret = func(self, *args, **kw)
        return ret
    return wrapper

class MysqlGeoCtr(object):
    def __init__(self):
        self.conn = pymysql.Connect("localhost", "root", "123", "geography", charset="utf8")
        self.cursor = self.conn.cursor()

    #插入数据
    @connDb
    def insertData(self, tb, info):
        sql = "INSERT INTO " + tb + "(geo, geo_link, loc, loc_link)VALUES(%s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, [info['geo'], info['geo_link'], info['loc'], info['loc_link']])
            self.conn.commit()
        except Exception as identifier:
            print(identifier)
            self.conn.rollback()
        finally:
            pass

    #创建数据表
    @connDb
    def createTb(self, tb):
        sql = "CREATE TABLE IF NOT EXISTS " + tb + "(geo VARCHAR(100) NOT NULL,geo_link TEXT,loc VARCHAR(100) NOT NULL,loc_link TEXT)"
        self.cursor.execute(sql)

    #删除数据表
    @connDb
    def dropTb(self, tb):
        sql = "DROP TABLE IF EXISTS " + tb
        self.cursor.execute(sql)

    #删除数据
    @connDb
    def deleteData(self, tb, name=None):
        sql = "DELETE FROM " + tb
        sql += (" WHERE name = " + name) if name is not None else ''
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
    def querygeoData(self, tb, name=None):
        sql = "SELECT * FROM " + tb
        sql += (" WHERE geo = '" + name + "'") if name is not None else ''
        results = None
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone() if name is not None else self.cursor.fetchall()
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

    #获取数据库所有表名
    @connDb
    def getAllTbs(self):
        results = []
        sql = "SHOW TABLES"
        self.cursor.execute(sql)
        results = list(self.cursor.fetchall())
        return results

geoctr = MysqlGeoCtr()
