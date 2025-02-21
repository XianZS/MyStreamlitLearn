# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : sqlite_db.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/21 18:40 
    @NowThing: sqlite 数据库操作类
"""
import sqlite3
from src import api


class SqliteDB:
    """
    Meaning:
        向外暴露数据库操作类 DataBase
        该类用于连接和操作SQLite数据库。
    Attributes:
        conn (sqlite3.Connection): 数据库连接对象。
        curr (sqlite3.Cursor): 数据库游标对象。
        sqlite_api = SqliteApi("sqlite3.db")
    Example:
        # 创建一个DataBase类的实例，连接到名为"myData"的数据库
        sqlite_api.createTable("myTable", "title text", "author text", "tags text")
        sqlite_api.insertTable("myTable", "test", "test", "test")
        sqlite_api.dropTable("myDataBaseThings")
        sqlite_api.close()
    """

    def __init__(self, dataBaseName):
        """
        初始化数据库连接

        Args:
            dataBaseName (str): 数据库名称。
        """
        load = api.get_root_path() + f"/data/db/{dataBaseName}.db"
        print(f"load >>> {load}")
        # 连接到指定的SQLite数据库
        self.conn = sqlite3.connect(load)
        # 创建一个游标对象，用于执行SQL语句
        self.curr = self.conn.cursor()

    def createTable(self, tableName, *args):
        """
        创建一个新的表

        Args:
            tableName (str): 表名
            *args (str): 表的列名和数据类型，例如 "id INTEGER", "name TEXT"
        """
        strs = f"create table if not exists {tableName} ({','.join(args)});"
        try:
            self.curr.execute(strs)
            self.conn.commit()  # 提交事务
            return True
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            return False

    def insertTable(self, tableName, *args):
        """
        向表中插入数据

        Args:
            tableName (str): 表名
            *args (str): 要插入的数据，例如 "1", "John Doe", "john.doe@example.com"
        """
        args = [f"'{arg}'" for arg in args]
        # args = [f"'{arg}'" if isinstance(arg, str) else str(arg) for arg in args]
        strs = f"insert into {tableName} values({','.join(args)});"
        # print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        # print("strs : ", strs)
        self.curr.execute(strs)
        self.conn.commit()

    def dropTable(self, tableName):
        """
        删除表

        Args:
            tableName (str): 要删除的表名
        """
        strs = f"drop table {tableName};"
        print("strs : ", strs)
        self.curr.execute(strs)

    def close(self):
        """
        关闭数据库连接
        """
        self.curr.close()
        self.conn.close()


if __name__ == "__main__":
    sqlite_api = SqliteDB("sqlite3")
    # 创建一个DataBase类的实例，连接到名为"myData"的数据库
    sqlite_api.createTable("myTable", "title text", "author text", "tags text")
    sqlite_api.insertTable("myTable", "test", "test", "test")
    sqlite_api.close()
