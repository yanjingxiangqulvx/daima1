import pymysql


def mycursor(db_name=None):
    '''连接数据库，创建游标'''
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="123",
        db=db_name,
        charset="utf8")
    cursor = connection.cursor()
    return cursor, connection

def use(db_name):
    '''切换数据库，返回游标'''
    return mycursor(db_name)

def create_database(db_name):
    '''新建数据库'''
    sql = f'create database if not exists {db_name};'
    cursor.execute(sql)

def create_table(tbl_name):
    '''新建数据表'''
    sql = f'CREATE TABLE IF NOT EXISTS {tbl_name} ' \
          f'(ID INT NOT NULL AUTO_INCREMENT,' \
          f'USERNAME VARCHAR (255) NOT NULL,' \
          f'groups VARCHAR (255) NOT NULL,PRIMARY KEY (ID));'
    cursor.execute(sql)

def drop_database(db_name):
    '''删除数据库'''
    sql = f'drop database if exists {db_name};'
    cursor.execute(sql)

def drop_table(tbl_name):
    '''删除数据表'''
    sql = f'drop table if exists {tbl_name};'
    cursor.execute(sql)

def query(sql):
    '''返回查询据结果'''
    cursor.execute(sql)
    data = cursor.fetchone()  # 以元组形式返回查询数据
    return data

def insert():
    '''插入数据'''
    sql = "insert into teams(id, USERNAME, groups) values(3, '王四', '计算机')"
    try:
        cursor.execute(sql)
    except Exception as e: # 捕获所有异常
        print("发生异常", e)
        conn.rollback()  # 事件回滚
    finally:
        conn.close() # 关闭数据库


def update():
    '''更新数据'''
    sql = "update teams set groups = '医学' where USERNAME = '王二'"
    cursor.execute(sql)

def delete():
    '''删除数据'''
    sql = "delete from teams where USERNAME = '王二'"
    cursor.execute(sql)

def show_table(tbl_name):
    '''查看表数据信息'''
    sql = f'select * from {tbl_name}'
    return query(sql)

def show_databases():
    '''查看服务器上的所有数据库'''
    sql = 'show databases;'
    return query(sql)


def select_database():
    '''查看当前数据库'''
    sql = 'select database();'
    return query(sql)


def show_tables():
    '''查看当前数据库中所有的表'''
    sql = 'show tables;'
    return query(sql)


cursor, conn = mycursor("users")
insert()
sql = "select * from teams;"

# print(query(sql))
# create_table('teams')