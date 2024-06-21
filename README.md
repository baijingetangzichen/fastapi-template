# fastapi-template
使用fastapi实现web后端，包括登录 异步操作 orm 
## 数据库
注意： 在api下的每个目录中的models，如果想迁移成功，必须导入到alembic/env.py中
+　创建数据库
```
CREATE USER comm_llm_api WITH PASSWORD 'q8x06B4uF9JJ8B1Jh7xo';
CREATE DATABASE comm_llm_api OWNER comm_llm_api;
GRANT ALL PRIVILEGES ON DATABASE comm_llm_api TO comm_llm_api;
```
+ 初始化
```
# 初始化
alembic init alembic
# 使用命令，生成当前的版本
alembic revision --autogenerate -m "init"
# 将alembic的版本更新到最新版
alembic upgrade head
```
+ 再次迁移表
```
alembic revision --autogenerate -m "用户表"
alembic upgrade head
```

