-- MySQL dump 10.13  Distrib 5.7.14, for Win64 (x86_64)
--
-- Host: localhost    Database: world
-- ------------------------------------------------------
-- Server version	5.7.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

DROP DATABASE IF EXISTS contacts;
CREATE DATABASE IF NOT EXISTS contacts;
USE contacts;

--
-- Table structure for table `contactslist`
--

DROP TABLE IF EXISTS `contactslist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE contactslist (
	cid INT PRIMARY KEY,
    firstName VARCHAR(50),
    lastName VARCHAR(50),
    department VARCHAR(50),
    telNum VARCHAR(50)
);

INSERT INTO contactslist (cid, firstName, lastName, department, telNum)
VALUES
(001, "John", "Doe", "Management", 1234567890),
(002, "Jane", "Smith", "Accounting", 9876543210),
(003, "Michael", "Johnson", "Customer Service", 4567890123),
(004, "Emily", "Brown", "Management", 7890123456),
(005, "David", "Taylor", "Accounting", 2345678901),
(006, "Sarah", "Martinez", "Customer Service", 8901234567),
(007, "Chris", "Anderson", "Customer Service", 5678901234),
(008, "Jessica", "Lee", "Management", 9012345678),
(009, "Daniel", "Garcia", "Accounting", 6789012345),
(010, "Amanda", "Wilson", "Customer Service", 3456789012);
