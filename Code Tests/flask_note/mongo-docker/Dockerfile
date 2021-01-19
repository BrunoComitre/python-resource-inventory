FROM mongo:4.2.8

ENV MONGO_INITDB_ROOT_USERNAME admin
ENV MONGO_INITDB_ROOT_PASSWORD admin-password
ENV MONGO_INITDB_DATABASE notes

ADD mongo-init.js /docker-entrypoint-initdb.d/
