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
DELETE FROM `RealEstateManagementDatabaseSystem`.`Account`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`Advertisement`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`Application`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`ConstructionDetails`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`ContentDeliveryNetwork`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`ExternalECommerceSites`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`Firm`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`HOAFinancials`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`InteriorFactsandFeatures`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`Location`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`MediaHosted`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`MultiMediaContent`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`Photo`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`ProfessionalTypes`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`Profile`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`Property`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`PropertyFactsandFeatures`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`Region`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`RegisteredUser`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`Room`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`SavedProperty`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`UtilitiesandEnergyDetails`;
DELETE FROM `RealEstateManagementDatabaseSystem`.`Video`;
*/
-- the database used to insert the data into
USE RealEstateManagementDatabaseSystem;

-- registereduser table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`RegisteredUser`
(`email`,`password`)
VALUES
('poncho@gmail.com','poncho123'),
('reah@gmail.com','reah123'),
('benito@gmail.com','slim123'),
('maria@gmail.com', 'mom123'),
('deaduser@gmail.com', 'deaduser123');

-- externalecommercesites table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`ExternalECommerceSites`
(`name`,`websitelink`)
VALUES
('Facebook Marketplace','https://www.facebook.com/marketplace/create'),
('Craigslist','https://post.craigslist.org/'),
('OfferUp','https://offerup.com/');

-- location table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`Location`
(`loc_id`,`state`,`city`,`zipcode`,`address`)
VALUES
(1,'California','Irvine',92606,'667 Santa Maria'),
(2,'California','San Francisco',94112,'170 Lobos'),
(3,'New York','New York',10007,'10 Murray St'),
(4,'Washington','DC',20004,'1101 Pennsylvania Ave NW'),
(5,'Oregon','Portland',97201,'1526 SW 10th Ave'),
(6,'California','Bakersfield',93304,'700 Oak St'),
(7,'California','Bakersfield',93304,'15590 Heitor Dr.'),
(8,'California','Fresno',94134,'41 Waller St'),
(9,'California','Irvine',92604,'12 Tortoise Shell');


-- professionaltypes table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`ProfessionalTypes`
(`type`)
VALUES
('Realtor'),
('Renter'),
('Private');

-- firm table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`Firm`
(`firm_id`,`name`,`location`)
VALUES
(1,'Ponchos Realtor',4),
(2,'Innova',5),
(3,'Benito Inc.',6);

-- property table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`Property`
(`property_id`,`user`,`location`,`listed`)
VALUES
(1,'poncho@gmail.com',1,1),
(2,'reah@gmail.com',2,0),
(3,'benito@gmail.com',3,1),
(4,'benito@gmail.com',7,1),
(5,'poncho@gmail.com',8,1),
(6,'poncho@gmail.com',9,1);


-- region table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`Region`
(`region_id`,`description`)
VALUES
(1,'Washington, DC'),
(2,'New York'),
(3,'Los Angeles');

-- contentdeliverynetwork table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`ContentDeliveryNetwork`
(`cdn_id`,`region`,`description`,`numcopies`)
VALUES
(1,1,'Washington DC',0),
(2,2,'New York',0),
(3,3,'Los Angeles',10);

-- multimediacontent table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`MultiMediaContent`
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

INSERT INTO `RealEstateManagementDatabaseSystem`.`Photo`
(`photo_id`,`content_id`)
VALUES
(1,1),
(2,2),
(3,4),
(4,5),
(5,7),
(6,8),
(7,10);

INSERT INTO `RealEstateManagementDatabaseSystem`.`Video`
(`video_id`,`content_id`,`length`)
VALUES
(1,3,5),
(2,6,6),
(3,9,2);

-- mediahosted table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`MediaHosted`
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
INSERT INTO `RealEstateManagementDatabaseSystem`.`Account`
(`account_id`,`user`,`profession`,`firstname`,`lastname`,`zipcode`,`phonenumber`,`firm`)
VALUES
(1,'poncho@gmail.com',null,'Poncho','Slim',94112,'9498366192',null),
(2,'reah@gmail.com','Private','Reah','Mehta','92606','9494444444',2),
(3,'benito@gmail.com','Renter','Benito','Slim','91123','9494177744',3),
(4,'maria@gmail.com',null,'Maria','Palacios','92606','9491919191',null),
(5,'deaduser@gmail.com',null,null,null,null,null,null);

-- profile table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`Profile`
(`screenname`,`profile_id`,`user`,`photo`)
VALUES
('Poncho',1,'poncho@gmail.com',1),
('reahm',2,'reah@gmail.com',4),
('BadBunny',3,'benito@gmail.com',7),
('bokitaspintadas',4,'maria@gmail.com',10),
(null, 5, 'deaduser@gmail.com', null);

-- advertisement table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`Advertisement`
(`ad_id`,`property`,`ecommercesite`,`message`,`photo`)
VALUES
(1,1,'Facebook Marketplace','Come check out this house. I just posted it and anyone can come look.',2),
(2,2,'Craigslist','Hello! I have a room in this apartment. Message me for more information. Thank you.',5),
(3,1,'OfferUp','Hola, yo tengo una condo para vender. Mandarme un mensage si queieres saber mas. Gracias.',8);

