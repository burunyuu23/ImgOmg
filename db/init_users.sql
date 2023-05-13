drop table if exists users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    login VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    patronymic VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    birthdate DATE NOT NULL,
    category numeric NOT NULL DEFAULT 2);

INSERT INTO users (login, password, name, surname, patronymic, email, birthdate, category)
VALUES
('test', '123',
 'Коля', 'ЮГ', '404',
 'ezzfvkoko@gmail.com', '2003-05-30', 0);


INSERT INTO users (login, password, name, surname, patronymic, email, birthdate)
VALUES
('nikolay228', '123',
 'Коля', 'ЮГ', '404',
 'pipuk@gmail.com', '2003-05-30');