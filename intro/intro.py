'''DRF'''
# API(Aplicatoin programming interface) - это соприкосновения клиента и сервера, 
# предназначена для взаимодействия между программами 

# '''REST(representational state transfer) - стиль Api, стандарт, которому следует API'''
# 1. разграничение клиента и сервера
# 2. отсутствие состояние( нет сохранения состояния) - сервер не должен хранить какую либо информацию о клиенте
# 3. кэширвание
# 4. многоуровнеывя система 
# 5. единный интерфейс
# 6. код предоставляет по запросу 



# RESTfull API = API которое соответсвует принципам REST 



# 1. Создаем виртуальные окружение
# python3 -m venv venv
# 2. активируем виртуальные окружение
# . venv/bin/activate
# 3. создаем файл req.txt
# записываем: Django
# djangorestframework
# psycopg2-binary
# 4. устанавливаем: pip3 install -r req.txt
# 5. django-admin startprogect <название> .
# если в конце не поставить точку то будет ошибка
# 6. python3 manage.py startapp <app_name>
# создание приложения
# 7. открывает файл settings.py в INSTALED_APPS -> региструем rest_framework, <app_name>
# 8. файл settings.py настраиваем базу данных
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'test',
#         'USER': 'hello',
#         'PASSWORD': 1,
#         'HOST': 'localhost',
#         'PORT': 5432
# python3 manage.py makemigrations - создает файл миграций
# python3 manage.py migrate

# python3 manage.py createsuperuser - создание суперпользователя (админа)
# python3 manage.py runserver - запуск проекта

'''Models'''
# как проходит запрос
# 1. asgi/wsgi - (те кто принимают запрос и возвращает ответ)
# 2. settings - middlewares
# 3. urls - маршрутизароры
# 4. views - представления (функция, которые возвращают данные в нужнои формате)
# 5. serializers (классы, которые переводят данные из json в python и наоборот)
# 6. models (классы, которые обозначают как будет выглядеть наша таблицв в база данных)
# 7. managers(objects) - классы, которые работают с ORM
# 8. db - база данных

'''Поля'''
# CharField -  для строкового значения(обязательно нужно указывать max_length)
# SlugField - для хранения slug (обычно используется в url) содержит ттолько буквы, числа, -, _
# TextField - для хранения текста
# DecimalField - для дробных чисел (max_digit: количество цифр целой части,
# decimal_places(количество цифр после запятой)
# IntegerField - для чисел
# BooleanField - для bool значений
# DateField - для дат (datetime.date) - можно передать аргументы: auto_now -> обновляется при запиииииси
# auto_now_add -> задается только один раз при создании
# TimeField - для времени (auto_now, auto_now_add)
# DateTimeField - для даты и времени
# EmailField - для email
# FileField - для файлов и принимает аргументы как(upload_to - указание директории,
# где будет хранится файл)
# ImageField - для картинок
# JSONField - для строк в формате json

'''Ключевые параметры для полей(функции)'''
# null - если True, будет в бд записывать null, если данные не переданы
# blank - если True, будет ставить пустую строку(не обязательно для заполнения)
# default - значение по умолчанию
# unique - если true, в колонке могут храниться только уникальные значения
# primary_key если True, первичный ключ - идентиификатор
# choices - список с tuple(ограничиваем возможные варианты для заполнения)

'''Связи'''
# ForeignKey - свзяь один ко многим (обязательно указать модельна которую мы будем ссылаться, on_delete, related_name - для обратной связи)
# ManyToManyField - многи ко многим (все тоже самое, что и ForeignKey)


'''on_delete'''
# models.CASCADE - каскадное удаление (если удаляется главный объект, то удаляются и зависящие от него)
# models.PROTECT - вызывает ошибку при попытке удалсить главный объект
# models.SET_NULL - не уадляет зависящие объекты, а ставит null(null=True)
# models.SET_DEFAULT - если определен default, то ставит его
# models.DO_NOTHING - ничего не делает, вызывается ошибка 

# Product.objects.all()
# # SELECT * FROM products;
#
# Product.objects.get(id=1)
# SELECT * FROM products WHERE id = 1;

# Product.objects.filter(условие1, условие2)
# SELECT * FROM products WHERE условие AND условие2;

# Product.objects.filter(Q(условие)|Q(условие2))
# SELECT * FROM products WHERE условие1 OR условие2;

# Product.objects.filter(~Q(условие))
# Product.objects.exclude(условие)
# SELECT * FROM products WHERE NOT условие;

