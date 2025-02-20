# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : media.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/20 12:09 
    @NowThing: 
"""
import streamlit as st
import os


def media_things() -> None:
    """
        > > > streamlit 媒体渲染方法 < <
        image:渲染图片
        audio:渲染音频
        video:渲染视频
        :return:None
    """
    image_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/data/static/image/少女.jpg"
    print(f"ROOT_PATH: {image_path}")
    st.image(image_path)
    audio_path1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/data/static/audio/曼波.mp3"
    st.audio(audio_path1)
    audio_path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/data/static/audio/数据结构的基本概念.mp4"
    st.video(audio_path2)
