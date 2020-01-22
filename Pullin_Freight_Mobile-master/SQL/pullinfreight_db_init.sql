USE pullinFreight;

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `bill_of_ladings`;
DROP TABLE IF EXISTS `job_link`;
SET FOREIGN_KEY_CHECKS=1;

SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS `bill_of_laidings`;
DROP TABLE IF EXISTS `shippers`;
DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `job_link`;
DROP TABLE IF EXISTS `current_jobs`;
SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE `users`(
`user_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
`first_name`	TEXT NOT NULL,
`last_name` TEXT NOT NULL,
`username` TEXT NOT NULL,
`phone_number` VARCHAR (20) NOT NULL,
`email` TEXT NOT NULL,
`address`	TEXT NOT NULL,
`license_number` TEXT NOT NULL,
`license_expire` DATE NOT NULL
);

CREATE TABLE `shippers`(
`shipper_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
`name`	TEXT NOT NULL,
`broker_name` TEXT,
`address`	TEXT,
`origin` TEXT,
`destination` TEXT,
`comments` TEXT
);


CREATE TABLE `bill_of_ladings` (
`bill_id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
`date` DATE NOT NULL,
`bill_number` VARCHAR(12) NOT NULL,
`shipper_name` TEXT NOT NULL,
`user_name` TEXT NOT NULL,
`origin` VARCHAR(255) NOT NULL,
`destination` VARCHAR(255) NOT NULL,
`loads`  TINYINT UNSIGNED NOT NULL,
`start_time` TIME NOT NULL,
`end_time` TIME NOT NULL,
`hours_worked` TINYINT NOT NULL
);


CREATE TABLE `current_jobs` (
`job_id` INT UNSIGNED  NOT NULL AUTO_INCREMENT PRIMARY KEY,
`shipper_name` TEXT NOT NULL,
`user_name` TEXT NOT NULL,
`start_date` DATE NOT NULL,
`start_time` TIME NOT NULL,
`pay_type` VARCHAR(10) NOT NULL,
`rate` FLOAT,
`origin` TEXT NOT NULL,
`destination` TEXT NOT NULL,
`comments` TEXT
);


CREATE TABLE `job_link` (
`user_id` INT UNSIGNED NOT NULL, FOREIGN KEY (`user_id`) REFERENCES users(`user_id`),
`bill_id` INT UNSIGNED NOT NULL, FOREIGN KEY (`bill_id`) REFERENCES bill_of_ladings (`bill_id`),
PRIMARY KEY (`user_id`, `bill_id`)
);