-- application table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`Application`
(`app_id`,`property`,`user`,`message`)
VALUES
(1,1,null,'Hello, my name is Charlie.'),
(2,1,'maria@gmail.com','Yo vi tu apartamento y quiero saber mas.'),
(3,2,'maria@gmail.com','I would like to learn more, Thank you');

-- constructiondetails table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`ConstructionDetails`
(`constdet_id`,`property`,`type`,`archstyle`,`subtype`,`materials`,`roof`,`condition`,`new`,`yearbuilt`)
VALUES
(1,1,'House','Rustic',null,'Brick and Wood','Mansard',null,0,1994),
(2,2,'Apartment','Apartment','Quad','Steel and PLaster','Flat','Good',0,2012),
(3,3,'Condo','Modern','null','Steel, Concrete, Plaster','Pyramid Hip','New',1,2020);

-- hoafinancials table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`HOAFinancials`
(`financials_id`,`property`,`yrprice`,`monthprice`,`pricerangehigh`,`pricerangelow`,`hoafee`,`amenities`,`services`,`associationname`,`buyeragencycomp`)
VALUES
(1,1,1300000,8399,null,1300000,null,'No Amenities','Trash collection comes by weekly', null,2.5),
(2,2,null,2375,null,null,null,null,'Trash collection comes by weekly', null,null),
(3,3,1795000,12125,null,1795000,528,'No Amenities','Exterior Painting, Trash, Maintenance','NYHOA','3.5'),
(4,4,1110000,8000,null,1110000,120,'Gym','Trash and Park access',null,'3.5'),
(5,5,null,4000,null,null,null,'No Amenities','Parking Spot','FresnoCounty',null),
(6,6,1000000,7000,null,1000000,100,'No Amenities','City of Irvine aid','City of Irvine','1');

-- interiorfactsandfeatures table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`InteriorFactsandFeatures`
(`interiorff_id`,`property`,`bedrooms`,`bathroom`,`fullbathrooms`,`halfbathrooms`,`flooring`,`heating`,`cooling`,`appliances`,`parking`,`laundry`,`pets`,`totalstructurearea`,`totallivablearea`)
VALUES
(1,1,3,1,1,0,'Wooden','Air Conditioning','Air Conditioning','Full Kitchen','Driveway parking 2','Washer and Dry in the Garage','Allowed',1500,1399),
(2,2,1,1,1,0,'Sheet wood','Fireplace','None','Refrigerator, Gas Stove, Oven, Microwave','Street','Not Included','40 lbs. weight limit',1038,1038),
(3,3,3,1,1,0,'Concrete','Forced Air','Gas','Refrigerator, Gas Stove, Oven, Microwave','Common','In-Unit Laundry','Allowed',1483,1483),
(4,4,1,1,1,0,'Sheet wood','Fireplace','None','Refrigerator, Gas Stove, Oven, Microwave','Street','Not Included','40 lbs. weight limit',1038,1038),
(5,5,5,2,1,1,'Brick','AC','AC','Refrigerator, Gas Stove, Oven, Microwave','One spot','Included','40 lbs. weight limit',1200,1200),
(6,6,2,2,2,0,'Sheet wood','AC','None','Kitchen','Driveway','Not Included','40 lbs. weight limit',1038,1038);

-- propertyfactsandfeatures table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`PropertyFactsandFeatures`
(`propff_id`,`property`,`accessibility`,`levels`,`stories`,`viewdescription`,`lotfeatures`,`attatchedtoanother`,`specialcond`)
VALUES
(1,1,null,'Two',2,'Forest','Large Backyard',0,null),
(2,2,'Elevator and Accesibility Ramps','One',6,'Street View','Apartment Complex',1,null),
(3,3,'Elevator and Accesibility Ramps','One',3,'Overview of the City','Hi-Rise',1,'Located above a business');

-- room table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`Room`
(`room_id`,`property`,`name`,`level`,`area`,`dim_len`,`dim_wid`,`features`)
VALUES
(1,1,'Living Room','Floor',800,100,80,'Open Concept, TV Area, Connected to Backyard'),
(2,1,'Guest Room','Upstairs',149,10,150,'Window, Bathroom Connected'),
(3,1,'Master Bedroom','Upstairs',450,90,50,'Window, Bathroom Connected, Walk in Closet');

-- savedproperty table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`SavedProperty`
(`property`,`user`)
VALUES
(1,'poncho@gmail.com'),
(3,'poncho@gmail.com'),
(3,'maria@gmail.com'),
(4,'maria@gmail.com'),
(5,'maria@gmail.com'),
(6,'maria@gmail.com');

-- utilitiesandenergydetails table inserts
INSERT INTO `RealEstateManagementDatabaseSystem`.`UtilitiesandEnergyDetails`
(`utilenergy_id`,`property`,`info`,`sewage`,`utilities`,`energyefficient`,`security`)
VALUES
(1,1,'Updated Recently','Public Sewer','Natural Gas Connected','Not','Gated'),
(2,2,'Utilities OnCall','Public Sewer','Natural Gas Connected','PG&E','Key Card Required'),
(3,3,'Regular Amenities','Public Sewer','Natural Gas Connected','Solar Powered','Locked Gate');