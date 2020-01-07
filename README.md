# Pizza-task - тестовое задание <br>
Веб сайт с бекендом на django упакованный в docker контейнер <br>
Для запуска проекта необходимо установить docker и docker-compose <br>
В консоли папки проекта docker-compose up -d --build <br>
Соберется контейнер и запустится сайт на http://0.0.0.0:2000/<br>

База проекта заполненна товарами db.sqlite3. Удаление базы приведет к удалению товаров<br> 

Товары можно добавлять через админку на сайту http://0.0.0.0:2000/admin<br>
Чтобы воспользоваться админкой нужно войти <br>
- login qwil <br>
- password qwil<br>

Группы в админке/модели в 'pizza/models.py'
- Product pizzas
- Product classicss	
- Product drinkss	
- Product specialss

