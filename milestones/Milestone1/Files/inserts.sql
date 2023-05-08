/*
Script Name: inserts.sql
Author: Andy Almeida
Purpose:
This file a script that will fill the RealEstateDatabaseManagementSystem with sample data tot est the integrity of this database system
Every table will have three sample entries
The order prioritizes the obejcts that do not have foreign keys
The objects that have foreign keys referring to other objects will be placed after to avoid issues in inserting data
*/

-- delete statement to clear the database of data. this can be used to make sure the script can be run again.
-- Safe Update must be set to off in Preferences -> Edit/Preferences/SQL Editor/Other/Safe Updates
/*
DELETE FROM `realestatemanagementdatabasesystem`.`account`;
DELETE FROM `realestatemanagementdatabasesystem`.`advertisement`;
DELETE FROM `realestatemanagementdatabasesystem`.`application`;
DELETE FROM `realestatemanagementdatabasesystem`.`constructiondetails`;
DELETE FROM `realestatemanagementdatabasesystem`.`contentdeliverynetwork`;
DELETE FROM `realestatemanagementdatabasesystem`.`externalecommercesites`;
DELETE FROM `realestatemanagementdatabasesystem`.`firm`;
DELETE FROM `realestatemanagementdatabasesystem`.`hoafinancials`;
DELETE FROM `realestatemanagementdatabasesystem`.`interiorfactsandfeatures`;
DELETE FROM `realestatemanagementdatabasesystem`.`location`;
DELETE FROM `realestatemanagementdatabasesystem`.`mediahosted`;
DELETE FROM `realestatemanagementdatabasesystem`.`multimediacontent`;
DELETE FROM `realestatemanagementdatabasesystem`.`photo`;
DELETE FROM `realestatemanagementdatabasesystem`.`professionaltypes`;
DELETE FROM `realestatemanagementdatabasesystem`.`profile`;
DELETE FROM `realestatemanagementdatabasesystem`.`property`;
DELETE FROM `realestatemanagementdatabasesystem`.`propertyfactsandfeatures`;
DELETE FROM `realestatemanagementdatabasesystem`.`region`;
DELETE FROM `realestatemanagementdatabasesystem`.`registereduser`;
DELETE FROM `realestatemanagementdatabasesystem`.`room`;
DELETE FROM `realestatemanagementdatabasesystem`.`savedproperty`;
DELETE FROM `realestatemanagementdatabasesystem`.`utilitiesandenergydetails`;
DELETE FROM `realestatemanagementdatabasesystem`.`video`;
*/

-- the database used to insert the data into
USE RealEstateManagementDatabaseSystem;

-- registereduser table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`registereduser`
(`email`,`password`)
VALUES
('poncho@gmail.com','poncho123'),
('reah@gmail.com','reah123'),
('benito@gmail.com','slim123'),
('maria@gmail.com', 'mom123');

-- externalecommercesites table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`externalecommercesites`
(`name`,`websitelink`)
VALUES
('Facebook Marketplace','https://www.facebook.com/marketplace/create'),
('Craigslist','https://post.craigslist.org/'),
('OfferUp','https://offerup.com/');

-- location table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`location`
(`loc_id`,`state`,`city`,`zipcode`,`address`)
VALUES
(1,'California','Irvine',92606,'667 Santa Maria'),
(2,'California','San Francisco',94112,'170 Lobos'),
(3,'New York','New York',10007,'10 Murray St'),
(4,'Washington','DC',20004,'1101 Pennsylvania Ave NW'),
(5,'Oregon','Portland',97201,'1526 SW 10th Ave'),
(6,'California','Bakersfield',93304,'700 Oak St');

-- professionaltypes table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`professionaltypes`
(`type`)
VALUES
('Realtor'),
('Renter'),
('Private');

-- firm table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`firm`
(`firm_id`,`name`,`location`)
VALUES
(1,'Ponchos Realtor',4),
(2,'Innova',5),
(3,'Benito Inc.',6);

-- property table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`property`
(`property_id`,`user`,`location`,`listed`)
VALUES
(1,'poncho@gmail.com',1,1),
(2,'reah@gmail.com',2,0),
(3,'benito@gmail.com',3,1);

-- region table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`region`
(`region_id`,`description`)
VALUES
(1,'Washington, DC'),
(2,'New York'),
(3,'Los Angeles');

-- contentdeliverynetwork table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`contentdeliverynetwork`
(`cdn_id`,`region`,`description`,`numcopies`)
VALUES
(1,1,'Washington DC',0),
(2,2,'New York',0),
(3,3,'Los Angeles',10);

-- multimediacontent table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`multimediacontent`
(`content_id`,`title`,`created`,`property`)
VALUES
(1,'Profile Image','poncho@gmail.com',null),
(2,'House Image','poncho@gmail.com',1),
(3,'House Video','poncho@gmail.com',1),
(4,'Profile Image','reah@gmail.com',null),
(5,'Apartment Image','reah@gmail.com',2),
(6,'Apartment Video','reah@gmail.com',2),
(7,'Profile Image','benito@gmail.com',null),
(8,'Condo Image','benito@gmail.com',3),
(9,'Condo Video','benito@gmail.com',3),
(10,'Profile Image','maria@gmail.com',null);

INSERT INTO `realestatemanagementdatabasesystem`.`photo`
(`photo_id`,`content_id`)
VALUES
(1,1),
(2,2),
(3,4),
(4,5),
(5,7),
(6,8),
(7,10);

INSERT INTO `realestatemanagementdatabasesystem`.`video`
(`video_id`,`content_id`,`length`)
VALUES
(1,3,5),
(2,6,6),
(3,9,2);

