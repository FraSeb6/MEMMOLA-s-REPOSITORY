create user dse with password 'test';
create database imdbdse with owner dse;
--database have different multiple schemas
-- public
-- pg_restore
-- imdb: you'll find this schema by importing our database, the oe that we'll use

-- A DATABSE IS A COLLECTION OF TABLES THAT DESCRIBE A SPECIFIC KIND OF OBJECT
-- A SCHEMA: REFERS TO THE SET OF ATTRIBUTES (LIKE YEAR, ID...) with related contraints of table
-- in sql, DDL refers to DATA DEFINITION LANGUAGE
create table name;
