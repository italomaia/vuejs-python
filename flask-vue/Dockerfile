FROM python:3.6

ENV USR usr
ENV HOME /home/$USR
RUN groupadd -g 1000 -r $USR && \
  useradd -u 1000 -d $HOME -m -r -g $USR $USR

WORKDIR $HOME
COPY . $HOME
RUN chown -R 1000:1000 .
RUN pip install --no-cache-dir\
  eventlet==0.21.0\
  flask==0.12.2\
  flask-admin==1.5.0\
  flask-jsglue==0.3.1\
  flask-marshmallow==0.8.0\
  flask-migrate==2.1.1\
  flask-restful==0.3.6\
  flask-sqlalchemy==2.3.1\
  flask-socketio==2.9.2\
  flask-debugtoolbar==0.10.1\
  marshmallow-sqlalchemy==0.13.1

# make sure user running the process is a regular user
USER $USR
EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0"]
