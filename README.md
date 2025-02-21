# MyStreamlitLearn

Streamlit数据应用开发学习项目

## 一、🚀 功能特性

- 媒体文件处理模块
- 多环境启动配置
- Streamlit Web界面集成
- 模块化项目结构

## 二、📦 安装依赖

### 1.`requirements.txt`手动安装

```shell
pip install -r requirements.txt
```

### 2.`python`脚本安装

```shell
python run setup.py
```

### 3.直接安装方式

```markdown
请直接运行`setup.py`文件
```

## 三、🖥 快速开始

### 1.`shell`启动方式

```shell
streamlit run main.py
```

### 2.短暂测试启动

```markdown
直接运行`test_run.py`文件
```

### 3.`shell`脚本启动方式
```shell
source ./run.sh
```
## 四、📂 项目结构

```markdown
MyStreamlitLearn/
├── data/                   # 数据存储目录
│   ├── db/                 # 数据库文件存储
│   └── static/             # 静态资源文件
├── src/                    # 核心源代码
│   ├── database/           # 数据库操作模块
│   │   └── mysql_db.py     # MySQL连接器
|   |   └── sqlite_db.py    # SQLite连接器
|   |   └── mongo_db.py     # MongoDB连接器
│   ├── api/                # API接口模块
│   ├── conf/               # 配置文件
│   ├── logs/               # 日志文件
│   └── server/             # 服务端逻辑
├── requirements.txt        # Python依赖清单
├── setup.py                # 项目初始化安装脚本
├── main.py                 # Streamlit主入口-shell
├── test_run.py             # 快速测试入口-run
└── run.sh                  # Shell启动脚本-linux-source
```

## 五、📄 许可证

`MIT License`
