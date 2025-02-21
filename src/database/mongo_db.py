# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : mongo_db.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/21 20:24 
    @NowThing: 
"""
import pymongo


class MyMongoDB:
    def __init__(self, cho_set):
        """
        初始化MyMongoDB类的实例。

        该方法创建一个MongoDB客户端连接，并选择要使用的数据库和集合。

        Attributes:
            conn (pymongo.MongoClient): MongoDB客户端连接对象。
            collection (pymongo.collection.Collection): 选择的集合对象。
        """
        # host = '39.100.73.172'
        # username = 'social'
        # password = 'YangHaiTao3135'
        # port = '27017'
        # db = 'social'
        # 创建一个MongoDB客户端连接，指定主机和端口
        # self.conn = pymongo.MongoClient('mongodb://{0}:{1}@{2}:{3}/?authSource={4}&authMechanism=SCRAM-SHA-1'.
        #                                 format(username, password, host, port, db))
        self.conn = pymongo.MongoClient(
            host='39.100.73.172',
            port=27017,
            username='streamlit_mongo',
            password='streamlit_mongo',
            authSource='streamlit_mongo',
        )
        # 选择名为 ' social ' 的数据库
        db = self.conn['streamlit_mongo']
        # 选择名为 ' cho_set ' 的集合
        self.collection = db[f"{cho_set}"]

    def insert_one_things(self, **kwargs):
        print(kwargs)
        res = self.collection.insert_one(kwargs)
        print(res.inserted_id)

    def insert_many_things(self, *args, **kwargs):
        print(args[0])
        res = self.collection.insert_many(args[0])
        print(res.inserted_ids)

    def close(self):
        """
        关闭MongoDB连接。
        该方法关闭与MongoDB服务器的连接，释放资源。
        """
        # 关闭与MongoDB服务器的连接
        self.conn.close()


if __name__ == '__main__':
    myMongoDB = MyMongoDB("test")
    myMongoDB.insert_one_things(name="XianZS", age=20)
    myMongoDB.insert_many_things([
        {"name": "jom", "age": 20},
        {"name": "kom", "age": 21},
        {"name": "lom", "age": 22},
    ])
    myMongoDB.close()
