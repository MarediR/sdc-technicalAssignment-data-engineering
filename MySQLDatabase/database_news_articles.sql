CREATE DATABASE news;

use news;

CREATE TABLE sources(
    source_id varchar(200) not null AUTO_INCREMENT,
    source_name varchar(200),
    decsription varchar(200),
    source_url varchar(200),
    category varchar (200),
    source_language varchar(5),
    counrty varchar(2),
    PRIMARY KEY (source_id)
)