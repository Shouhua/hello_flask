## 安装运行
### windows
```shell
# 1. 下载安装python3.10

# 2. 下载工程

# 3. 进入工程运行
py -3 -m venv .venv
.venv\scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# 4. 本地开发
python app.py

# 5. 如果要安装包使用
python -m pip install ***
python -m pip freeze > requirements.txt
```
### ubuntu
使用python3.10版本，ubuntu安装方法可以参考这个链接：https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/ 安装命令如下：
```shell
sudo apt install python3.10 python3.10-dev python3.10-venv

# 在工程目录运行如下命令
python3.10 -m venv .venv
source .venv/bin/active

# 恢复python安装包
python -m pip install --upgrade pip

# 如果pip安装mysqlclient需要使用的包, ubuntu环境
sudo apt install default-libmysqlclient-dev

pip install -r requirement.txt
python app.py

# 比如安装新的包
python -m pip install flask-restful
pip freeze > requirements.txt

# 退出venv环境
deactive
rm -rf .venv
```

## 配置
- config.py 开发环境配置文件  
- instance/config.py 生产环境配置文件(https://spacewander.github.io/explore-flask-zh/5-configuration.html)

## ORM
Flask-SQLAlchemy

## 日志
flask builtin logger

## 部署
**注意**: 每次生成镜像时，需要确认是否时最新的requirements.txt, 不然部署会产生错误  
目前使用docker镜像部署，将来可能有多个镜像，比如数据库mysql，缓存redis，前端web等，可以统一使用docker compose部署。本工程生成镜像可以使用脚本docker_script，windows使用docker_script.ps1，*nix可以使用docker_script.sh，如果docker registry有变化，可能需要更新脚本内容。

