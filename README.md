### Django REST Framework API by Example


Example APIs using Django 2.1.7 + Django REST Framework 3.9.2 + Swagger UI 2.2.0

This DRF repository contains several example APIs for various applications types.

Data Models:

1.  Bookmarks
2.  Code Snippets
3.  ToDos
4.  Bookmarks
5.  Locations


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

##### Usage

```
curl -i http://127.0.0.1:8888/locations/geolocate/<str:ip_addr>
```






