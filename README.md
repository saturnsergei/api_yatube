# Yatube API
### Описание
Учебный проект: REST API для сервиса Yatube

### Эндпоинты

- `api/v1/api-token-auth/ (POST)` - получить токен
- `api/v1/posts/ (GET, POST)` - получить список всех постов или создать новый пост
- `api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE)` -  получить/редактировать/удалить пост по id
- `api/v1/groups/ (GET)` -  получить список групп
- `api/v1/groups/{group_id}/ (GET)` - получить информацию о группе по id
- `api/v1/posts/{post_id}/comments/ (GET, POST)` - получить список всех комментариев поста, создать новый комметарий
- `api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE)` - получить/редактировать/ удалить комментарий
    
### Запуск

Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
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
