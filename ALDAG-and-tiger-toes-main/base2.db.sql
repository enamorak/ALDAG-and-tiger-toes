BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `zoos` (
	`zoo_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`zoo_name`	TEXT,
	`place`	TEXT
);
INSERT INTO `zoos` VALUES (1,'Rocky','Capetown');
INSERT INTO `zoos` VALUES (2,'Mountain','Florida');
INSERT INTO `zoos` VALUES (3,'Climbing Ceil','Florida');
CREATE TABLE IF NOT EXISTS `payments` (
	`order_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`date`	TEXT,
	`sum`	INTEGER
);
INSERT INTO `payments` VALUES (1,'2021-09-01',28000);
INSERT INTO `payments` VALUES (2,'2021-05-04',30000);
INSERT INTO `payments` VALUES (3,'2021-06-03',30000);
CREATE TABLE IF NOT EXISTS `orders` (
	`client_id`	INTEGER,
	`order_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`price`	INTEGER,
	`order_date`	TEXT,
	`received_date`	TEXT
);
INSERT INTO `orders` VALUES (1,1,28000,'2021-09-01','2021-09-03');
INSERT INTO `orders` VALUES (2,2,30000,'2021-05-04','2021-05-04');
INSERT INTO `orders` VALUES (3,3,30000,'2021-06-03','2021-06-04');
CREATE TABLE IF NOT EXISTS `clients` (
	`client_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`client_name`	TEXT,
	`manager`	TEXT,
	`telephone`	INTEGER
);
INSERT INTO `clients` VALUES (1,'Anna Grek','John Lennon',89152190343);
INSERT INTO `clients` VALUES (2,'Well Well','Sheila Wills',89167893487);
INSERT INTO `clients` VALUES (3,'Sting Smith','Nick Flamel',89154533453);
CREATE TABLE IF NOT EXISTS `categories` (
	`category_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`category_name`	TEXT,
	`price`	INTEGER,
	`number`	INTEGER
);
INSERT INTO `categories` VALUES (1,'amur tigers',30000,2);
INSERT INTO `categories` VALUES (2,'bengal tigers',28000,1);
CREATE TABLE IF NOT EXISTS `basket` (
	`order_id`	INTEGER,
	`animal_id`	INTEGER,
	PRIMARY KEY(`order_id`,`animal_id`)
);
INSERT INTO `basket` VALUES (1,3);
INSERT INTO `basket` VALUES (2,2);
INSERT INTO `basket` VALUES (3,1);
CREATE TABLE IF NOT EXISTS `animals` (
	`animal_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`category_id`	INTEGER,
	`zoo_id`	INTEGER,
	`nick`	INTEGER,
	`gender`	TEXT,
	`height`	INTEGER,
	`weight`	INTEGER,
	`birthday`	TEXT
);
INSERT INTO `animals` VALUES (1,1,1,'Leo','m',120,45,'2011-12-11');
INSERT INTO `animals` VALUES (2,1,2,'Yan','m',121,37,'2018-09-03');
INSERT INTO `animals` VALUES (3,2,3,'In','f',115,34,'2017-05-04');
COMMIT;
