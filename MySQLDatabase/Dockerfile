FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=root

COPY ./database_news_articles.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

