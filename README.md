# Shopping app
Shopping cart application build with flask and facebook react

## Installation
Inspired from https://github.com/MediaSapiens/flamaster, https://github.com/limelights/todo-reflux.git, https://github.com/coinbolt/catshop and https://github.com/chadpaulson/react-isomorphic-video-game-search
 * install python dependencies

        pip install -r requirements.txt

 * install bower

        npm install -g bower

 * install js dependencies

        bower install

* run flask server

        python manage.py run

* install database and optional data

  	  python manage.py create_all

	  python manage.py create_data

* locations:
    - shop app: http://127.0.0.1:5000
    - swagger.json: http://127.0.0.1:5000/swagger.json (todo)
    - api docs: http://127.0.0.1:5000/doc (todo)

* demo:
    - http://127.0.0.1:5000/products/
    - http://127.0.0.1:5000/admin/
    
    