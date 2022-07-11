CREATE DATABASE news;

use news;

CREATE TABLE sources(
    source_id varchar(200) not null ,
    source_name varchar(200),
    source_description varchar(1000),
    source_url varchar(500),
    category varchar (200),
    source_language varchar(5),
    country varchar(2),
    PRIMARY KEY (source_id)
);

CREATE TABLE toparticles(
    author varchar(200),
    title varchar(200),
    source_description varchar(1000),
    source_url varchar(500),
    url_to_image varchar(500),
    publishedAt varchar (200),
    content varchar(1000)
);


CREATE TABLE articles(
    author varchar(200),
    title varchar(200),
    source_description varchar(1000),
    source_url varchar(500),
    url_to_image varchar(500),
    publishedAt varchar (200),
    content varchar(1000)
);
