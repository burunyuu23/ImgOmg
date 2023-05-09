drop table if exists test;

CREATE TABLE test (
    user_id serial PRIMARY KEY,
    name VARCHAR(255) NOT NULL);

INSERT INTO test
VALUES
(0, 'test'),
(1, 'test2'),
(2, 'test3');