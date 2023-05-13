drop table if exists users;

CREATE TABLE users (
    user_id serial PRIMARY KEY,
    login VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    patronymic VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    birthdate DATE NOT NULL,
    category serial);


INSERT INTO users
VALUES
(0, 'test', '123',
 'Коля', 'ЮГ', '404',
 'ezzfvkoko@gmail.com', '2003-05-30', 0);