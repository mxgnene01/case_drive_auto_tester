# 说明

学习虫师 python web接口开发及测试 记录


# 中间用的命令

## 创建 guest 项目

```
django-admin startproject guest
```

## 创建 sign 项目

```
cd guest; python manage.py startapp sign
```

## 运行项目

```
python manage.py runserver [127.0.0.1:8000]
```

## 数据的迁移 migrate

```
-- 使用session 之后需要django 帮忙创建 django_session 表
python manage.py migrate
```

## 创建admin 后台的帐号

```
python manage.py createsuperuser
```

## 写过model 之后，进行数据库的创建

```
python3 manage.py makemigrations sign

python3 manage.py migrate
```