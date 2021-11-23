BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `zoos` (
	`zoo_id`	INTEGER,
	`cage_id`	INTEGER
);
INSERT INTO `zoos` VALUES (34,45);
INSERT INTO `zoos` VALUES (34,56);
INSERT INTO `zoos` VALUES (79,78);
CREATE TABLE IF NOT EXISTS `warehouse` (
	`warehouse_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`item_id`	INTEGER,
	`specification`	TEXT,
	`price`	INTEGER NOT NULL,
	`rest`	INTEGER,
	`address`	TEXT
);
INSERT INTO `warehouse` VALUES (887,3,'ring',300,89,'Hello, 12');
INSERT INTO `warehouse` VALUES (888,2,'box',200,45,'EasyMade, 12');
INSERT INTO `warehouse` VALUES (889,1,'painting',100,12,'MadWorld, 11');
CREATE TABLE IF NOT EXISTS `payments` (
	`order_id`	INTEGER,
	`organization_id`	INTEGER,
	`payment_date`	TEXT,
	`payment_sum`	INTEGER,
	PRIMARY KEY(`order_id`,`organization_id`)
);
INSERT INTO `payments` VALUES (344,7,'2021-09-04',1000);
INSERT INTO `payments` VALUES (354,5,'2021-09-03',2000);
INSERT INTO `payments` VALUES (364,5,'2021-09-03',300);
CREATE TABLE IF NOT EXISTS `organizations` (
	`organization_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`TIN`	INTEGER NOT NULL,
	`organization_name`	TEXT,
	`CEO`	TEXT,
	`legal_address`	TEXT,
	`telephone`	INTEGER NOT NULL,
	`fax`	INTEGER NOT NULL
);
INSERT INTO `organizations` VALUES (5,243546576,'Safari','Peter Smith','Baker street, 13',12345678912,13334445555);
INSERT INTO `organizations` VALUES (6,324567,'Paradise','Peter Smith','Baker street, 12',12345678912,16789671111);
INSERT INTO `organizations` VALUES (7,24356789,'IceCream','John Wild','Green street, 12',12345673435,12344566786);
CREATE TABLE IF NOT EXISTS `orders` (
	`order_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`client_id`	INTEGER,
	`order_date`	TEXT,
	`order_sum`	INTEGER,
	`state`	INTEGER,
	`shipment_date`	INTEGER,
	`note`	TEXT
);
INSERT INTO `orders` VALUES (344,33,'2021-09-03',2000,0,20210903,NULL);
INSERT INTO `orders` VALUES (354,102,'2021-09-04',300,1,20210904,NULL);
INSERT INTO `orders` VALUES (364,89,'2021-09-03',1000,1,20210903,'be careful');
CREATE TABLE IF NOT EXISTS `ordered` (
	`order_id`	INTEGER,
	`warehouse_id`	INTEGER,
	`number`	INTEGER,
	`cost`	INTEGER,
	PRIMARY KEY(`order_id`,`warehouse_id`)
);
INSERT INTO `ordered` VALUES (344,887,10,3533);
INSERT INTO `ordered` VALUES (354,888,10,33535);
INSERT INTO `ordered` VALUES (364,899,1,1345);
CREATE TABLE IF NOT EXISTS `offsprings` (
	`animal_id`	INTEGER,
	`offspring_id`	INTEGER PRIMARY KEY AUTOINCREMENT
);
INSERT INTO `offsprings` VALUES (11,14);
INSERT INTO `offsprings` VALUES (11,15);
INSERT INTO `offsprings` VALUES (11,16);
CREATE TABLE IF NOT EXISTS `clients` (
	`client_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`manager`	TEXT,
	`telephone`	INTEGER,
	`organization_id`	INTEGER
);
INSERT INTO `clients` VALUES (33,'Jane',12346571234,7);
INSERT INTO `clients` VALUES (89,'Nike',12347850123,5);
INSERT INTO `clients` VALUES (102,'Stella',12345678900,6);
CREATE TABLE IF NOT EXISTS `catalog` (
	`item_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`animal_id`	INTEGER
);
INSERT INTO `catalog` VALUES (1,11);
INSERT INTO `catalog` VALUES (2,12);
INSERT INTO `catalog` VALUES (3,13);
CREATE TABLE IF NOT EXISTS `cages` (
	`animal_id`	INTEGER,
	`cage_id`	INTEGER PRIMARY KEY AUTOINCREMENT
);
INSERT INTO `cages` VALUES (11,45);
INSERT INTO `cages` VALUES (12,56);
INSERT INTO `cages` VALUES (13,78);
CREATE TABLE IF NOT EXISTS `basket` (
	`order_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`item_id`	INTEGER
);
INSERT INTO `basket` VALUES (344,1);
INSERT INTO `basket` VALUES (354,2);
INSERT INTO `basket` VALUES (364,3);
CREATE TABLE IF NOT EXISTS `animals` (
	`animal_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`nick`	TEXT,
	`gender`	TEXT,
	`weight`	INTEGER,
	`height`	INTEGER,
	`birthday`	TEXT
);
INSERT INTO `animals` VALUES (11,'Roxy','f',20,71,'16.02.2016');
INSERT INTO `animals` VALUES (12,'Leo','m',20,76,'17.03.2018');
INSERT INTO `animals` VALUES (13,'In','m',20,72,'18.05.2017');
INSERT INTO `animals` VALUES (14,'Garry','m',5,32,'05.05.2020');
INSERT INTO `animals` VALUES (15,'Mia','f',5,30,'05.05.2020');
INSERT INTO `animals` VALUES (16,'Teo','m',5,28,'05.05.2020');
COMMIT;
