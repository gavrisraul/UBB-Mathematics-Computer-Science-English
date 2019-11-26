-- Setup the database
CREATE database lab3;
USE lab3;


---- Create the tables
CREATE TABLE dbo.house (
	pk_house_id VARCHAR(100) PRIMARY KEY
);


CREATE TABLE dbo.dog_house (
	pk_house_id INT PRIMARY KEY,
	material NVARCHAR(30) -- make this a choice? wood / metal / concrete / etc
);


CREATE TABLE dbo.person (
	pk_person_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	name NVARCHAR(255) NOT NULL,
	email NVARCHAR(255),
	-- Many persons can stay in one house
	fk_house VARCHAR(100) FOREIGN KEY REFERENCES house(pk_house_id)
);


CREATE TABLE dbo.dog (
	pk_dog_id INT PRIMARY KEY,
	name NVARCHAR(255) NOT NULL,
	birthday DATE,
	-- One dog has one house so we have a one to one relation!
	fk_dog_house INT UNIQUE FOREIGN KEY REFERENCES dog_house(pk_house_id),
	-- Many dogs can belong to one owner so one to many 
	fk_owner INT FOREIGN KEY REFERENCES person(pk_person_id),
	-- Many dogs can stay in one house
	fk_house VARCHAR(100) FOREIGN KEY REFERENCES house(pk_house_id)
);


CREATE TABLE dbo.cat (
	pk_cat_id INT IDENTITY(1,1) PRIMARY KEY,
	name NVARCHAR(100),
	-- Many cats can stay in one house
	fk_house VARCHAR(100) FOREIGN KEY REFERENCES house(pk_house_id),
);


CREATE TABLE dbo.dog_vs_cat (
	dog_id INT FOREIGN KEY REFERENCES dog(pk_dog_id),
	cat_id INT FOREIGN KEY REFERENCES cat(pk_cat_id),
	CONSTRAINT hate_relation PRIMARY KEY (dog_id,cat_id),
);


-- simple table, no relations, no pk
CREATE TABLE dbo.street (
	name VARCHAR(123) NOT NULL,
	len INT
);


-- Insert some data!
INSERT INTO dog_house VALUES (1, 'wood');
INSERT INTO dog_house VALUES (2, 'wood');
INSERT INTO dog_house VALUES (3, 'metal');
INSERT INTO dog_house VALUES (4, 'metal');
INSERT INTO dog_house VALUES (5, 'metal');
INSERT INTO dog_house VALUES (6, 'diamonds');
INSERT INTO dog_house VALUES (7, 'platinum');
INSERT INTO dog_house VALUES (8, 'red diamonds');
INSERT INTO dog_house VALUES (9, 'blue diamonds');

INSERT INTO house VALUES ('house 1');
INSERT INTO house VALUES ('house 2');
INSERT INTO house VALUES ('house 3');
INSERT INTO house VALUES ('house 4');
INSERT INTO house VALUES ('house 5');
INSERT INTO house VALUES ('house 6');

INSERT INTO person VALUES ('person 1', 'email_1@gmail.com', 'house 6');
INSERT INTO person VALUES ('person 2', 'email_2@gmail.com', 'house 5');
INSERT INTO person VALUES ('person 3', 'email_3@gmail.com', 'house 4');
INSERT INTO person VALUES ('person 4', 'email_4@gmail.com', 'house 3');
INSERT INTO person VALUES ('person 5', 'email_5@gmail.com', 'house 2');
INSERT INTO person VALUES ('person 6', 'email_6@gmail.com', 'house 1');

INSERT INTO dog VALUES (1, 'dog 1', '2001-01-01', 1, 3, 'house 1');
INSERT INTO dog VALUES (2, 'dog 2', '2001-01-01', 4, 3, 'house 1');
INSERT INTO dog VALUES (3, 'dog 3', '2001-01-01', 5, 3, 'house 3');
INSERT INTO dog VALUES (4, 'dog 4', '2001-01-01', 6, 4, NULL);
INSERT INTO dog VALUES (5, 'dog 5', '2001-01-01', 3, 5, NULL);
INSERT INTO dog VALUES (6, 'dog 6', '2001-01-01', 2, 6, NULL);

