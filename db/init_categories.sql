drop table if exists categories;

CREATE TABLE categories (
    category_id serial PRIMARY KEY,
    category VARCHAR(255) NOT NULL UNIQUE);

INSERT INTO categories
VALUES
(0, 'Админ'),
(1, 'Обыватель'),
(2, 'Студент'),
(3, 'Дизайнер');