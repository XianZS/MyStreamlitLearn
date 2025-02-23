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
    st.title("上传文件")
    st.markdown("""
        ---
    """)
    upload_image = st.file_uploader("上传图片", type=["png", "jpg", "jpeg"])
    if upload_image:
        st.write(upload_image.name)
        st.write(upload_image.type)
        st.write(upload_image.size)
        # st.write(upload_image.getvalue())
        st.image(upload_image)


def main_page_3_show():
    __upload_things()


if __name__ == "__main__":
    main_page_3_show()
