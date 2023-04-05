FROM python:3.7-bullseye
WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN python3 -m flask --app rfs initdb
RUN pip3 install connexion[swagger-ui]
CMD [ "python3", "-m" , "flask", "--app","rfs", "run", "--host=0.0.0.0"]