INSERT INTO cat VALUES ('black cat', 'house 1');
INSERT INTO cat VALUES ('white cat', 'house 4');
INSERT INTO cat VALUES ('red cat', 'house 4');
INSERT INTO cat (name) VALUES ('blue cat');

INSERT INTO dog_vs_cat VALUES (1,1);
INSERT INTO dog_vs_cat VALUES (2,3);
INSERT INTO dog_vs_cat VALUES (3,3);

INSERT INTO street VALUES ('happy street', 100);
INSERT INTO street VALUES ('error street', -100);
INSERT INTO street VALUES ('null street', NULL);
INSERT INTO street (name) VALUES ('clean code street');
INSERT INTO street (name, len) VALUES ('cool street', 10);


CREATE OR ALTER PROCEDURE V1
AS
BEGIN
	ALTER TABLE dog ADD COLUMN breed VARCHAR(16)
	PRINT('V1 add column')
END
GO
EXEC V1

CREATE OR ALTER PROCEDURE V2
AS
BEGIN
	ALTER TABLE dog ADD CONSTRAINT my_pk_dog PRIMARY KEY(Tdoggy)
	PRINT('V2 add primary key')
END
GO

CREATE OR ALTER V3
AS
BEGIN
	ALTER TABLE dog ADD fk_event INT NOT NULL
	ALTER TABLE dog ADD CONSTRAINT fk_doggy_event FOREIGN KEY(fk_event) REFERENCES cat(pk_cat_id)
	PRINT('V3 add foreign key')
END
GO

CREATE OR ALTER V4
AS
BEGIN
	CREATE TABLE last_owner(
		id_last_owner INT PRIMARY KEY,
		name VARCHAR(16)
	)
	PRINT('V4 create table')
END
GO

CREATE OR ALTER RV1
AS
BEGIN
	ALTER TABLE dog DROP COLUMN breed
	PRINT('RV1 drop column')
END	
GO
EXEC RV1

CREATE OR ALTER RV2
AS
BEGIN
	ALTER TABLE dog DROP CONSTRAINT my_pk_dog
	PRINT('RV2 drop primary key')
END
GO

CREATE OR ALTER RV3
AS
BEGIN
	ALTER TABLE dog DROP CONSTRAINT fk_doggy_event
	ALTER TABLE dog DROP COLUMN fk_doggy_event
	PRINT('RV3 drop foreign key')
END
GO

CREATE OR ALTER RV4
AS
BEGIN
	DROP TABLE last_owner
	PRINT('RV4 drop table')
END
GO

CREATE TABLE Versions(
	vid INT PRIMARY KEY,
	no_ver INT NOT NULL
)

INSERT INTO Versions VALUES(0, 0)

DROP TABLE Versions

CREATE OR ALTER PROCEDURE main
	@version INT
AS
BEGIN
	DECLARE @vfrom INT

	SET @vfrom = (SELECT V.no_ver FROM Versions V)
	DECLARE @do VARCHAR(50)
	IF @version <= 7 AND @version >= 0
		IF @version > @vfrom
		BEGIN
			WHILE @version > @vfrom
			BEGIN
				SET @vfrom = @vfrom + 1
				SET @do = 'V' + CAST(@vfrom AS VARCHAR(2))
				EXEC @do
			END
		END

		ELSE
			WHILE @version < @vfrom
			BEGIN
				IF @vfrom != 0
				BEGIN
					SET @do = 'RV' + CAST(@vfrom AS VARCHAR(2))
					EXEC @do
				END
				SET @vfrom = @vfrom - 1
			END

		ELSE
		BEGIN
			PRINT('Version out of bounds')
			RETURN
		END

		UPDATE Versions
		SET no_ver = @version
		
END
GO

EXEC main 0
SELECT * FROM Versions