# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : main_page_2.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/22 10:31 
    @NowThing: checkbox, radio, button, selectbox（下拉单选）, multiselect（下拉多选）
"""
import os
import sys
import streamlit as st

index = 1


def __changed_function():
    """
        改变函数
        :global:index
        :return:None
    """
    global index
    print()
    print(f"{index} >>> 正在被改变")
    index += 1
    print("......")


def __checkbox_things() -> None:
    """
        复选框
        st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)
            label:标签
            value:默认值
            on_change:改变时的回调函数
            args:回调函数的参数
        :return:None
    """
    st.header("复选框")
    state = st.checkbox("我是一个复选框",
                        value=True,
                        key="checkbox_1",
                        on_change=__changed_function())
    if state:
        st.write("我被选中了")
    else:
        st.write("我没有被选中")


def __radio_things() -> None:
    """
        单选框
        st.radio(label, options=None, index=0, format_func=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)
            label:标签
            options:选项
            index:默认值
            on_change:改变时的回调函数
            args:回调函数的参数
        :return:None
    """
    st.header("单选框")
    state = st.radio("单选框", options=("radio_1", "radio_2", "radio_3"))
    print(f"state:{state}")
    st.text(f"state:{state}")


def __btn_click() -> None:
    """
        按钮点击事件
        :return:None
    """
    print("BUTTON CLICKED ! BUTTON CLICKED! BUTTON CLICKED!")


def __button_things() -> None:
    """
        按钮
        st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, disabled=False)
            label:标签
            on_click:点击时的回调函数
            args:回调函数的参数
        :return:None
    """
    st.header("按钮")
    state = st.button("Button", on_click=__btn_click())


def __selectbox_function():
    """
        下拉框改变事件
        :return:None
    """
    print("SELECTBOX CHANGED! SELECTBOX CHANGED! SELECTBOX CHANGED!")


def __selectbox_one_things() -> None:
    """
        下拉单选框
        st.selectbox(label, options, index=0, format_func=str, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)
            label:标签
            options:选项
            index:默认值
            on_change:改变时的回调函数
            args:回调函数的参数
        :return:None
    """
    st.header("下拉框")
    select_one = st.selectbox("下拉框",
                              options=("selectbox1", "selectbox2", "selectbox3"),
                              on_change=__selectbox_function())
    print(f"select_one:{select_one}")


def __selectbox_some_things() -> None:
    """
        下拉多选框
        st.multiselect(label, options, default=None, format_func=str, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False)
            label:标签
            options:选项
            default:默认值
            on_change:改变时的回调函数
            args:回调函数的参数
        :return:None
    """
    st.header("下拉多选框")
    select_some = st.multiselect("下拉多选框",
                                 options=("selectbox1", "selectbox2", "selectbox3"))
    print(f"select_some:{select_some}")
    st.json(select_some)


def main_page_2_show():
    st.title("Streamlit 学习")
    __checkbox_things()
    __radio_things()
    __button_things()
    __selectbox_one_things()
    __selectbox_some_things()
    pass


if __name__ == '__main__':
    main_page_2_show()
