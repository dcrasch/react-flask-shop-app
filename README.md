# react-flask-shop-app
Shop build with reactjs and flask

## Installation

```
pipenv install
pipenv shell
flask --app rfs initdb
cd frontend
npm install
```

```
pipenv install connexion[swagger-ui]
```

## Running api server
```
pipenv shell
flask --app rfs run
```

or 

```pipenv run flask --app rfs run```

## Running frontend

```
cd frontend
npm run dev
```

## Swagger UI
http://127.0.0.1:5000/ui/


## Docker

```
docker build --tag python-docker .
docker run -d -p 5000:5000 python-docker
```
