# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : root_path.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/20 13:38 
    @NowThing: 
"""
import os
import sys


# 获得根路径
def get_root_path():
    # 获取文件目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # print(f"curPath >>> {curPath}")
    # 获取项目根路径，内容为当前项目的名字
    rootPath = curPath[:curPath.find("MyStreamlitLearn") + len("MyStreamlitLearn")]
    return rootPath


if __name__ == '__main__':
    print(get_root_path())
