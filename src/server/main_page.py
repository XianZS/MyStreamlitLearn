# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : main_page.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/21 18:24 
    @NowThing: 
"""
import os
import sys
import streamlit as st
import pandas as pd
from src import api


def __table_things() -> None:
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


def __media_things() -> None:
    """
        > > > streamlit 媒体渲染方法 < <
        image:渲染图片
        audio:渲染音频
        video:渲染视频
        :return:None
    """
    image_path = api.get_root_path() + "/data/static/image/少女.jpg"
    st.image(image_path)
    audio_path1 = api.get_root_path() + "/data/static/audio/曼波.mp3"
    st.audio(audio_path1)
    audio_path2 = api.get_root_path() + "/data/static/video/数据结构的基本概念.mp4"
    st.video(audio_path2)


def __text_things() -> None:
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


def main_page_show() -> bool:
    """
        > > > 主页面导出函数 < < <
        :return:None
        渲染主界面
    """
    try:
        __text_things()
        __table_things()
        __media_things()
        return True
    except Exception as error:
        print(error)
        return False


if __name__ == "__main__":
    __text_things()
    __table_things()
    __media_things()
