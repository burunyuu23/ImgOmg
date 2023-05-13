drop table if exists categories;

CREATE TABLE categories (
    category_id serial PRIMARY KEY,
    category VARCHAR(255) NOT NULL UNIQUE);

INSERT INTO categories (category)
VALUES
('Админ'),
('Обыватель'),
('Студент'),
('Дизайнер');