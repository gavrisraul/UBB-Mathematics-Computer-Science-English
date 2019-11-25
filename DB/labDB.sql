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
    fan INT(6) UNSIGNED NOT NULL,
    FOREIGN KEY (team) REFERENCES teams(id),
    FOREIGN KEY (fan) REFERENCES fans(id)
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

INSERT INTO coaches VALUES (1, 'aaa', '111', 1, 1);
INSERT INTO coaches VALUES (2, 'bbb', '222', 4, 2);
INSERT INTO coaches VALUES (3, 'ccc', '333', 3, 3);
INSERT INTO coaches VALUES (4, 'ddd', '444', 4, 4);

INSERT INTO player_overall VALUES ('99', '99', '99', 1);
INSERT INTO player_overall VALUES ('89', '67', '70', 2);
INSERT INTO player_overall VALUES ('30', '59', '41', 3);
INSERT INTO player_overall VALUES ('63', '30', '50', 1);
INSERT INTO player_overall VALUES ('42', '76', '77', 1);

-- data update
UPDATE player_overall SET strength='100' WHERE strength >= 80;
UPDATE shoes set player='3' where brand like '%Nike';

-- data deletion
DELETE FROM shoes where id BETWEEN 1 AND 2;

-- union
SELECT brand FROM shoes
WHERE  player='3' AND id IS NOT NULL
UNION
SELECT brand from balls
WHERE brand like '%Nike%' AND id IS NOT NULL ORDER BY brand DESC;

-- except
SELECT brand FROM balls
WHERE id IS NOT NULL
EXCEPT
SELECT brand from shoes
WHERE brand NOT LIKE '%Nike%';

-- intersect
SELECT DISTINCT brand FROM balls
INTERSECT
SELECT DISTINCT brand FROM shoes WHERE shoes.id IS NOT NULL OR shoes.id>1;

-- in
SELECT * FROM coaches WHERE id IN (1, 2);

-- exists
SELECT id FROM coaches WHERE EXISTS (select id FROM balls);

-- from subquery
select id from (select * from players where id>2) as tb;

--triple join
SELECT * FROM players INNER JOIN balls ON players.id=balls.id INNER JOIN shoes ON shoes.id=balls.id;
-- joins
SELECT * FROM players LEFT JOIN balls ON players.id=balls.id;
SELECT * FROM players RIGHT JOIN balls ON players.id=balls.id;
-- SELECT * FROM players FULL OUTER JOIN balls ON players.id=balls.id;

-- group by
SELECT * FROM players LEFT JOIN balls ON players.id=balls.id GROUP BY players.id, players.first_name;

SELECT players.id, AVG(players.id) AS average
FROM players LEFT JOIN balls ON players.id=balls.id
GROUP BY players.id HAVING average>2;

SELECT players.id, AVG(players.id) AS average
FROM players LEFT JOIN balls ON players.id=balls.id
GROUP BY players.id HAVING average IN ( SELECT id FROM balls ) ORDER BY id DESC;

-- others
-- SELECT TOP 3 * FROM coaches;
SELECT * from coaches LIMIT 3;


-- versioning mechanism
CREATE TABLE version (
    version_number INT(6) UNSIGNED
);

DELIMITER //
CREATE PROCEDURE versioning(IN ver INT(6))
BEGIN
    UPDATE version SET version_number=ver;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE V1()
BEGIN
    ALTER TABLE coaches ADD COLUMN nickname VARCHAR(15);
    CALL versioning(1);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE RV1()
BEGIN
    ALTER TABLE coaches DROP COLUMN nickname;
    CALL versioning(0);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE V2()
BEGIN
    DROP TABLE coaches;
    CREATE TABLE coaches (
        id INT(6) UNSIGNED,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        team INT(6) UNSIGNED NOT NULL,
        fan INT(6) UNSIGNED NOT NULL,
        FOREIGN KEY (team) REFERENCES teams(id),
        FOREIGN KEY (fan) REFERENCES fans(id)
    );
    CALL versioning(2);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE RV2()
BEGIN
    DROP TABLE coaches;
    CREATE TABLE coaches (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        team INT(6) UNSIGNED NOT NULL,
        fan INT(6) UNSIGNED NOT NULL,
        FOREIGN KEY (team) REFERENCES teams(id),
        FOREIGN KEY (fan) REFERENCES fans(id)
    );
    CALL versioning(1);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE V3()
BEGIN
    DROP TABLE coaches;
    CREATE TABLE coaches (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        team INT(6) UNSIGNED NOT NULL,
        fan INT(6) UNSIGNED NOT NULL,
        FOREIGN KEY (team) REFERENCES teams(id)
    );
    CALL versioning(3);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE RV3()
BEGIN
    DROP TABLE coaches;
    CREATE TABLE coaches (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        team INT(6) UNSIGNED NOT NULL,
        fan INT(6) UNSIGNED NOT NULL,
        FOREIGN KEY (team) REFERENCES teams(id),
        FOREIGN KEY (fan) REFERENCES fans(id)
    );
    CALL versioning(2);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE V4()
BEGIN
    DROP TABLE coaches;
    CALL versioning(4);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE RV4()
BEGIN
    CREATE TABLE coaches (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        first_name VARCHAR(30) NOT NULL,
        last_name VARCHAR(30) NOT NULL,
        team INT(6) UNSIGNED NOT NULL,
        fan INT(6) UNSIGNED NOT NULL,
        FOREIGN KEY (team) REFERENCES teams(id),
        FOREIGN KEY (fan) REFERENCES fans(id)
    );
    CALL versioning(3);
END //
DELIMITER ;

