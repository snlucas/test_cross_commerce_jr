# test_cross_commerce_jr
Teste para vaga de dev. Elixir Jr. na Cross Commerce.

## First Step: Extract Data
- [x] Get the whole data from the first page.
- [x] Get data from each page 'til empty list.
 - [ ] Improve with parallel requests.

## Second Step: Transform
- [x] Implement a sort algorithm.
 - [ ] Improve with a middle or randomic pivot.
 - [ ] Improve with a quick sort dual pivot implementation.
- [x] Sort data.

## Third Step: Load
- [x] Expose a REST API with processed data.

## How to Run
### Run Using Docker Compose
```shell
$ sudo docker-compose run web django-admin startproject test_cross_commerce .
$ sudo chown -R $USER:$USER .
$ docker-compose up
```

### Run Using Python
**Obs.**, First you should use a *Virtual Environment*.
```shell
$ pip install -r requirements.txt
$ python manage.py runserver
```
The API is being served at 127.0.0.1:8000/api

### Run Tests
**Django**
```shell
$ python manage.py test
```
**Python utils dir**
```shell
$ python -m unittest test_cross_commerce/utils/tests_quick_sort.py
```