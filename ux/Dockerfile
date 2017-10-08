FROM node:8

# node image already has a regular user called node
ENV USR node
ENV HOME /home/$USR

WORKDIR $HOME
COPY . .
RUN chown -R 1000:1000 .

USER $USR
RUN yarn --non-interactive --no-progress --no-lockfile && \
  yarn cache clean
