# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : mysql_db.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/21 19:22 
    @NowThing: mysql 数据库操作类
"""
import mysql.connector


class MySqlDB:
    """
    Meaning:
        向外暴露数据库操作类 DataBase
        该类用于连接和操作SQLite数据库。
    Attributes:
        conn (sqlite3.Connection): 数据库连接对象。
        curr (sqlite3.Cursor): 数据库游标对象。
        sqlite_api = SqliteApi("sqlite3.db")
    Example:
        mysql_db = MySqlDB()
        mysql_db.createTable("user", "name text", "age text", "address text")
        mysql_db.insertTable("user", "jom", 19, "Xian")
        print(mysql_db.selectTable("user", "*"))
        mysql_db.dropTable("user")
    """

    def __init__(self):
        # 连接到 MySQL 数据库
        self.conn = mysql.connector.connect(
            # 数据库主机地址
            host="39.100.73.172",
            # 数据库用户名
            user="streamlit_mysql",
            # 数据库密码
            passwd="streamlit_mysql",
            # 数据库名称
            database="streamlit_mysql",
            # 设置字符编码为 utf8mb4
            charset='utf8mb4'
        )

        self.cursor = self.conn.cursor()

    def createTable(self, tableName, *args):
        self.cursor.execute(f"create table if not exists {tableName} ({','.join(args)});")

    def insertTable(self, tableName, *args):
        args = [f"'{arg}'" for arg in args]
        strs = f"insert into {tableName} values({','.join(args)});"
        self.cursor.execute(strs)

    def selectTable(self, tableName, *args):
        self.cursor.execute(f"select {','.join(args)} from {tableName};")
        return self.cursor.fetchall()

    def dropTable(self, tableName):
        self.cursor.execute(f"drop table {tableName};")

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    mysql_db = MySqlDB()
    mysql_db.createTable("user", "name text", "age text", "address text")
    mysql_db.insertTable("user", "jom", 19, "Xian")
    print(mysql_db.selectTable("user", "*"))
    mysql_db.dropTable("user")
    mysql_db.close()
