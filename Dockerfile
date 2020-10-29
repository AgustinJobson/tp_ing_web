FROM python:3.8.5

RUN mkdir /app_grupo2
WORKDIR /app_grupo2

COPY . /app_grupo2

RUN pip install -r requirements.txt

ENV IS_DOCKER = True


RUN mkdir /data
COPY tpingweb/db.sqlite3 /../data

CMD ["sh","-c","/app_grupo2/start.sh"]
