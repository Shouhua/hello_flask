# 设置连接数据库的URL
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@10.122.48.111:3306/company"
# 设置每次请求结束后会自动提交数据库的改动
SQLALCHEMY_COMMIT_ON_TEARDOWN = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 查询时显示原始SQL语句
# SQLALCHEMY_ECHO = True