#!/usr/bin/env bash
# build.sh

# Установка зависимостей
pip install -r requirements.txt

# Сбор статики
python manage.py collectstatic --noinput

# Применение миграций (можно и в start command)
# python manage.py migrate
