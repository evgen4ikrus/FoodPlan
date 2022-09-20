# FoodPlan
Сервис с рецептами на каждый день
## Установка и запуск
* Скачайте код
* Установите зависимости:
```
pip install -r requirements.txt
```
* Создайте файл .env в корневой папке проекта, определите в файле переменные окружения. Пример содержимого файла .env:
```
SECRET_KEY=h7wfbk14otyo6qs-1l3^)i9h@(qo&fcfg=e6i@k*(nvg9^fg2f
DEBUG=True
ALLOWED_HOSTS=127.0.0.1
```
Примечание: SECRET_KEY - обязательно, у остальных заданы параметры по умолчанию (DEBUG = True, ALLOWED_HOSTS = ['127.0.0.1'])
* Примените миграции:
```
python manage.py migrate
```
* Запустите локальный сервер:
```
python manage.py runserver
```
* Перейдите по ссылке в командной строке