# YSTU Basketball Tournament Site :basketball:
Доступ к админке 127.0.0.1:8000/admin
Username: YSTUClassic
Password: NoWaying

# Развертывание
Скачиваем репозиторий, если на компьютере установлен гит, то в выделенной под него папке с помощью консоли прописываем:
```git clone -b Backend https://github.com/Delmark/YSTUTournamentSite.git```  

После установки репозитория у себя на компьютере, необходимо в консоли в директории с репозиторием создать виртуальное окружение:
```python -m venv BasketballBackend``` 

После установки виртуального окружения необходимо запустить его, для этого требуется зайти в папку Scripts и запустить один из активаторов
 
```cd Scripts``` 

```activate.bat```
 
Если перед указателем директории появилось название вирутального окружение, значит оно успешно запущенно.
Требуется далее установить все необходимые модули, для этого возвращаемся в главную директорию вирутального окружения и прописываем ```pip install -r requirements.txt```
 
Можно запускать сайт, для этого заходим в проект.  

```cd DBTestModels```
Для запуска сервера необходимо прописать:  

```py manage.py runserver```
 
В случае запуска без ошибок можно заходить на сайт по адресу 127.0.0.1:8000.