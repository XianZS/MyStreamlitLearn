# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : text.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/20 12:08 
    @NowThing: 
"""
import streamlit as st


def text_things() -> None:
    """
        > > > streamlit 文本渲染方法 < < <
        title:页面大标题
        header:一级标题
        subheader:二级标题
        text:普通文本
        markdown:渲染markdown文本
        latex:渲染latex公式文本
        json:渲染JSON格式数据
        code:渲染传入代码
        :return:None
    """
    st.title("StreamLit")
    st.header("Web App")
    st.subheader("Author : XianZS")
    st.text("text")
    md: str = """
        ## One
        > 内容
        * 选项1
        * 选项2
        * 选项3
        ## Two
        > 内容
        * 选项1
        * 选项2
        * 选项3
    """
    st.markdown(md)
    st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
    jsonThings = {
        "name": "jom",
        "age": 19,
        "address": "Xi'an"
    }
    st.json(jsonThings)
    codeThings = """
        def Hello():
            print("hello world")
        Hello()
    """
    st.code(codeThings, language="python")
