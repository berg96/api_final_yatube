### Описание

Учебный проект API Yatube v1


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

git clone https://github.com/berg96/api_final_yatube.git
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:

python -m venv venv
source venv/Scripts/Activate
```
Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:

python manage.py migrate
```
Запустить проект:

python3 manage.py runserver


### Примеры запросов

GET: http://127.0.0.1:8000/api/v1/posts/{id}/
Response:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}

POST: http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
Payload:
{
  "text": "string"
}
Response:
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}

# Более подробно в документации 
http://127.0.0.1:8000/redoc/
