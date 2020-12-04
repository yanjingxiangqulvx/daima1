import pymongo
import datetime
import re

client = pymongo.MongoClient()
#连接DB数据库
db = client['DB']
#连接集合user，集合类似关系数据库的数据表
#如果集合不存在，就会新建集合user
user_collection = db.user
#设置文档格式（文档即我们常说的数据）
user_info = {'_id':'100','author':'小黄','text':'Python爬虫开发','tags':['mongodb','python','pymongo'],'date':datetime.datetime.utcnow()}

user_id = user_collection.insert_one(user_info).inserted_id
print("user id is",user_id)

user_infos = [{
    'id':101,
    'author':'小黄',
        'text':'Python爬虫开发',
        'tags':['mongodb','python','pymongo'],
        'date':datetime.datetime.utcnow()},
    {
    'id':102,
    'author':'小黄_A',
        'text':'Python爬虫开发_A',
        'tags':['mongodb','python','pymongo'],
        'date':datetime.datetime.utcnow()
    }]

user_id = user_collection.insert_many(user_infos).inserted_ids
print("user id is",user_id)