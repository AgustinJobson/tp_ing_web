FROM python:3.8.5
#set envionment variables
ENV PYTHONUNBUFFERED 1

# run this before copying requirements for cache efficiency
RUN pip install --upgrade pip

RUN mkdir /app_grupo2
WORKDIR /app_grupo2

COPY . /app_grupo2

RUN pip install -r requirements.txt


ENV IS_DOCKER = True

RUN mkdir /data

CMD ["python", "tpingweb/manage.py", "runserver", "0.0.0.0:8000"]