# Product.objects.filter(price__gt=50000) #больше
# SELECT * FROM products WHERE price > 50000;

# Product.objects.filter(price__lt=50000) #меньше
# SELECT * FROM products WHERE price < 50000;

# Product.objects.filter(price=50000) #равно
# SELECT * FROM products WHERE price = 50000;

# Product.objects.filter(~Q(price=50000))
# SELECT * FROM products WHERE NOT price = 50000;

# Product.objects.filter(price__gte=50000)
# SELECT * FROM products WHERE price >= 50000;

# Product.objects.filter(price__lte=50000)
# SELECT * FROM products WHERE price <= 50000;

# Product.objects.filter(category_id__in=['phones', 'notebooks'])
# SELECT * FROM product WHERE category_id IN ('phones', 'notebooks');

# Product.objects.filter(price__range=[20000, 50000])
# SELECT * FROM products WHERE price BETWEEN 20000 AND 50000;

# Product.objects.filter(name__exact='Iphone')
# SELECT * FROM products WHERE name LIKE 'Iphone';
# Product.objects.filter(name__iexact='Iphone')
# # SELECT * FROM products WHERE name ILIKE 'Iphone';

# Product.objects.filter(name__startswith='Iphone')
# # SELECT * FROM products WHERE name LIKE 'Iphone%';
# Product.objects.filter(name__istartswith='Iphone')
# # SELECT * FROM products WHERE name ILIKE 'Iphone%';

# Product.objects.filter(name__contains='Iphone')
# # SELECT * FROM products WHERE name LIKE '%Iphone%';
# Product.objects.filter(name__icontains='Iphone')
# # SELECT * FROM products WHERE name ILIKE '%Iphone%';

# Product.objects.filter(name__endswith='Iphone')
# # SELECT * FROM products WHERE name LIKE '%Iphone';
# Product.objects.filter(name__iendswith='Iphone')
# SELECT * FROM products WHERE name ILIKE '%Iphone';

# Product.objects.order_by('price')
# # SELECT * FROM products ORDER BY price ASC;

# Product.objects.order_by('-price')
# # SELECT * FROM products ORDER BY price DESC;

# Product.objects.only('name')
# SELECT name FROM products;

# Product.objects.only('name', 'price') #запрашивает указанные поля
# # SELECT name, price FROM products;

# Product.objects.defer('name', 'price') #исключает указанные поля
# # SELECT id, description, category_id FROM products;

# Product.objects.count()
# # SELECT COUNT(*) FROM products;

# Product.objects.filter(...).count()
# # SELECT COUNT(*) FROM products WHERE ...;

# Product.objects.create(name='Apple Iphone 12',
#                        description='awddwdawd',
#                        price=78000,
#                        category_id='phones')
# INSERT INTO products (name, description, price, category_id) VALUES \
    # ('Apple Iphone 12', 'dwadaafafaw', 78000, 'phones');

# Product.objects.bulk_create([
#     Product(...),
#     Product(...)
# ]) #множественное создание

# Product.objects.update(price=50000)
# # UPDATE products SET price=50000;

# Product.objects.filter(...).update(price=50000)
# #UPDATE products SET price=50000 WHERE ...;

# Product.objects.filter(id=1).update(price=50000)
# #UPDATE products SET price=50000 WHERE id=1;

# product = Product.objects.get(id=1)
# product.price = 50000
# product.save()

# Product.objects.delete()
# DELETE FROM products;

# Product.objects.filter(category_id='phones').delete()
# DELETE FROM products WHERE category_id = 'phones';

# Product.objects.filter(id=1).delete()
# DELETE FROM products WHERE id=1;

# product = Product.objects.get(id=1)
# product.delete()


'''related_name'''
# позволяет обращатьсяя из связанных объектов к тем, от которых эта связь создана (для обратного списка)
# releted_name - создает связь с обратной стороны
#cat = Category.objects.get(id=1)
# cat.posts.all() - получение всех постов, относящихся к данной категории.

'''related_query_name'''
# создает именованный атрибут, 
# который позволяет делать запросы с использованием метода perfeth_related - загружает связанные объекты (оптимизирует запросы в бд)
# cat.post.all()

# QuerySet - объект полученные из базы данных, благодаря maneger'y (objects)
# Manager - класс, пероставляет методы для доступа к ORM Django (отправляет запрос в бд)
# default - objects
# (обнавляем, получаем, удаляем, фильтруем данные из таблиц)