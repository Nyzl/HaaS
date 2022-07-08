FROM python:3.9

LABEL version="1.0"
LABEL maintainer="Ian Ansell"

RUN pip install --upgrade pip

COPY . /haas
WORKDIR /haas

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod 444 *.py
RUN chmod 444 requirements.txt

ENV PORT 8080

ENV GUNICORN_CMD_ARGS="--timeout 900 --graceful-timeout 900 --workers 2"
EXPOSE 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 wsgi:app