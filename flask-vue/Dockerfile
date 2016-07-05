FROM python:latest

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN apt-get update && \
    apt-get install -y nodejs npm &&\
    rm -rf /var/lib/apt/lists/*

RUN npm install coffee-script
RUN ln -s /usr/bin/nodejs /usr/bin/node


COPY ./ /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements/dev.txt
RUN python manage.py db-create
ENTRYPOINT python manage.py runserver
