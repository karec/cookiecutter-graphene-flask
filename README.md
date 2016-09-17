# cookiecutter-graphene-flask

Very basic cookiecutter recipe for graphene application using flask and sqlalchemy

## Use it

```
$ pip install cookiecutter
$ cookiecutter gh:karec/cookiecutter-graphene-flask
```

You will be asked for basic project informations.

## Initialize project

This recipe provide you basics elements to start a project with some examples and fixtures, so you need to init them :

```
$ pip install -r requirements.txt --pre
$ python manage.py db upgrade
$ python manage.py run
```

At this point a Flask debug server should be running on port 5000 and a `graphql.db` file should has been created on your project folder with basic fixtures.

Graphql endpoint is by default configured on `/` endpoint

## Feaures

* Flask application factory configured and ready to be extended
* Graphene endpoint configured inside a blueprint
* Already configured db extension with flask-sqlalchemy
* Minimal amount of fixtures to test graphql with sqlalchemy
* Already configured logger
* Basic graphene schema declaration for example
