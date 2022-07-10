CREATE DATABASE news;

use news;

CREATE TABLE sources(
    source_id varchar(200) not null ,
    source_name varchar(200),
    decsription varchar(200),
    source_url varchar(200),
    category varchar (200),
    source_language varchar(5),
    counrty varchar(2),
    PRIMARY KEY (source_id)
);

CREATE TABLE toparticles(
    source varchar(200) not null,
    author varchar(200),
    title varchar(200),
    source_description varchar(200),
    source_url varchar(200),
    publishedAt varchar (200),
    content varchar(200),
    PRIMARY KEY (source)
);


CREATE TABLE articles(
    source varchar(200) not null,
    author varchar(200),
    title varchar(200),
    source_description varchar(200),
    source_url varchar(200),
    url_to_image varchar(200),
    publishedAt varchar (200),
    content varchar(200),
    PRIMARY KEY (source)
);
