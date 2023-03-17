CREATE TABLE users
(
    "id"          SERIAL PRIMARY KEY,
    "telegram_id" bigint UNIQUE NOT NULL,
    "firs_name"   varchar(25)   NOT NULL,
    "last_name"   varchar(25)
);


CREATE TABLE information
(
    "id"   SERIAL PRIMARY KEY,
    "text" varchar(100) UNIQUE ,
    "link" varchar(100)
);


CREATE TABLE user_link
(
    id             serial primary key ,
    user_id        bigint references users (id),
    information_id int2 references information (id)

);
ALTER TABLE user_link
    ADD UNIQUE (user_id, information_id);



