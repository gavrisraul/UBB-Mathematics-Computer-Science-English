create database football_statistics;
use football_statistics;


-- create tables with relations one to one, one to many, many to many
create table teams (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    title VARCHAR(30) NOT NULL
);

-- a team has many players but a player plays in one team
create table players (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    team INT(6) UNSIGNED NOT NULL,
    FOREIGN KEY (team) REFERENCES teams(id)
);

create table balls (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(30) NOT NULL
);

create table fans (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(30) NOT NULL
);

-- many fans buy many balls and many balls are bought by many fans
create table balls_fans_relation (
    bid INT(6) UNSIGNED,
    fid INT(6) UNSIGNED,
    FOREIGN KEY (bid) REFERENCES balls(id),
    FOREIGN KEY (fid) REFERENCES fans(id),
    UNIQUE (bid, fid)
);

create table shoes (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(30) NOT NULL,
    player INT(6) UNSIGNED NOT NULL,
    FOREIGN KEY (player) REFERENCES players(id)
);

create table coaches (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    team INT(6) UNSIGNED NOT NULL,
    FOREIGN KEY (team) REFERENCES teams(id)
);

create table player_overall (
    strength VARCHAR(30) NOT NULL,
    agility VARCHAR(30) NOT NULL,
    overall VARCHAR(30) NOT NULL,
    player INT(6) UNSIGNED NOT NULL,
    FOREIGN KEY (player) REFERENCES players(id)
);

-- data insertion
INSERT INTO teams VALUES (1, 'Barcelona', '1stPlace');
INSERT INTO teams VALUES (2, 'Real Madrid', '2ndPlace');
INSERT INTO teams VALUES (3, 'Chelsea', '3rdPlace');
INSERT INTO teams VALUES (4, 'PSG', '4thPlace');
INSERT INTO teams VALUES (5, 'CFR', '5thPlace');
INSERT INTO teams VALUES (6, 'UCJ', '6thPlace');

INSERT INTO players VALUES(1, 'Banel', 'Nicolita', 1);
INSERT INTO players VALUES(2, 'Cristiano', 'Ronaldo', 2);
INSERT INTO players VALUES(3, 'Lionel', 'Messi', 1);
INSERT INTO players VALUES(4, 'Sergio', 'Ramos', 4);
INSERT INTO players VALUES(5, 'Maradona', 'The Great', 6);
INSERT INTO players VALUES(6, 'Ronaldinho', 'Second Great', 5);
INSERT INTO players VALUES(7, 'Mutu', 'Adrian', 3);
INSERT INTO players VALUES(8, 'Puyol', 'Spain', 2);

INSERT INTO balls VALUES (1, 'Nike');
INSERT INTO balls VALUES (2, 'Adidas');
INSERT INTO balls VALUES (3, 'Puma');
INSERT INTO balls VALUES (4, 'Kappa');

INSERT INTO fans VALUES (1, 'Romania');
INSERT INTO fans VALUES (2, 'Spain');
INSERT INTO fans VALUES (3, 'Italy');
INSERT INTO fans VALUES (4, 'Russia');
INSERT INTO fans VALUES (5, 'America');

INSERT INTO balls_fans_relation VALUES (1, 1);
INSERT INTO balls_fans_relation VALUES (1, 2);
INSERT INTO balls_fans_relation VALUES (1, 3);
INSERT INTO balls_fans_relation VALUES (2, 2);
INSERT INTO balls_fans_relation VALUES (4, 3);

INSERT INTO shoes VALUES (1, 'Nike', 1);
INSERT INTO shoes VALUES (2, 'Puma', 2);
INSERT INTO shoes VALUES (3, 'Puma', 3);
INSERT INTO shoes VALUES (4, 'Kappa', 1);

INSERT INTO coaches VALUES (1, 'aaa', '111', 1);
INSERT INTO coaches VALUES (2, 'bbb', '222', 4);
INSERT INTO coaches VALUES (3, 'ccc', '333', 3);
INSERT INTO coaches VALUES (4, 'ddd', '444', 4);

INSERT INTO player_overall VALUES ('99', '99', '99', 1);
INSERT INTO player_overall VALUES ('89', '67', '70', 2);
INSERT INTO player_overall VALUES ('30', '59', '41', 3);
INSERT INTO player_overall VALUES ('63', '30', '50', 1);
INSERT INTO player_overall VALUES ('42', '76', '77', 1);
