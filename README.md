# Shopping app
Shopping cart application build with flask and facebook react

## Installation
Inspired from https://github.com/cbalan/react-flask-todo-app

 * install python dependencies

        pip install -r requirements.txt

* install bower

        npm install -g bower

* install js dependencies

        bower install

* compile jsx files using [React tool](http://facebook.github.io/react/docs/tooling-integration.html#productionizing-precompiled-jsx) for development purpose

        jsx --watch static/js static/jsx

* run flask server

        python manage.py run

* locations:
    - shop app: http://127.0.0.1:5000
    - swagger.json: http://127.0.0.1:5000/swagger.json
    - api docs: http://127.0.0.1:5000/doc
