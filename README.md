# ToDo

Простое приложение ToDo, в котором зарегистрированные пользователи имеют 
возможность добавлять, редактировать и удалять 
задачи, также присутствует флаг выполнения задачи
***

## Стек технологий

Python 3.10.1, Django 4.0.4, Django REST Framework 
3.13.1, React 18.1.0
***

## Как начать

Необходимо скопировать репозиторий на свой локальный компьютер. Для этого перейти в каталог (например, рабочий стол)
```
cd desktop
```

и выполнить команду
```
git clone https://github.com/rufreedomman/todo_drf_react
```
### Backend
Открыть проект в IDE в новом виртуальном окружении (например, venv), 
активировать его. 
Перейти в каталог /backend/ и скопировать необходимые пакеты, указанные в файле requirements.txt
```
source venv/bin/activate
cd backend
pip install -r requirements.txt
```

Создать файл .env в директории /backend/ с содержанием:
```
SECRET_KEY=любой_секретный_ключ_на_ваш_выбор
DEBUG=False
ALLOWED_HOSTS=*,или,ваши,хосты,через,запятые,без,пробелов
```

Выполнить миграцию
```
python manage.py migrate
```

и запустить локальный сервер
```
python manage.py runserver
```

### Frontend
Открыть проект в новой IDE. Перейти в каталог /frontend/. Установить 
зависимости и запустить сервер
```
cd frontend
npm install
npn start
```

[![Screenshot-2022-05-16-at-10-40-27.png](https://i.postimg.cc/5NfsGhBS/Screenshot-2022-05-16-at-10-40-27.png)](https://postimg.cc/s10PG00M)