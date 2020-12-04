import xlrd
import pymysql

# 创建打开excel函数

def open_excel():
    try:
        book = xlrd.open_workbook("知乎热榜.xlsx")
    except:
        print("打开excel文件失败！")
    try:
        sheet = book.sheet_by_name("Sheet")  # excel表中sheet名
        return sheet
    except:
        print("在excel中查找sheet失败！")


# 连接数据库
try:
    db = pymysql.connect("localhost", "root", "123456", "zhihu", charset="utf8")
except:
    print("连接数据库失败！")

# 创建数据表
# 使用 cursor() 方法创建一个游标对象 cursor
cursor_sql = db.cursor()
# 使用预处理创建表
# #排名id   #标题title  #热度heat  #回答链接html  #回答数reply  #关注数attention  #浏览数browse  #时间time
sql = """
CREATE TABLE zhihu_heat(
  id int(2) NOT NULL AUTO_INCREMENT,  
  title_name varchar(255) NOT NULL,   
  heat varchar(255) NOT NULL,         
  html varchar(255) NOT NULL,         
  reply varchar(255) NOT NULL,         
  attention varchar(255) NOT NULL,    
  browse varchar(255) NOT NULL,       
  times varchar(255) NOT NULL,         
  PRIMARY KEY (id)
) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
"""
# 执行sql语句
cursor_sql.execute(sql)


# 创建数据插入函数
def insert_data():
    sheet = open_excel()
    cursor = db.cursor() # 使用cursor方法创建游标对象
    nrows_counts = sheet.nrows  # 获取excel数据行数
    for i in range(1, nrows_counts):
        # 获取每一个行中每个单元格的数据
        # #排名id   #标题title  #热度heat  #回答链接html  #回答数reply  #关注数attention  #浏览数browse  #时间time
        id = sheet.cell(i, 0).value
        title_name = sheet.cell(i, 1).value
        heat = sheet.cell(i, 2).value
        html = sheet.cell(i, 3).value
        reply = sheet.cell(i, 4).value
        attention = sheet.cell(i, 5).value
        browse = sheet.cell(i, 6).value
        time = sheet.cell(i, 7).value
        # 打印
        print(id,title_name,heat,html,reply,attention,browse,time)
        value = [id,title_name,heat,html,reply,attention,browse,time]  # 将数据写入元组
        print(value)
        # 创建数据库语句
        try:

            sqls = "insert into zhihu_heat(id,title_name,heat,html,reply,attention,browse,times) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            # sql = "INSERT INTO zhihu_heat(id,title,heat,html,reply,attention,browse,time)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sqls, value)
            db.commit() # 将所做的操作提交保存到数据库
        except:

            print("插入失败")
    cursor.close()  # 关闭连接
    db.close()  # 关闭数据库连接
    print("数据全部写入成功")

# 执行函数
open_excel()
insert_data()
