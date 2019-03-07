### Django REST Framework API by Example

![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

![django](https://www.pythonanywhere.com/user/craigderington/files/home/craigderington/newblog2/static/images/drfexample-location-list.png?raw=true "Django REST Framework by Example")

Example APIs using Django 2.1.7 + Django REST Framework 3.9.2 + Swagger UI 2.2.0

This DRF repository contains several example APIs for various applications types.

Data Models:

1.  Bookmarks
2.  Code Snippets
3.  ToDos
4.  Bookmarks
5.  Geolocation by IP Address


##### Installation

```
$ mkdir django-drf-by-example
$ cd django-drf-by-example
$ virtualenv .env --python=python3.6
$ source .env/bin/activate
(.env) $ pip3 install -r requirements.txt
(.env) $ cd drfexample
(.env) ~drfexample$ python manage.py makemigrations
(.env) ~drfexample$ python manage.py migrate
... runs migrations ...
(.env) ~drfexample$ python manage.py runserver 8888
```








