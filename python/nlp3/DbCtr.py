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
        self.conn = pymysql.Connect("localhost", "root", "123", "test", charset="utf8")
        self.cursor = self.conn.cursor()

    #插入数据
    @connDb
    def insertData(self, tb, info):
        sql = "INSERT INTO " + tb + "(name, sequence)VALUES(%s, %s)"
        try:
            self.cursor.execute(sql, [info['name'], pymysql.Binary(info['sequence'])])
            self.conn.commit()
        except Exception as identifier:
            print(identifier)
            self.conn.rollback()
        finally:
            pass

    #创建数据表
    @connDb
    def createTb(self, tb):
        sql = "CREATE TABLE IF NOT EXISTS " + tb + "(name VARCHAR(50) NOT NULL,sequence TEXT)"
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
    def queryData(self, tb, name=None):
        sql = "SELECT * FROM " + tb
        sql += (" WHERE name = " + name) if name is not None else ''
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
    def updateData(self, tb, name, info):
        sql = "UPDATE " + tb + " SET sequence=%s where name=%s"
        try:
            self.cursor.execute(sql, [pymysql.Binary(info), name])
            self.conn.commit()
        except:
            print("update data failed!")
            self.conn.rollback()

ctr = MysqlCtr()

# content = '以下例子中我们将在 RUNOOB 数据库中创建数据表runoob_tbl以下例子中我们将在 RUNOOB 数据库中创建数据表runoob_tbl以下例子中我们将在 RUNOOB 数据库中创建数据表runoob_tbl'[:40]
# ctr.insertData('apps', {'name':content, 'country':'cn'})
# ctr.createTb('tt', {'name':40,'mean':100})
# ctr.dropTb('tt')
# ctr.queryData('apps', "'taobao'")
# ctr.deleteData('apps', "'taobao'")
# ctr.queryData('apprrrrs', "'taobao'")