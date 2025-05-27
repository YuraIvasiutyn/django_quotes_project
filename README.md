# django_quotes_project

1. Створюємо проект і переходимо в його директорію
django-admin startproject quotes_project
cd quotes_project 

2. Встановлюжмо необхідні бібліотеки
pip install django
pip install psycopg2-binary

3. Сворюємо наш додаток та додаємо в settings.py його назву (INSTALLED_APPS)
python3 manage.py startapp qoutes_app

4. Ставимо локальну базу даних postgresql
docker run --name noteapp-postrges -p 5431:5432 -e POSTGRES_PASSWORD=567234 -d postgres

5. у файлі quotes_project/settings.py змінюємо підключення до бази даних на нашу локальну базу в докері (DATABASES)

6. застосовуємо міграцію та сворюємо суперкористувача (адміна)
python3 manage.py migrate
python3 manage.py createsuperuser

7. Виконуємо перший запуск застосунку на перевірку коректності
python3 manage.py runserver
Шлях до застосутнку - http://127.0.0.1:8000/
Шлях до адмін-панелі - http://127.0.0.1:8000/admin/login/?next=/admin/


8. В файлі qoutes_app/models.py додаємо наші моделі для представлення об'єктів та виконуємо міграцію
python3 manage.py makemigrations
python3 manage.py migrate

9. В файлі qoutes_app/admin.py реєструємо наші моделі

10. в каталозі qoutes_app створюємо templates/qoutes_app/index.html для головної стрінки

11. В файлі qoutes_app/views.py додамо функцію для обробки запитів до застосунку

12. В файлі quotes_project/urls.py додаємо маршрутизацію до нашого застосунку

13. Створюємо файл qoutes_app/urls.py та додаємо маршрут до головної сторінки я views.main

14. Створюємо базовий шаблон та шаблон тегів в html qoutes_app/tepmlates/qoutes_app/base.html i tag.html a також
qoutes_app/static/qoutes_app/style.css

15. Створюємо файл qoutes_app/forms.py яка відповідає за перевірку даних

16. В файлі qoutes_app/views.py додаємо обробку маршрута tag

17. В файлі qoutes_app/urls.py додаємо наш маршрут з обробником

18. Створюємо шаблон html з доданям цитат qoutes_app/templates/qoutes_app/quotes.html

19. Створюємо форму для цитат всередині файлу forms.py

20. Додаємо функцію в views.py для обробки маршрутів та маршрут в urls.py

21. Для додання авторів використовуємо такий самий підхід як вище

22. Для висвітлення цитат з авторами і тегами змінимо нашу функцію main в qoutes_app/views.py

23. Створимо проект users для аутентифікації і авторизації
python3 manage.py startapp users

24. В файлі quotes_project/urls.py додамо маршрут до url нашого проекту користувачів

25. Створємо файл users/forms.py та додаємо реєстраційну форму на базі django

26. В файлі users/views.py додаємо функцію для реєстрації користувача та запису в базу даних

27. Створюємо html users/templates/users/signup.html

28. Створюємо маршрутизацію до реєстрації users/urls.py

29. Аутентифікація користувача та вихід виконуємо ідентично до реєстрації (ті ж самі файли)

30. Додаємо користувача до моделей бази даних qoutes_app/models.py

31. Додаємо по тому ж принципу вихід з застосунку

32. Створюємо профіль користувача

---
1. pip install django-environ
2. 




