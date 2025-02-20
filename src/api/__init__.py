# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : __init__.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/20 13:44 
    @NowThing: 
"""
import os
from src.api.root_path import get_root_path

if __name__ == "__main__":
    print(os.path.abspath(os.path.dirname(__file__)))
