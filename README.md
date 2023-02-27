# Ссылка на тестирование проекта на серверах pythonanywhere: 
   http://chingizpain.pythonanywhere.com/
   
### Логин и пароль от суперпользователя:
    username: root
    password: root

# Настройка проекта:
## Для начала делаем клон ветки:

 	 $ git clone git@github.com:Chingiz-Almukhan/e-shop_django_app.git
  
## После переходим в деректорию проекта:

   $ cd e-shop_django_app && cd core
	
## Запуск приложения с помощью докера:

   $ docker-compose up -d

## Стандартный запуск:
### Устанавливаем виртуальное окружение

	 $ python3 -m venv venv
### Активируем его

	 $. venv/bin/activate
### После устанавливаем необходимые зависимости 

	 $ pip install -r requirements.txt
### Делаем миграцию

 	 $ python3 manage.py migrate
 ### После ставим дамп бд
 
 	 $ python3 manage.py loaddata fixtures/dump.json
 ## После чего запускаем приложение
 
 	 $ python3 manage.py runserver
	
