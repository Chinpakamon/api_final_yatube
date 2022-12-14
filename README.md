## Проект API для YaTube
### Описание 
API для YaTube представляет собой проект соц.сети, в которой реализованы возможности публикации поста, комментарирования и подписки.
### Технологии
Python 3.7, Django, Django Rest Framework, JWT + Djoser
### Запуск проекта 
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Chinpakamon/api_final_yatube.git
cd api_final_yatube
```
Создать и активировать виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
### Пример запросов к API
Получение публикаций (GET запрос):
```
Запрос:

api/v1/posts/

Ответ:

{
"count": number,
"next": URL,
"previous": URL,
"results": [
{}
]
}
```

Добавление комментариев (POST запрос):
```
Запрос:

api/v1/posts/{post_id}/comments/

Ответ:

{
"text": "string"
}
```
Обновление комментария (PUT запрос):
```
Запрос:

api/v1/posts/{post_id}/comments/{id}/

Ответ:

{
"text": "string"
}

```

Частичное обновление комментария (PATCH запрос):
```
Запрос:

api/v1/posts/{post_id}/comments/{id}/

Ответ:

{
"text": "string"
}

```

УДаление комментария (DELETE запрос):
```
Запрос:

api/v1/posts/{post_id}/comments/{id}/

Ответ:

{
"detail": "Удачное выполнение запроса."
}
```
