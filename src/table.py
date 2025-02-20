# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : table.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/20 12:09 
    @NowThing: 
"""
import streamlit as st
import pandas as pd


def table_things() -> None:
    """
        > > > streamlit 表格渲染方法 < <
        write:常用于渲染图像等
        metric:渲染指标
            * label:指标名称
            * value:指标数值
            * delta:指标变化量
                * delta="-1.4ms\^-1" 会出现一个向下的箭头
                * delta="1.4ms\^-1" 会出现一个向上的箭头
        table:渲染表格
        dataframe【推荐使用】:渲染数据框 与 table 的区别在于 dataframe 可以设置列宽
        :return:None
    """
    st.write("## H2")
    st.metric(label="Wind Speed", value="120ms\^-1", delta="-1.4ms\^-1")
    tb = pd.DataFrame({
        "first column": [1, 2, 3, 4],
        "second column": [10, 20, 30, 40]
    })
    tb2 = {
        "one": [1, 2, 3],
        "Two": [4, 5, 6],
        "Three": [7, 8, 9]
    }
    st.table(tb2)
    st.dataframe(tb, width=500)
