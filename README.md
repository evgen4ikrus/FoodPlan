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
TELEGRAM_TOKEN=<your_token>
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

### Запуск телеграм-бота
```
python manage.py start_bot
```

### Загрузка данных
```
python manage.py load_recipes -p [first_page_number] [second_page_number]
```
* Скрипт загружает рецепты с сайта eda.ru. 
  `first_page_number` и `second_page_number` - диапазон страниц.
 Рецепты перезаписываются в `data_recipes.json`
 ### Формирование базы данных
 ```
 python manage.py update_db
 ```
 Из сформированного на предыдущем этапе файла `data_recipes.json` рецепты запишутся в базу данных.
