/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 10.4.14-MariaDB : Database - peoples_voice_new
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`peoples_voice_new` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `peoples_voice_new`;

/*Table structure for table `authorities` */

DROP TABLE IF EXISTS `authorities`;

CREATE TABLE `authorities` (
  `authority_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `authority_name` varchar(111) DEFAULT NULL,
  `place` varchar(111) DEFAULT NULL,
  `landmark` varchar(111) DEFAULT NULL,
  `pincode` varchar(111) DEFAULT NULL,
  `phone` varchar(111) DEFAULT NULL,
  `email` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`authority_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `authorities` */

insert  into `authorities`(`authority_id`,`login_id`,`authority_name`,`place`,`landmark`,`pincode`,`phone`,`email`) values 
(6,3,'ambulance','medical trust','pallimukku junction','678 765','999999666','medtrust@gmail.com'),
(7,4,'fire force','Ernakulam south','MG road','655 778','8545768944','fireandrescue@gmail.com');

/*Table structure for table `awareness` */

DROP TABLE IF EXISTS `awareness`;

CREATE TABLE `awareness` (
  `awareness_id` int(11) NOT NULL AUTO_INCREMENT,
  `police_id` int(11) DEFAULT NULL,
  `title` varchar(111) DEFAULT NULL,
  `description` varchar(11111) DEFAULT NULL,
  `file` varchar(1111) DEFAULT NULL,
  `place` varchar(111) DEFAULT NULL,
  `event_date_time` varchar(111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`awareness_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `awareness` */

insert  into `awareness`(`awareness_id`,`police_id`,`title`,`description`,`file`,`place`,`event_date_time`,`date_time`) values 
(1,2,'drug free kerala','to council school children to not use drugs','static/files/f099b2cb-7e44-4483-a194-d8a2ffa9d188f4.jpg','Ernakulam','2021-02-10T14:00','2021-02-15 09:48:59');

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `usertype` varchar(111) DEFAULT NULL,
  `title` varchar(111) DEFAULT NULL,
  `description` varchar(111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  `status` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`user_id`,`usertype`,`title`,`description`,`date_time`,`status`) values 
(1,1,'user','mpokket threat','vilich shalyam cheyunnu guyss','everytime','FIR_filed'),
(2,1,'user','sdf','qwerty','2021-02-23 18:23:03','pending');

/*Table structure for table `contacts` */

DROP TABLE IF EXISTS `contacts`;

CREATE TABLE `contacts` (
  `contact_id` int(11) NOT NULL AUTO_INCREMENT,
  `authority` varchar(111) DEFAULT NULL,
  `details` varchar(1111) DEFAULT NULL,
  `number` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`contact_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `contacts` */

insert  into `contacts`(`contact_id`,`authority`,`details`,`number`) values 
(1,'ambulance','in urgent case of any emergency regarding medical issues','102'),
(2,'fire force','emergency cases regarding fire','101');

/*Table structure for table `crime_categories` */

DROP TABLE IF EXISTS `crime_categories`;

CREATE TABLE `crime_categories` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(111) DEFAULT NULL,
  `description` varchar(1111) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `crime_categories` */

insert  into `crime_categories`(`category_id`,`category_name`,`description`) values 
(1,'rape','sexually assaulting a women'),
(2,'dowry','an amound or property of money brought by a bride to a husband on their marriage'),
(3,'domestic violence','violent behaviour between current or formal intimate partners'),
(4,'illegal drug trade','crime of trading or selling illegal drugs'),
(5,'arms traffing','carrying or selling fire arms'),
(6,'petty crime','minor crimes such as theft,tresspassing etc');

/*Table structure for table `crime_records` */

DROP TABLE IF EXISTS `crime_records`;

CREATE TABLE `crime_records` (
  `crime_record_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint_id` int(11) DEFAULT NULL,
  `police_id` int(11) DEFAULT NULL,
  `title` varchar(111) DEFAULT NULL,
  `description` varchar(1111) DEFAULT NULL,
  `file` varchar(1111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`crime_record_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `crime_records` */

insert  into `crime_records`(`crime_record_id`,`complaint_id`,`police_id`,`title`,`description`,`file`,`date_time`) values 
(1,1,2,'taken action against them','death sentense','static/crime_records/d33452d2-5f23-44cf-a4d3-4226b94f904cf6.jpg','2021-02-15 10:05:19');

/*Table structure for table `criminal_alert` */

DROP TABLE IF EXISTS `criminal_alert`;

CREATE TABLE `criminal_alert` (
  `criminal_alert_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `criminal_id` int(11) DEFAULT NULL,
  `police_id` int(11) DEFAULT NULL,
  `found_place` varchar(111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  `status` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`criminal_alert_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `criminal_alert` */

insert  into `criminal_alert`(`criminal_alert_id`,`user_id`,`criminal_id`,`police_id`,`found_place`,`date_time`,`status`) values 
(1,1,1,2,'adholokam','now','investigating');

/*Table structure for table `criminals` */

DROP TABLE IF EXISTS `criminals`;

CREATE TABLE `criminals` (
  `criminal_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `first_name` varchar(111) DEFAULT NULL,
  `last_name` varchar(111) DEFAULT NULL,
  `house_name` varchar(111) DEFAULT NULL,
  `place` varchar(111) DEFAULT NULL,
  `pincode` varchar(111) DEFAULT NULL,
  `age` varchar(111) DEFAULT NULL,
  `gender` varchar(111) DEFAULT NULL,
  `photo` varchar(111) DEFAULT NULL,
  `status` varchar(111) DEFAULT NULL,
  `most_wanted` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`criminal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `criminals` */

insert  into `criminals`(`criminal_id`,`category_id`,`first_name`,`last_name`,`house_name`,`place`,`pincode`,`age`,`gender`,`photo`,`status`,`most_wanted`) values 
(1,1,'ananthu','prasad','pambayil','Alappuzha','688 007','21','male','static/criminals/8244c4d8-31b6-417b-9493-69610dd9888bg7.jpg','missing','most_wanted');

/*Table structure for table `districts` */

DROP TABLE IF EXISTS `districts`;

CREATE TABLE `districts` (
  `district_id` int(11) NOT NULL AUTO_INCREMENT,
  `district_name` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`district_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `districts` */

insert  into `districts`(`district_id`,`district_name`) values 
(1,'alappuzha'),
(2,'idukki'),
(3,'kannur');

/*Table structure for table `feedbacks` */

DROP TABLE IF EXISTS `feedbacks`;

CREATE TABLE `feedbacks` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `feedback` varchar(1111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `feedbacks` */

insert  into `feedbacks`(`feedback_id`,`sender_id`,`feedback`,`date_time`) values 
(3,2,'feeling good','2021-02-15 09:59:55'),
(4,7,'hello','2021-02-23 14:09:16'),
(5,5,'aaa','2021-02-23 23:16:10'),
(6,5,'aaa','2021-02-23 23:17:18'),
(7,7,'hllll','2021-02-23 23:18:12'),
(8,7,'hiiii','2021-02-23 23:22:32');

/*Table structure for table `files` */

DROP TABLE IF EXISTS `files`;

CREATE TABLE `files` (
  `file_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaint_id` int(11) DEFAULT NULL,
  `file` varchar(11111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`file_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `files` */

insert  into `files`(`file_id`,`complaint_id`,`file`,`date_time`) values 
(1,1,'screeenshot','12-22-2020'),
(2,2,'static/uploads/1e4d84ac-93c9-4627-9c65-16729567bd49.jpg','2021-02-23 18:23:03');

/*Table structure for table `local_body` */

DROP TABLE IF EXISTS `local_body`;

CREATE TABLE `local_body` (
  `localbody_id` int(11) NOT NULL AUTO_INCREMENT,
  `station_id` int(11) DEFAULT NULL,
  `name` varchar(111) DEFAULT NULL,
  `description` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`localbody_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `local_body` */

insert  into `local_body`(`localbody_id`,`station_id`,`name`,`description`) values 
(1,1,'jana seva sangam','to protect and ensure safety to people'),
(2,2,'reksha sangam','to be equal');

/*Table structure for table `localbody_members` */

DROP TABLE IF EXISTS `localbody_members`;

CREATE TABLE `localbody_members` (
  `member_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(111) DEFAULT NULL,
  `last_name` varchar(111) DEFAULT NULL,
  `house_name` varchar(111) DEFAULT NULL,
  `place` varchar(111) DEFAULT NULL,
  `pincode` varchar(111) DEFAULT NULL,
  `phone` varchar(111) DEFAULT NULL,
  `email` varchar(111) DEFAULT NULL,
  `status` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `localbody_members` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(111) DEFAULT NULL,
  `password` varchar(111) DEFAULT NULL,
  `usertype` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(3,'authority','authority','authority'),
(4,'authority2','authority2','authority'),
(5,'police','police','police'),
(6,'police1','police1','police'),
(7,'user','user','user'),
(8,'cc','cc','vehicle');

/*Table structure for table `meetings` */

DROP TABLE IF EXISTS `meetings`;

CREATE TABLE `meetings` (
  `meeting_id` int(11) NOT NULL AUTO_INCREMENT,
  `localbody_id` int(11) DEFAULT NULL,
  `meet_date_time` varchar(111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`meeting_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `meetings` */

insert  into `meetings`(`meeting_id`,`localbody_id`,`meet_date_time`,`date_time`) values 
(1,1,'2021-02-18T02:03','2021-02-15');

/*Table structure for table `missing_found` */

DROP TABLE IF EXISTS `missing_found`;

CREATE TABLE `missing_found` (
  `found_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `missing_person_id` int(11) DEFAULT NULL,
  `place` varchar(111) DEFAULT NULL,
  `details` varchar(1111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`found_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `missing_found` */

insert  into `missing_found`(`found_id`,`user_id`,`missing_person_id`,`place`,`details`,`date_time`) values 
(1,1,1,'adholokam','alive','30-12-2021'),
(2,1,1,'pvk','sample','2021-02-23 17:53:46');

/*Table structure for table `missing_persons` */

DROP TABLE IF EXISTS `missing_persons`;

CREATE TABLE `missing_persons` (
  `missing_person_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(111) DEFAULT NULL,
  `last_name` varchar(111) DEFAULT NULL,
  `house_name` varchar(111) DEFAULT NULL,
  `place` varchar(111) DEFAULT NULL,
  `pincode` varchar(111) DEFAULT NULL,
  `photo` varchar(111) DEFAULT NULL,
  `contact_person` varchar(111) DEFAULT NULL,
  `relation` varchar(1111) DEFAULT NULL,
  `phone` varchar(111) DEFAULT NULL,
  `status` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`missing_person_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `missing_persons` */

insert  into `missing_persons`(`missing_person_id`,`first_name`,`last_name`,`house_name`,`place`,`pincode`,`photo`,`contact_person`,`relation`,`phone`,`status`) values 
(1,'treata','regina','aroor','aroor','656989','static/missing/8d31eedc-6535-42bf-b860-3150b3e9ef73g1.jpg','titta','married','76567678','pending');

/*Table structure for table `police` */

DROP TABLE IF EXISTS `police`;

CREATE TABLE `police` (
  `police_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `station_id` int(11) DEFAULT NULL,
  `first_name` varchar(111) DEFAULT NULL,
  `last_name` varchar(111) DEFAULT NULL,
  `age` varchar(111) DEFAULT NULL,
  `qualification` varchar(111) DEFAULT NULL,
  `year_of_join` varchar(111) DEFAULT NULL,
  `phone` varchar(111) DEFAULT NULL,
  `email` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`police_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `police` */

insert  into `police`(`police_id`,`login_id`,`station_id`,`first_name`,`last_name`,`age`,`qualification`,`year_of_join`,`phone`,`email`) values 
(2,5,1,'Biju','Paulose','34','degree','2017','9067676766','actionherobiju@gmail.com'),
(3,6,2,'Sam','Alex','35','IPS','2005','7856340378','samuelalexander@gmail.com');

/*Table structure for table `police_stations` */

DROP TABLE IF EXISTS `police_stations`;

CREATE TABLE `police_stations` (
  `station_id` int(11) NOT NULL AUTO_INCREMENT,
  `district_id` int(11) DEFAULT NULL,
  `station_name` varchar(111) DEFAULT NULL,
  `place` varchar(111) DEFAULT NULL,
  `landmark` varchar(111) DEFAULT NULL,
  `pincode` varchar(111) DEFAULT NULL,
  `phone` varchar(111) DEFAULT NULL,
  `email` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`station_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `police_stations` */

insert  into `police_stations`(`station_id`,`district_id`,`station_name`,`place`,`landmark`,`pincode`,`phone`,`email`) values 
(1,2,'janamaithri police station','kunnumpuram','opp palace','676 789','7565657878','janamaithripolice@gmail.com'),
(2,3,'kannapuram station','kannapuram','post office','670 331','767809874','kannapurmpolice123@gmail.com');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(111) DEFAULT NULL,
  `last_name` varchar(111) DEFAULT NULL,
  `house_name` varchar(111) DEFAULT NULL,
  `place` varchar(111) DEFAULT NULL,
  `pincode` varchar(111) DEFAULT NULL,
  `phone` varchar(111) DEFAULT NULL,
  `email` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`user_id`,`login_id`,`first_name`,`last_name`,`house_name`,`place`,`pincode`,`phone`,`email`) values 
(1,7,'koots','oli','pamba','tharamood','678654','7845650199','koots@gmail.com');

/*Table structure for table `vehicle_locations` */

DROP TABLE IF EXISTS `vehicle_locations`;

CREATE TABLE `vehicle_locations` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_id` varchar(111) DEFAULT NULL,
  `latitude` varchar(111) DEFAULT NULL,
  `longitude` varchar(111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `vehicle_locations` */

insert  into `vehicle_locations`(`location_id`,`vehicle_id`,`latitude`,`longitude`,`date_time`) values 
(1,'2','9.9763527','76.2863176','2022-04-03 14:42:16');

/*Table structure for table `vehicle_request` */

DROP TABLE IF EXISTS `vehicle_request`;

CREATE TABLE `vehicle_request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `vehicle_id` int(11) DEFAULT NULL,
  `police_id` int(11) DEFAULT NULL,
  `reason` varchar(111) DEFAULT NULL,
  `date_time` varchar(111) DEFAULT NULL,
  `status` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `vehicle_request` */

insert  into `vehicle_request`(`request_id`,`vehicle_id`,`police_id`,`reason`,`date_time`,`status`) values 
(1,1,2,'ride pokanam','2021-02-15 09:28:12','assigned');

/*Table structure for table `vehicles` */

DROP TABLE IF EXISTS `vehicles`;

CREATE TABLE `vehicles` (
  `vehicle_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `vehicle_number` varchar(111) DEFAULT NULL,
  `chasis_number` varchar(222) DEFAULT NULL,
  `engine_number` varchar(111) DEFAULT NULL,
  `year_of_manufacture` varchar(111) DEFAULT NULL,
  `company` varchar(111) DEFAULT NULL,
  `model` varchar(111) DEFAULT NULL,
  `status` varchar(111) DEFAULT NULL,
  PRIMARY KEY (`vehicle_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `vehicles` */

insert  into `vehicles`(`vehicle_id`,`login_id`,`vehicle_number`,`chasis_number`,`engine_number`,`year_of_manufacture`,`company`,`model`,`status`) values 
(1,NULL,'456 654 789 766','54;54;778;87','4509:8799:0989','1999','toyota','innova','assigned'),
(2,8,'Quae maxime tenetur ','Dolor hic ea qui et ','Aut sit nulla accusa','Exercitation nesciun','Herman and Jenkins LLC','Quod ut perferendis ','pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
