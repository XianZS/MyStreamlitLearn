# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : setup.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/21 12:46 
    @NowThing: 
"""
import os
import sys
import subprocess


def init_MyStreamlitLearn() -> bool:
    """
    启动应用程序
    :return: bool
    """
    python_exec = sys.executable
    print(f"Now python env/conda is {python_exec}")
    try:
        # pip3 install -r requirements.txt
        # 添加超时保护和返回值检查
        exit_code = subprocess.call(
            [python_exec, "-m", "pip", "install", "-r", "requirements.txt"],
            timeout=60 * 10  # 添加启动超时限制 10 分钟
        )
        if exit_code != 0:
            print(f"初始化项目异常，所执行代码为 : {exit_code}")
            return False
    except subprocess.TimeoutExpired:
        print("项目初始化超时")
        return False
    return True


if __name__ == '__main__':
    if init_MyStreamlitLearn():
        print("项目初始化成功")
        print("The project is initialized successfully")
    else:
        print("项目初始化失败")
        print("The project is initialization failed")
