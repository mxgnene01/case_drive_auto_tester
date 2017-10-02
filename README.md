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
python manage.py makemigrations sign

python manage.py migrate
```

## 4.3 基本数据访问

```
python manage.py shell

>>> from sign.models import Event, Guest
>>> Event.objects.all()

-- select
>>> Event.objects.get(name='aaa').address

-- insert
>>> Event.objects.create()

-- like
>>> Event.objects.filter(name__contains='发布会')

-- delete
>>> Guest.objects.get(phone='13611001101').delete()

-- update
>>> g3=Guest.objects.get(phone='13611001101') >>> g3.realname='andy2'
>>> g3.save()
```

## 运行单元测试

```
-- 执行的是 sign/tests.py
python manage.py test
```

## 运行 sign 应用下的所有测试用例

```
python manage.py test sign
```

## 运行sign应用下的tests.py 测试文件

```
python manage.py test sign.tests
```

## 运行 sign 应用 tests.py 测试文件下的 ModelTest 测试类

```
python manage.py test sign.tests.ModelTest
```

## 执行 ModelTest 测试类下面的 test_event_models 测试方法(用例)

```
python manage.py test sign.tests.ModelTest.test_event_models
```

## 除此之外，我们还可以使用 -p (或 --pattern)参数模糊匹配测试文件

```
python manage.py test -p test*.py
```