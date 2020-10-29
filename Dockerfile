FROM python:3.8.3
#set envionment variables
ENV PYTHONUNBUFFERED 1

# run this before copying requirements for cache efficiency
RUN pip install --upgrade pip

RUN mkdir /app_grupo2
WORKDIR /app_grupo2
COPY . /app_grupo2

RUN pip install -r requirements.txt


RUN mkdir /data
COPY db.sqlite3 /data

CMD ["python", "./tpingweb/manage.py", "makemigrations"]
CMD ["python", "./tpingweb/manage.py", "migrate"]
CMD ["python", "./tpingweb/manage.py", "runserver", "0.0.0.0:8000"]