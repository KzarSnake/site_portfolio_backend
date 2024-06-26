# Бэкенд для сайта-портфолио

## Описание
В репозитории содержится основной бэкенд и упрощенный фронтенд для сайта-портфолио. Может использоваться как основа для создания виртуального портфолио под нужды различных профессий: дизайнеры, фотографы, архитекторы, разработчики, крафтеры. При необходимости функционал может быть расширен.
Основной функционал сайта покрыт тестами.

**Структура сайта:**
- административная панель для редактирования информации на сайте: проекты (название, описание, изображения), категории проектов (название), услуги (название, описание, цены), информация об авторе (текст, изображение), контакты (телефон, email, описание);
- главная страница сайта с примерами проектов;
- портфолио с проектами;
- страница об авторе с возможностью размещать фото;
- услуги автора;
- контактные данные автора и форма обратной связи с отсылкой письма на почтовый сервис автора.

## Стэк технологий:

- Python 3.10
- Django 3.2
- SQLite3

## Подготовка к запуску:

**Клонируйте репозиторий:**

```
git clone https://github.com/KzarSnake/site_portfolio_backend.git
```

**Установите и активируйте виртуальное окружение:**

```
python -m venv venv
source venv/Scripts/activate
```

**Установите зависимости из файла requirements.txt:**

```
pip install -r requirements.txt
```

**Выполните миграции:**
```
python manage.py migrate
```

**Создайте файл .env**
Пример заполнения файла:
```
SECRET_KEY=YOUR_KEY_HERE
```

## Запуск:
Находясь в директории проекта c файлом manage.py, выполните в терминале команду:

```
python manage.py runserver
```


## Автор проекта:

[Денис Свашенко](https://github.com/KzarSnake)
