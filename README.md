# Setup

#### [Preferred way is to use virtual environment](https://docs.python.org/3/library/venv.html)  
1. use git clone  
```git clone https://github.com/LukaszMazurek/recrutation.git```
2. create and activate virtual environment [venv](https://docs.python.org/3/library/venv.html) 
3. use pip to install requirements.txt  
```pip install -r requirements.txt```
4. on local version you have to setup sqlite with commands  
```python manage.py makemigrations```  
```python manage.py migrate```
5. create superuser  
```python manage.py createsuperuser```
6. run server on your local machine  
```python manage.py runserver```