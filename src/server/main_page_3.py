# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : main_page_3.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/22 21:01 
    @NowThing: 
"""
import streamlit as st


def __upload_things():
    """
        上传文件
        st.file_uploader(
            # 显示标题
            label,
            # 文件类型 参数为list
            type=None,
            # 设置是否允许多个文件上传
            accept_multiple_files=False,
        )
        :return:
    """
    st.title("file_uploader")
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

    st.subheader("上传文件")
    upload_file = st.file_uploader("上传文件",
                                   type=["md", "txt", "py"],
                                   accept_multiple_files=True)
    if upload_file:
        st.code(upload_file[0].getvalue().decode("utf8"), language="python")


def main_page_3_show():
    __upload_things()


if __name__ == "__main__":
    main_page_3_show()
