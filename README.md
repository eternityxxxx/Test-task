## Django auth task
Система регистрации и авторизации пользователей

#### Роуты
---
1. '/' - домашняя страница
2. '/accounts/login' - страница входа
3. '/accounts/signup' - страница регистрации
4. '/accounts/logout' - выход

#### Админка
---
Логин: admin
Пароль: admin

#### Как запустить проект?
---
1. Создать новую директорию под проект и перейти в нее
```
mkdir название_директории
cd название_директории
```
2. Создать виртуальное окружение
```
python -m venv название_окружения/либо '.'
```
3. Активировать виртуальное окружение
```
cd название_окружения/Scripts
activate
```
4. Перейти в папку с проектом и установить зависимости
```
cd auth_task
pip install -r requirements.txt
```
5. Запустить сервер
```
python manage.py runserver
```
