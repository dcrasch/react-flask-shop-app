# react-flask-shop-app
Shop build with reactjs and flask

## Installation

```
poetry install
poetry shell
flask --app rfs initdb
cd frontend
npm install
```

```
poetry add connexion[swagger-ui]  -D --allow-prereleases
```

## Running api server
```
poetry shell
flask --app rfs run
```

or 

```poetry run flask --app rfs run```

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


## Poetry

### Create requirements.txt without hashes
```
poetry export --without-hashes --format=requirements.txt > requirements.txt
```

### Install pre-release version of package
```
poetry add connexion --allow-prereleases
```
