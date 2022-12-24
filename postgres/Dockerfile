FROM postgres:latest
ENV POSTGRES_PASSWORD=dieppiep
ENV POSTGRES_USER=admin
ENV POSTGRES_DB=scores
COPY init.sql /docker-entrypoint-initdb.d/init.sql
