# -*- coding: UTF-8 -*-
"""
    @Project : MyStreamlitLearn 
    @File    : test_run.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/2/21 13:16 
    @NowThing: 
"""
import os
import sys
import subprocess


def run() -> bool:
    python_exe_path = sys.executable
    print(f"Now python env/conda is {python_exe_path}")

    try:
        # 使用subprocess.run替代os.system
        result = subprocess.run(
            [python_exe_path, "-m", "streamlit", "run", "./src/main.py"],
            timeout=60 * 10,    # 短暂测试 10 分钟
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"应用异常退出，代码：{e.returncode}")
        print(f"错误输出：{e.stderr.decode()}")
        return False
    except subprocess.TimeoutExpired as e:
        return True


if __name__ == '__main__':
    if run():
        print("应用测试完成")
    else:
        print("应用测试失败")