-- mediahosted table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`mediahosted`
(`media_hosted`,`media`,`cdn`)
VALUES
(1,1,3),
(2,2,3),
(3,3,3),
(4,4,3),
(5,5,3),
(6,6,3),
(7,7,3),
(8,8,3),
(9,9,3),
(10,10,3);

-- account table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`account`
(`account_id`,`user`,`profession`,`firstname`,`lastname`,`zipcode`,`phonenumber`,`firm`)
VALUES
(1,'poncho@gmail.com',null,'Poncho','Slim',94112,'9498366192',null),
(2,'reah@gmail.com','Private','Reah','Mehta','92606','9494444444',2),
(3,'benito@gmail.com','Renter','Benito','Slim','91123','9494177744',3),
(4,'maria@gmail.com',null,'Maria','Palacios','92606','9491919191',null);

-- profile table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`profile`
(`screenname`,`profile_id`,`user`,`photo`)
VALUES
('Poncho',1,'poncho@gmail.com',1),
('reahm',2,'reah@gmail.com',4),
('BadBunny',3,'benito@gmail.com',7),
('bokitaspintadas',4,'maria@gmail.com',10);

-- advertisement table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`advertisement`
(`ad_id`,`property`,`ecommercesite`,`message`,`photo`)
VALUES
(1,1,'Facebook Marketplace','Come check out this house. I just posted it and anyone can come look.',2),
(2,2,'Craigslist','Hello! I have a room in this apartment. Message me for more information. Thank you.',5),
(3,1,'OfferUp','Hola, yo tengo una condo para vender. Mandarme un mensage si queieres saber mas. Gracias.',8);

-- application table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`application`
(`app_id`,`property`,`user`,`message`)
VALUES
(1,1,null,'Hello, my name is Charlie.'),
(2,1,'maria@gmail.com','Yo vi tu apartamento y quiero saber mas.'),
(3,2,'maria@gmail.com','I would like to learn more, Thank you');

-- constructiondetails table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`constructiondetails`
(`constdet_id`,`property`,`type`,`archstyle`,`subtype`,`materials`,`roof`,`condition`,`new`,`yearbuilt`)
VALUES
(1,1,'House','Rustic',null,'Brick and Wood','Mansard',null,0,1994),
(2,2,'Apartment','Apartment','Quad','Steel and PLaster','Flat','Good',0,2012),
(3,3,'Condo','Modern','null','Steel, Concrete, Plaster','Pyramid Hip','New',1,2020);

-- hoafinancials table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`hoafinancials`
(`financials_id`,`property`,`yrprice`,`monthprice`,`pricerangehigh`,`pricerangelow`,`hoafee`,`amenities`,`services`,`associationname`,`buyeragencycomp`)
VALUES
(1,1,1300000,8399,null,1300000,null,'No Amenities','Trash collection comes by weekly', null,2.5),
(2,2,null,2375,null,null,null,null,'Trash collection comes by weekly', null,null),
(3,3,1795000,12125,null,1795000,528,'No Amenities','Exterior Painting, Trash, Maintenance','NYHOA','3.5');

-- interiorfactsandfeatures table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`interiorfactsandfeatures`
(`interiorff_id`,`property`,`bedrooms`,`bathroom`,`fullbathrooms`,`halfbathrooms`,`flooring`,`heating`,`cooling`,`appliances`,`parking`,`laundry`,`pets`,`totalstructurearea`,`totallivablearea`)
VALUES
(1,1,3,1,1,0,'Wooden','Air Conditioning','Air Conditioning','Full Kitchen','Driveway parking 2','Washer and Dry in the Garage','Allowed',1500,1399),
(2,2,1,1,1,0,'Sheet wood','Fireplace','None','Refrigerator, Gas Stove, Oven, Microwave','Street','Not Included','40 lbs. weight limit',1038,1038),
(3,3,3,1,1,0,'Concrete','Forced Air','Gas','Refrigerator, Gas Stove, Oven, Microwave','Common','In-Unit Laundry','Allowed',1483,1483);

-- propertyfactsandfeatures table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`propertyfactsandfeatures`
(`propff_id`,`property`,`accessibility`,`levels`,`stories`,`viewdescription`,`lotfeatures`,`attatchedtoanother`,`specialcond`)
VALUES
(1,1,null,'Two',2,'Forest','Large Backyard',0,null),
(2,2,'Elevator and Accesibility Ramps','One',6,'Street View','Apartment Complex',1,null),
(3,3,'Elevator and Accesibility Ramps','One',3,'Overview of the City','Hi-Rise',1,'Located above a business');

-- room table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`room`
(`room_id`,`property`,`name`,`level`,`area`,`dim_len`,`dim_wid`,`features`)
VALUES
(1,1,'Living Room','Floor',800,100,80,'Open Concept, TV Area, Connected to Backyard'),
(2,1,'Guest Room','Upstairs',149,10,150,'Window, Bathroom Connected'),
(3,1,'Master Bedroom','Upstairs',450,90,50,'Window, Bathroom Connected, Walk in Closet');

-- savedproperty table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`savedproperty`
(`property`,`user`)
VALUES
(1,'poncho@gmail.com'),
(3,'poncho@gmail.com'),
(3,'maria@gmail.com');

-- utilitiesandenergydetails table inserts
INSERT INTO `realestatemanagementdatabasesystem`.`utilitiesandenergydetails`
(`utilenergy_id`,`property`,`info`,`sewage`,`utilities`,`energyefficient`,`security`)
VALUES
(1,1,'Updated Recently','Public Sewer','Natural Gas Connected','Not','Gated'),
(2,2,'Utilities OnCall','Public Sewer','Natural Gas Connected','PG&E','Key Card Required'),
(3,3,'Regular Amenities','Public Sewer','Natural Gas Connected','Solar Powered','Locked Gate');