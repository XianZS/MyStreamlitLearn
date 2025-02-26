# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : main_page_3.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/22 21:01 
    @NowThing: 1.st.file_uploader 上传文件方法
               2.st.slider 滑动条方法
               3.
"""
from datetime import timedelta
from typing import Union

import streamlit as st


def __upload_things():
    """
        上传文件
        st.file_uploader(
            # 显示标题
            label,
            # 文件类型 参数为list
            type=None,
            # 设置是否允许多个文件上传,默认为False不允许多文件上传
            accept_multiple_files=False,
        )
        :return:
    """
    st.subheader("上传图片")
    st.markdown("""
        ---
    """)
    upload_image = st.file_uploader("上传图片",
                                    type=["png", "jpg", "jpeg"],
                                    accept_multiple_files=True)
    if upload_image:
        # st.write(upload_image[0].name)
        # st.write(upload_image[0].type)
        # st.write(upload_image[0].size)
        st.image(upload_image[0])

    upload_file = st.file_uploader("上传文件",
                                   type=["md", "txt", "py"],
                                   accept_multiple_files=True)
    if upload_file:
        st.code(upload_file[0].getvalue().decode("utf8"), language="python")


def __slider_things() -> None:
    """
        滑动条方法
        st.slider(
            # 显示标题
            label,
            # 最小值
            min_value=None,
            # 最大值
            max_value=None,
            # 步长
            step=None,
            # 滑动条的默认值
            value=None,
            # 滑动条的格式
            format=None,
            # 滑动条的key
            key=None,
            # 滑动条的帮助信息
            help=None,
            # 滑动条的回调函数
            on_change=None,
            # 滑动条的参数
            args=None,
            # 滑动条的kwargs
            kwargs=None,
            # 滑动条的禁用状态
            disabled=False,
            # 滑动条的标签
            label_visibility="visible",
        )
        :return:
    """
    st.subheader("滚动条")
    st.markdown("""
        ---
    """)
    val = st.slider("This is a slider.",
                    # 最小可选值
                    min_value=20,
                    # 最大可选值
                    max_value=100,
                    # 初始值
                    value=70)
    st.write(f"当前选择值为 : {val}")


def __input_things() -> None:
    """
        st.text_input("文本输入",max_chars=最大输入上限)
        :return:
    """
    st.subheader("输入框")
    st.markdown("""
        ---
    """)
    val = st.text_input("普通输入")
    st.write(f"你的输入为:{val}")

    def clear_input() -> None:
        if st.session_state.user_input_things:
            st.session_state.input_things = st.session_state.user_input_things
        st.session_state.user_input_things = ""

    st.text_input("用户文本输入",
                  key="user_input_things",
                  max_chars=1000,
                  on_change=clear_input)
    if "input_things" in st.session_state:
        st.write(f"st.session_state type is {type(st.session_state)}")
        st.write(f"st.session_state things is {st.session_state}")
        st.write(f"你的输入 : {st.session_state.input_things}")

    # 日期输入
    date_input = st.date_input("日期选择输入",
                               key="user_date_input")
    st.write(f"st.session_state is {date_input}")
    import datetime
    # 时间输入
    time_input = st.time_input("时间选择输入",
                               # key 设置为 user_time_input
                               key="user_time_input",
                               # step 设置为 1 分钟
                               step=datetime.timedelta(minutes=1),
                               )
    st.write(f"st.session_state is {time_input}")


def main_page_3_show():
    __upload_things()
    __slider_things()
    __input_things()


if __name__ == "__main__":
    main_page_3_show()
