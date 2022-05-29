-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: rrp_db
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `admin_id` varchar(100) NOT NULL,
  `admin_first_name` varchar(50) NOT NULL,
  `admin_middle_name` varchar(50) NOT NULL,
  `admin_last_name` varchar(50) NOT NULL,
  `admin_location` varchar(250) NOT NULL,
  `admin_phone_no` varchar(15) NOT NULL,
  `admin_emailID` varchar(100) NOT NULL,
  `admin_department_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES ('bkMNVE886xPuadmT1MUI3uIB1tO2','I','M','Umesh','Room IS210, ISE department','9876543210','admin@rvce.edu.in','ASE');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add admins',7,'add_admins'),(26,'Can change admins',7,'change_admins'),(27,'Can delete admins',7,'delete_admins'),(28,'Can view admins',7,'view_admins'),(29,'Can add committee',8,'add_committee'),(30,'Can change committee',8,'change_committee'),(31,'Can delete committee',8,'delete_committee'),(32,'Can view committee',8,'view_committee'),(33,'Can add test',9,'add_test'),(34,'Can change test',9,'change_test'),(35,'Can delete test',9,'delete_test'),(36,'Can view test',9,'view_test'),(37,'Can add users',10,'add_users'),(38,'Can change users',10,'change_users'),(39,'Can delete users',10,'delete_users'),(40,'Can view users',10,'view_users'),(41,'Can add tender',11,'add_tender'),(42,'Can change tender',11,'change_tender'),(43,'Can delete tender',11,'delete_tender'),(44,'Can view tender',11,'view_tender'),(45,'Can add resources',12,'add_resources'),(46,'Can change resources',12,'change_resources'),(47,'Can delete resources',12,'delete_resources'),(48,'Can view resources',12,'view_resources'),(49,'Can add resource_logbook',13,'add_resource_logbook'),(50,'Can change resource_logbook',13,'change_resource_logbook'),(51,'Can delete resource_logbook',13,'delete_resource_logbook'),(52,'Can view resource_logbook',13,'view_resource_logbook'),(53,'Can add committee_members',14,'add_committee_members'),(54,'Can change committee_members',14,'change_committee_members'),(55,'Can delete committee_members',14,'delete_committee_members'),(56,'Can view committee_members',14,'view_committee_members'),(57,'Can add resoruce related links',15,'add_resorucerelatedlinks'),(58,'Can change resoruce related links',15,'change_resorucerelatedlinks'),(59,'Can delete resoruce related links',15,'delete_resorucerelatedlinks'),(60,'Can view resoruce related links',15,'view_resorucerelatedlinks'),(61,'Can add resource related links',16,'add_resourcerelatedlinks'),(62,'Can change resource related links',16,'change_resourcerelatedlinks'),(63,'Can delete resource related links',16,'delete_resourcerelatedlinks'),(64,'Can view resource related links',16,'view_resourcerelatedlinks'),(65,'Can add testing models',17,'add_testingmodels'),(66,'Can change testing models',17,'change_testingmodels'),(67,'Can delete testing models',17,'delete_testingmodels'),(68,'Can view testing models',17,'view_testingmodels'),(69,'Can add resource update logbook',18,'add_resourceupdatelogbook'),(70,'Can change resource update logbook',18,'change_resourceupdatelogbook'),(71,'Can delete resource update logbook',18,'delete_resourceupdatelogbook'),(72,'Can view resource update logbook',18,'view_resourceupdatelogbook'),(73,'Can add user message',19,'add_usermessage'),(74,'Can change user message',19,'change_usermessage'),(75,'Can delete user message',19,'delete_usermessage'),(76,'Can view user message',19,'view_usermessage');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$320000$YrZ4gqhtB3irp63RlBFSTN$AGq5mgyfKnP8U4CaxjF4H2paR0fNUnEwdW/Q9+OVRig=','2022-04-12 11:29:27.057353',1,'ameya','','','ameya@rvce.edu.in',1,1,'2022-01-20 17:46:31.904000'),(2,'pbkdf2_sha256$320000$vPtgQ5i4hH7d9bg1ahGW2F$6aAULiAnjcoEbIE5qsa3qv78Qe1fjBDjeSFO443Y3IU=','2022-04-12 18:22:07.449056',1,'amg','','','ameyaagsilver@gmail.com',1,1,'2022-01-28 12:36:01.174903');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-01-20 18:37:51.137739','23','resources object (23)',3,'',12,1),(2,'2022-01-20 18:38:03.122235','22','resources object (22)',3,'',12,1),(3,'2022-01-20 18:38:03.146414','21','resources object (21)',3,'',12,1),(4,'2022-01-28 12:36:35.639876','29','resources object (29)',3,'',12,2),(5,'2022-01-28 12:50:10.898239','28','resources object (28)',3,'',12,1),(6,'2022-01-28 12:50:38.826571','27','resources object (27)',3,'',12,1),(7,'2022-01-28 12:50:44.642024','26','resources object (26)',3,'',12,1),(8,'2022-01-28 12:50:49.805316','25','resources object (25)',3,'',12,1),(9,'2022-01-28 15:54:49.889391','33','resources object (33)',2,'[{\"changed\": {\"fields\": [\"Image\", \"About\"]}}]',12,1),(10,'2022-01-28 15:55:13.432209','33','resources object (33)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',12,1),(11,'2022-01-28 15:56:55.581841','32','resources object (32)',3,'',12,1),(12,'2022-01-28 15:57:02.944469','31','resources object (31)',3,'',12,1),(13,'2022-01-28 15:57:07.777017','30','resources object (30)',3,'',12,1),(14,'2022-01-28 16:03:09.567704','36','resources object (36)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',12,1),(15,'2022-01-29 10:42:48.626748','46','resources object (46)',3,'',12,1),(16,'2022-01-29 10:42:54.641070','45','resources object (45)',3,'',12,1),(17,'2022-02-11 15:55:36.054788','bkMNVE886xPuadmT1MUI3uIB1tO2','admins object (bkMNVE886xPuadmT1MUI3uIB1tO2)',2,'[{\"changed\": {\"fields\": [\"Department name\"]}}]',7,2),(18,'2022-04-12 17:52:25.933164','bkMNVE886xPuadmT1MUI3uIB1tO2','admins object (bkMNVE886xPuadmT1MUI3uIB1tO2)',2,'[]',7,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'USERVIEW','admins'),(8,'USERVIEW','committee'),(14,'USERVIEW','committee_members'),(15,'USERVIEW','resorucerelatedlinks'),(13,'USERVIEW','resource_logbook'),(16,'USERVIEW','resourcerelatedlinks'),(12,'USERVIEW','resources'),(18,'USERVIEW','resourceupdatelogbook'),(11,'USERVIEW','tender'),(9,'USERVIEW','test'),(17,'USERVIEW','testingmodels'),(19,'USERVIEW','usermessage'),(10,'USERVIEW','users');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'USERVIEW','0001_initial','2022-01-18 08:24:23.956340'),(2,'USERVIEW','0002_auto_20211216_1525','2022-01-18 08:24:24.299550'),(3,'USERVIEW','0003_auto_20211216_1531','2022-01-18 08:24:24.953846'),(4,'USERVIEW','0004_alter_committee_members_table','2022-01-18 08:24:24.965377'),(5,'USERVIEW','0005_alter_tender_about','2022-01-18 08:24:25.013036'),(6,'USERVIEW','0006_alter_resources_about','2022-01-18 08:24:25.059057'),(7,'USERVIEW','0007_alter_resource_logbook_member_id','2022-01-18 08:24:25.258805'),(8,'USERVIEW','0008_alter_resource_logbook_return_date','2022-01-18 08:24:25.319047'),(9,'USERVIEW','0009_auto_20211221_0959','2022-01-18 08:24:25.480203'),(10,'USERVIEW','0010_alter_resources_image','2022-01-18 08:24:25.546378'),(11,'USERVIEW','0011_alter_resources_image','2022-01-18 08:24:25.552672'),(12,'USERVIEW','0012_alter_resource_logbook_return_date','2022-01-18 08:24:25.561646'),(13,'contenttypes','0001_initial','2022-01-18 08:24:25.609958'),(14,'auth','0001_initial','2022-01-18 08:24:26.326462'),(15,'admin','0001_initial','2022-01-18 08:24:26.599642'),(16,'admin','0002_logentry_remove_auto_add','2022-01-18 08:24:26.611579'),(17,'admin','0003_logentry_add_action_flag_choices','2022-01-18 08:24:26.620330'),(18,'contenttypes','0002_remove_content_type_name','2022-01-18 08:24:26.718457'),(19,'auth','0002_alter_permission_name_max_length','2022-01-18 08:24:26.787339'),(20,'auth','0003_alter_user_email_max_length','2022-01-18 08:24:26.824343'),(21,'auth','0004_alter_user_username_opts','2022-01-18 08:24:26.833326'),(22,'auth','0005_alter_user_last_login_null','2022-01-18 08:24:26.887407'),(23,'auth','0006_require_contenttypes_0002','2022-01-18 08:24:26.895611'),(24,'auth','0007_alter_validators_add_error_messages','2022-01-18 08:24:26.903389'),(25,'auth','0008_alter_user_username_max_length','2022-01-18 08:24:26.973128'),(26,'auth','0009_alter_user_last_name_max_length','2022-01-18 08:24:27.036241'),(27,'auth','0010_alter_group_name_max_length','2022-01-18 08:24:27.044027'),(28,'auth','0011_update_proxy_permissions','2022-01-18 08:24:27.069195'),(29,'auth','0012_alter_user_first_name_max_length','2022-01-18 08:24:27.136018'),(30,'sessions','0001_initial','2022-01-18 08:24:27.180080'),(31,'USERVIEW','0013_resorucerelatedlinks','2022-01-20 13:53:39.218276'),(32,'USERVIEW','0014_remove_resorucerelatedlinks_id_and_more','2022-01-20 14:10:36.913826'),(33,'USERVIEW','0015_alter_resorucerelatedlinks_link_id','2022-01-20 14:10:36.929464'),(34,'USERVIEW','0016_delete_resorucerelatedlinks','2022-01-20 14:10:36.929464'),(35,'USERVIEW','0017_alter_resources_table','2022-01-20 14:10:36.929464'),(36,'USERVIEW','0018_alter_resources_table','2022-01-20 14:11:14.109735'),(37,'USERVIEW','0019_resourcerelatedlinks','2022-01-20 14:13:09.281508'),(38,'USERVIEW','0020_remove_resourcerelatedlinks_resoruce_id_and_more','2022-01-20 15:53:51.650816'),(50,'USERVIEW','0021_testingmodels','2022-04-12 15:18:14.922273'),(51,'USERVIEW','0022_alter_committee_members_table','2022-04-12 15:18:14.954233'),(52,'USERVIEW','0023_delete_testingmodels','2022-04-12 15:18:14.986225'),(53,'USERVIEW','0024_resourceupdatelogbook','2022-04-12 15:18:15.218130'),(54,'USERVIEW','0025_alter_resourceupdatelogbook_table','2022-04-12 15:18:15.258038'),(55,'USERVIEW','0026_rename_location_admins_admin_location','2022-04-12 15:18:15.290019'),(56,'USERVIEW','0027_rename_phone_number_admins_phone_no','2022-04-12 15:18:15.338068'),(57,'USERVIEW','0028_admins_department_name','2022-04-12 15:18:15.386057'),(58,'USERVIEW','0029_usermessage','2022-04-12 15:18:15.425961'),(59,'USERVIEW','0030_remove_usermessage_emailid_and_more','2022-04-12 15:18:15.717609'),(60,'USERVIEW','0031_remove_committee_members_committee_id_and_more','2022-04-12 15:18:16.300464'),(61,'USERVIEW','0032_remove_resource_logbook_member_id_and_more','2022-04-12 15:33:09.054423'),(62,'USERVIEW','0033_remove_resource_logbook_borrower_user_id_and_more','2022-04-12 15:33:09.081249'),(63,'USERVIEW','0034_remove_resource_logbook_member_id','2022-04-12 15:33:09.089263'),(64,'USERVIEW','0035_resource_logbook_member_id','2022-04-12 15:33:09.097276'),(65,'USERVIEW','0036_delete_resource_logbook','2022-04-12 15:33:09.105270'),(66,'USERVIEW','0037_resource_logbook','2022-04-12 15:34:01.478634'),(67,'USERVIEW','0038_alter_resourcerelatedlinks_url','2022-04-12 15:39:40.478297'),(68,'USERVIEW','0039_resourcerelatedlinks_hivar_and_more','2022-04-12 15:41:45.640839'),(69,'USERVIEW','0040_alter_resourcerelatedlinks_resource_id','2022-04-12 15:44:09.390345'),(70,'USERVIEW','0041_rename_admin_department_name_admins_admin_department_names','2022-04-12 17:51:45.726709'),(71,'USERVIEW','0042_rename_admin_department_names_admins_admin_department_name','2022-04-12 17:52:15.049989'),(72,'USERVIEW','0043_remove_resourcerelatedlinks_hivar_and_more','2022-04-12 18:20:21.895066'),(73,'USERVIEW','0044_remove_resourcerelatedlinks_resource_id','2022-04-12 18:20:21.918454'),(74,'USERVIEW','0045_resourcerelatedlinks_resource_id','2022-04-12 18:21:19.468551');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('05wu9xt1axvcq3loppgf73qlg1tbqez3','eyJ1aWQiOiJia01OVkU4ODZ4UHVhZG1UMU1VSTN1SUIxdE8yIiwidXNlcm5hbWUiOiJhZG1pbiIsImlzQWRtaW4iOnRydWV9:1nm7v7:LTMBF9fzMNXL7USb_NhXdApunUi5s2DOCAkRIdPiI2o','2022-05-18 11:21:29.970105'),('1m77vvki1v34bl0wuq2ci1ps3ipohjxg','eyJ1aWQiOiJQbkd2NWgwVTl2T2dNNDZlbHp1SGE2TzZRT0wyIiwidXNlcm5hbWUiOiJhbWV5YW1nb25hbC5pczE5IiwiaXNBZG1pbiI6ZmFsc2V9:1neFXz:Cciwd_ojt5P0k7g_726I-w7o2bOdydm8_k8Z6ezRzrw','2022-04-26 17:53:03.392834'),('1wpfh6ei79oe10ldxjzyvu7yx2jip8zc','.eJxVjU1PxCAURf8L64ZAQfqxcza6cFI10Y0xzSs8WpRCUsqY0fjfbc0sdPMW75x77xfJzpCW3Ieb09XEnppTNx6lQv-Zb0F16qG7K0lBcsIlwIybud0zzGMM4KlLvNmoS9dmdoG0FnzCgiyoMaz-_OzwA80jppgXjYm0L7J6LUgPeZ36vbL_3d4H_vwG0O8YdmDeIIyR6hjWxQ10V-iFJnqMBv3h4v4rmCBNWxoRZK00CtEwZgSqylZgjKxkbS2XqKXkKHjDS6tqXqsSbAk1A1QKxKAZ-f4B5-heRQ:1nch0g:R48agS4ooD_7q_KG5XtijuW1KWaf9ZE_0k-_5hBD1KA','2022-04-22 10:48:14.653173'),('3gcnp90xgt63u28x4lk8fy8lrovz00d7','eyJ1aWQiOiJia01OVkU4ODZ4UHVhZG1UMU1VSTN1SUIxdE8yIiwidXNlcm5hbWUiOiJhZG1pbiIsImlzQWRtaW4iOnRydWUsInJlY2VudGx5Vmlld2VkUmVzb3VyY2VzIjpbMzcsMzgsMjAsMjRdfQ:1nKbs4:aiFpu3EFaXskOurcOU8djJaS5NDxZaLhLoW4M9HSfYw','2022-03-03 13:40:36.800283'),('3ygz5uhgs1bez7z5ac8k4wpj0ijmdas3','eyJ1aWQiOiJvdzR5NmVLcVBRWGYwN3BPdDh0NDJCQkhLS0EzIiwidXNlcm5hbWUiOiJhdGhhcnZwdy5pczE5IiwiaXNBZG1pbiI6ZmFsc2UsInJlY2VudGx5Vmlld2VkUmVzb3VyY2VzIjpbMjAsMjQsNDMsNDAsMzldfQ:1nV4sB:bnGwkgvU4It5twgG98FactNN-zKZgXVp4bvmX_CEWrA','2022-04-01 10:39:59.366231'),('5k6ijmdqzef4nh9v4rad9ftewn3ty5x3','eyJ1aWQiOiJvdzR5NmVLcVBRWGYwN3BPdDh0NDJCQkhLS0EzIiwidXNlcm5hbWUiOiJhdGhhcnZwdy5pczE5IiwiaXNBZG1pbiI6ZmFsc2V9:1ndPnL:1Hkmm12QoclXjISQKuo1S0E4Y4nEYgHqB38M_7NgtZs','2022-04-24 10:37:27.220433'),('5vkz973be09clwozonk4aysw07dfo8jg','eyJ1aWQiOiJia01OVkU4ODZ4UHVhZG1UMU1VSTN1SUIxdE8yIiwidXNlcm5hbWUiOiJhZG1pbiIsImlzQWRtaW4iOnRydWUsInJlY2VudGx5Vmlld2VkUmVzb3VyY2VzIjpbMjBdfQ:1nd4tf:4eAEAI1ObuaZbGFwiajI72ZBeTG0TNbEIJbKf0aNZpg','2022-04-23 12:18:35.781657'),('6cjjeftfgjghr54stm9c9baucnne3twi','eyJ1aWQiOiJia01OVkU4ODZ4UHVhZG1UMU1VSTN1SUIxdE8yIiwidXNlcm5hbWUiOiJhZG1pbiIsImlzQWRtaW4iOnRydWUsInJlY2VudGx5Vmlld2VkUmVzb3VyY2VzIjpbMjQsMjBdfQ:1nKbqO:sq0hWbDYNICBIZTxCBnYKmdaOkgKrGxWafZok_8ilVY','2022-03-03 13:38:52.813527'),('785sxw8nx3wi2sk4h2e73es76errnllk','eyJ1aWQiOiJia01OVkU4ODZ4UHVhZG1UMU1VSTN1SUIxdE8yIiwidXNlcm5hbWUiOiJhZG1pbiIsImlzQWRtaW4iOnRydWV9:1nG08Q:G0dMLqWhEDKLkivTnJR_AHvP8dGUI3opCD8QZ05Nec8','2022-02-18 20:34:26.962968'),('7892gtxw87breu1hz1r11bijs8ppggku','eyJ1aWQiOiJQbkd2NWgwVTl2T2dNNDZlbHp1SGE2TzZRT0wyIiwidXNlcm5hbWUiOiJhbWV5YW1nb25hbC5pczE5IiwiaXNBZG1pbiI6ZmFsc2UsInJlY2VudGx5Vmlld2VkUmVzb3VyY2VzIjpbMzQsMjQsMjBdfQ:1nV5wL:sn1mV3KjBgNDs6jQHNr4REzkdMe5Zqfa-B-GGemSvWs','2022-04-01 11:48:21.369703'),('7mp9ygxhiq3ptk6bsodyuh82v7hojims','eyJ1aWQiOiJQbkd2NWgwVTl2T2dNNDZlbHp1SGE2TzZRT0wyIiwidXNlcm5hbWUiOiJhbWV5YW1nb25hbC5pczE5IiwiaXNBZG1pbiI6ZmFsc2V9:1ne9AV:wcEzCqztbfDcHUCsMVCt5Wvq-oTPSVBvqOB2aul_A_0','2022-04-26 11:04:23.594576'),('9bx9dw54co29zdds5ji6vy5sn589x9m7','eyJ1aWQiOiJia01OVkU4ODZ4UHVhZG1UMU1VSTN1SUIxdE8yIiwidXNlcm5hbWUiOiJhZG1pbiIsImlzQWRtaW4iOnRydWUsInJlY2VudGx5Vmlld2VkUmVzb3VyY2VzIjpbMjBdfQ:1nmqbe:pKTmPNvvVeqV_cphCKYlUMzPqhG6Z1Zcc1kAvHDOuFw','2022-05-20 11:04:22.442068'),('9ipg5r952jptc182nxqgua9gkiqp2wcd','eyJ1aWQiOiJQbkd2NWgwVTl2T2dNNDZlbHp1SGE2TzZRT0wyIiwidXNlcm5hbWUiOiJhbWV5YW1nb25hbC5pczE5IiwiaXNBZG1pbiI6ZmFsc2UsInJlY2VudGx5Vmlld2VkUmVzb3VyY2VzIjpbMjAsMjQsMzMsNDRdfQ:1ndGbe:Cw_LUsVZerxlWXFhDpXil28_Iz6I-sZR3igm0l0p390','2022-04-24 00:48:46.438351'),('acyyieotxtuy3oi6nya373wxt2vfyydt','eyJ1aWQiOiJvdzR5NmVLcVBRWGYwN3BPdDh0NDJCQkhLS0EzIiwidXNlcm5hbWUiOiJhdGhhcnZwdy5pczE5IiwiaXNBZG1pbiI6ZmFsc2UsInJlY2VudGx5Vmlld2VkUmVzb3VyY2VzIjpbMjQsMzQsMzgsMzYsMjBdfQ:1ngL6O:-le_WFjnAmttRJIgQYV9QOIOVWWxbL61D2qAAKOBIfg','2022-05-02 12:13:12.211448'),('e1vq7j2o6cabwmx43mirowf78zuu5cmq','eyJ1aWQiOiJia01OVkU4ODZ4UHVhZG1UMU1VSTN1SUIxdE8yIiwidXNlcm5hbWUiOiJhZG1pbiIsImlzQWRtaW4iOnRydWV9:1nToni:PIFjInpr-7N9rYJ2J4ySzD3c170BxXK9-sC50mb4ZAg','2022-03-28 23:18:10.293649'),('itnfr16d62osvgd9byb1364fl2bidiav','eyJ1aWQiOiJia01OVkU4ODZ4UHVhZG1UMU1VSTN1SUIxdE8yIiwidXNlcm5hbWUiOiJhZG1pbiIsImlzQWRtaW4iOnRydWUsInJlY2VudGx5Vmlld2VkUmVzb3VyY2VzIjpbMzksMjAsNDAsMzUsMjRdfQ:1nKbn6:ICK1PobzBgKJnFCc0RlQw8mbNmBBUOE4ENPyMTJHeDE','2022-03-03 13:35:28.020138'),('jjeng6etbvwe7q8on8mrj6yj3nicyzq4','eyJ1aWQiOiJQbkd2NWgwVTl2T2dNNDZlbHp1SGE2TzZRT0wyIiwidXNlcm5hbWUiOiJhbWV5YW1nb25hbC5pczE5IiwiaXNBZG1pbiI6ZmFsc2V9:1nUutD:jJHaxWxoS7nwoDCkTuOixcaYDsIp_EAB52U4Ise6Ic0','2022-04-01 00:00:23.384938'),('kondvnoiidnwfsledu8unolb0swdx3xp','eyJ1aWQiOiJia01OVkU4ODZ4UHVhZG1UMU1VSTN1SUIxdE8yIiwidXNlcm5hbWUiOiJhZG1pbiIsImlzQWRtaW4iOnRydWV9:1nIV48:ydjS8rJsfAHagMGVGFQD-oqVYjCqViiqzWQDsBU79qc','2022-02-25 18:00:20.043782'),('kypwln4zwpw9d6fbz6ag4vhp8c1cqt28','eyJ1aWQiOiJQbkd2NWgwVTl2T2dNNDZlbHp1SGE2TzZRT0wyIiwidXNlcm5hbWUiOiJhbWV5YW1nb25hbC5pczE5IiwiaXNBZG1pbiI6ZmFsc2V9:1ncp7K:lE4zEQ_OluVcSHer9124tj9IGzKAadcdyX5RDFoau0s','2022-04-22 19:27:38.108242'),('ltk9q4r3yz3zun5329eafj1t56dojg9a','eyJ1aWQiOiJQbkd2NWgwVTl2T2dNNDZlbHp1SGE2TzZRT0wyIiwidXNlcm5hbWUiOiJhbWV5YW1nb25hbC5pczE5IiwiaXNBZG1pbiI6ZmFsc2UsInJlY2VudGx5Vmlld2VkUmVzb3VyY2VzIjpbNDddfQ:1nd4ej:QViHZPM_whLiUeRcVlJz1jGWON5nSXomQtcQG4NNXt4','2022-04-23 12:03:09.422835'),('moinhnv5ft8efx3lijrhlckqeqo0jkt5','.eJxVjctOwzAQRf_FayvyS46bHZVYdBFaIegGoWhij4lp60h-CBDi30mqLmA3uvfcM9-kBkc6Mp76h-O9MfrzUMFdnnj_vJN1t-VlLwglNWOKcMGFXNoQlyjku-vVlVSRkoQWYzl_HQN-oHvEPNdkMZPuRSoqGBXqlZIBapmGVTZcv67qP9kI9oRxLdw7xLe5sXMsKYzNijS3Njf97PC8vbH_BBPkaVkjgjLaopQbxpxE3foWnFOtMt5zhVYpjpJvuPDacKMFeAGGAWoNcrSM_PwCyXlbBg:1ngKzt:LdB-aWAxs5q-8HYEYBKVsOHSNldZFqcPh1kg4sVB258','2022-05-02 12:06:29.358456'),('o3uxcoqam7okrcdx5v8g64owncp5hjmi','eyJ1aWQiOiJia01OVkU4ODZ4UHVhZG1UMU1VSTN1SUIxdE8yIiwidXNlcm5hbWUiOiJhZG1pbiIsImlzQWRtaW4iOnRydWUsInJlY2VudGx5Vmlld2VkUmVzb3VyY2VzIjpbMjAsMzNdfQ:1nKbsF:whGeBo-a7hKjYBkR-kLYJB6KWyDM9NfFVJBZY8iZwlU','2022-03-03 13:40:47.204247'),('ofshmvusfqt5ktvsjup4tm9dmrmzzsma','eyJ1aWQiOiJia01OVkU4ODZ4UHVhZG1UMU1VSTN1SUIxdE8yIiwidXNlcm5hbWUiOiJhZG1pbiIsImlzQWRtaW4iOnRydWV9:1nctNl:C-tuhNIJk7YpSoCYwQC49dwk0hDawXeGzkrMAIZKflM','2022-04-23 00:00:53.266703'),('wtjkwr5op1m4rrs00njtckp0o6dnqly1','eyJ1aWQiOiJQbkd2NWgwVTl2T2dNNDZlbHp1SGE2TzZRT0wyIiwidXNlcm5hbWUiOiJhbWV5YW1nb25hbC5pczE5IiwiaXNBZG1pbiI6ZmFsc2V9:1nV4YM:ZAjMzPgRQ5QtqLMedfyMTzsBXMxEH56U2cEOL9k7kyo','2022-04-01 10:19:30.169587'),('yw8kq9nvsy7j6ff0k1c16sbg982avty9','eyJ1aWQiOiJQbkd2NWgwVTl2T2dNNDZlbHp1SGE2TzZRT0wyIiwidXNlcm5hbWUiOiJhbWV5YW1nb25hbC5pczE5IiwiaXNBZG1pbiI6ZmFsc2V9:1nWzRw:adVsHlYd6LM0kieHee4peodGYJxzfXU4PLv0281amc8','2022-04-06 17:16:48.157678');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resource_logbook`
--

DROP TABLE IF EXISTS `resource_logbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resource_logbook` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `issue_date` date NOT NULL,
  `return_date` date DEFAULT NULL,
  `admin_id` varchar(100) NOT NULL,
  `member_id` varchar(100) NOT NULL,
  `resource_id` int NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `resource_logbook_admin_id_5a36f74d_fk_admins_admin_id` (`admin_id`),
  KEY `resource_logbook_member_id_9d00e12f_fk_users_user_id` (`member_id`),
  KEY `resource_logbook_resource_id_c52b7e52_fk_resources_resource_id` (`resource_id`),
  CONSTRAINT `resource_logbook_admin_id_5a36f74d_fk_admins_admin_id` FOREIGN KEY (`admin_id`) REFERENCES `admins` (`admin_id`),
  CONSTRAINT `resource_logbook_member_id_9d00e12f_fk_users_user_id` FOREIGN KEY (`member_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `resource_logbook_resource_id_c52b7e52_fk_resources_resource_id` FOREIGN KEY (`resource_id`) REFERENCES `resources` (`resource_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resource_logbook`
--

LOCK TABLES `resource_logbook` WRITE;
/*!40000 ALTER TABLE `resource_logbook` DISABLE KEYS */;
INSERT INTO `resource_logbook` VALUES (1,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(2,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(3,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(4,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(5,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(6,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(7,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(8,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(9,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',24),(10,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(11,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(12,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(13,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',34),(14,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',34),(15,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(16,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(17,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(18,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(19,'2022-04-12','2022-04-12','bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20),(20,'2022-04-18','2022-04-18','bkMNVE886xPuadmT1MUI3uIB1tO2','ow4y6eKqPQXf07pOt8t42BBHKKA3',36),(21,'2022-05-06',NULL,'bkMNVE886xPuadmT1MUI3uIB1tO2','PnGv5h0U9vOgM46elzuHa6O6QOL2',20);
/*!40000 ALTER TABLE `resource_logbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resourcerelatedlinks`
--

DROP TABLE IF EXISTS `resourcerelatedlinks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resourcerelatedlinks` (
  `link_id` int NOT NULL AUTO_INCREMENT,
  `url` varchar(400) NOT NULL,
  `heading` varchar(100) NOT NULL,
  `resource_id` int DEFAULT NULL,
  PRIMARY KEY (`link_id`),
  KEY `resourceRelatedLinks_resource_id_84922dd7_fk_resources` (`resource_id`),
  CONSTRAINT `resourceRelatedLinks_resource_id_84922dd7_fk_resources` FOREIGN KEY (`resource_id`) REFERENCES `resources` (`resource_id`)
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resourcerelatedlinks`
--

LOCK TABLES `resourcerelatedlinks` WRITE;
/*!40000 ALTER TABLE `resourcerelatedlinks` DISABLE KEYS */;
INSERT INTO `resourcerelatedlinks` VALUES (1,'http://google.com/url?q=https://www.arduino.cc/&sa=U&ved=2ahUKEwjgmP-G9cD1AhURyzgGHZnHDhEQFnoECAAQAg&usg=AOvVaw2bbTQAbE2xcJYDYs6r9c6Y','Arduino',20),(2,'http://google.com/url?q=https://en.wikipedia.org/wiki/Arduino&sa=U&ved=2ahUKEwjgmP-G9cD1AhURyzgGHZnHDhEQFnoECAYQAg&usg=AOvVaw2VMRqhlccHancay8HcLX-Y','Arduino - Wikipedia',20),(3,'http://google.com/url?q=https://learn.sparkfun.com/tutorials/what-is-an-arduino/all&sa=U&ved=2ahUKEwjgmP-G9cD1AhURyzgGHZnHDhEQFnoECAoQAg&usg=AOvVaw1H90sKvBBvYioByi_CX4_g','What is an Arduino? - learn.sparkfun.com',20),(13,'http://google.com/url?q=https://beagleboard.org/bone&sa=U&ved=2ahUKEwjVk-_q_cD1AhWGzjgGHSbsAtIQFnoECAkQAg&usg=AOvVaw3E1cuJUGsKYYk9m6IsOAgJ','bone - BeagleBoard.org',24),(14,'http://google.com/url?q=https://beagleboard.org/&sa=U&ved=2ahUKEwjVk-_q_cD1AhWGzjgGHSbsAtIQFnoECAgQAg&usg=AOvVaw30wkRvmpYCQoKU78loUJRs','BeagleBoard.org - community supported open hardware computers ...',24),(15,'http://google.com/url?q=https://en.wikipedia.org/wiki/BeagleBoard&sa=U&ved=2ahUKEwjVk-_q_cD1AhWGzjgGHSbsAtIQFnoECAEQAg&usg=AOvVaw2-bF4spZu9f90D1GQ4vzoY','BeagleBoard - Wikipedia',24),(40,'http://google.com/url?q=https://www.aliexpress.com/item/1758757093.html&sa=U&ved=2ahUKEwiV-qbW5tT1AhWUUGwGHRvWCPkQFnoECAkQAg&usg=AOvVaw2zzXJ_OUfKtjK9prEW4hBn','Devkit 8500D,TI DM3730(ARM Cortex A8) Evaluation Board (1GHZ ...',33),(41,'http://google.com/url?q=https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx6ultralite-evaluation-kit:MCIMX6UL-EVK&sa=U&ved=2ahUKEwiV-qbW5tT1AhWUUGwGHRvWCPkQFnoECAoQAg&usg=AOvVaw0sX-JpWEVZf-c4CKG7Lqb-','MCIMX6UL-EVK: i.MX6UltraLite Evaluation Kit - NXP',33),(42,'http://google.com/url?q=https://www.nxp.com/design/development-boards/i-mx-evaluation-and-development-boards/i-mx-rt1060-evaluation-kit:MIMXRT1060-EVK&sa=U&ved=2ahUKEwiV-qbW5tT1AhWUUGwGHRvWCPkQFnoECAgQAg&usg=AOvVaw0JhqDU6HbLGO05FrTv7zM5','MIMXRT1060-EVK: i.MX RT1060 Evaluation Kit - NXP',33),(43,'http://google.com/url?q=http://www.cmt-gmbh.de/Produkte/WirelessSensorNetworks/Classroom_Kit.html&sa=U&ved=2ahUKEwj818-O6NT1AhXbUGwGHRnkDiEQFnoECAkQAg&usg=AOvVaw1B6eZik3USkL53WXdl22yE','Wireless Sensor Networks ::WSN Classroom Kit - CMT Consulting ...',34),(44,'http://google.com/url?q=https://www.analog.com/en/education/education-library/videos/5579266084001.html&sa=U&ved=2ahUKEwj818-O6NT1AhXbUGwGHRnkDiEQtwJ6BAgBEAE&usg=AOvVaw0tfMkEUgXBK1Ri0VpgqV9_','SmartMesh IP Wireless Sensor Network Starter Kit | Analog Devices',34),(45,'http://google.com/url?q=https://www.researchgate.net/publication/228092464_An_educational_tool_for_wireless_sensor_networks&sa=U&ved=2ahUKEwj818-O6NT1AhXbUGwGHRnkDiEQFnoECAIQAg&usg=AOvVaw310ofVgayTlnJbMwNJXwHj','An educational tool for wireless sensor networks - ResearchGate',34),(46,'http://google.com/url?q=https://www.nltk.org/&sa=U&ved=2ahUKEwjGsau96NT1AhU_TGwGHVLRAmAQFnoECAoQAg&usg=AOvVaw0VSZO_zR6dmKWPMlwRMYB2','NLTK :: Natural Language Toolkit',35),(47,'http://google.com/url?q=https://www.guru99.com/nltk-tutorial.html&sa=U&ved=2ahUKEwjGsau96NT1AhU_TGwGHVLRAmAQFnoECAYQAg&usg=AOvVaw2C6krC9KAl4iyEDhNxeE90','NLTK Tutorial: What is NLTK Library in Python? - Guru99',35),(48,'http://google.com/url?q=https://en.wikipedia.org/wiki/Natural_Language_Toolkit&sa=U&ved=2ahUKEwjGsau96NT1AhU_TGwGHVLRAmAQFnoECAgQAg&usg=AOvVaw3OREGy-w-Vb6xU4ar6ZP0B','Natural Language Toolkit - Wikipedia',35),(49,'http://google.com/url?q=https://www.selenium.dev/&sa=U&ved=2ahUKEwjVyarl6NT1AhUk63MBHfuaA_0QFnoECAcQAg&usg=AOvVaw1LWqw12UBFN6hdlozmdUyp','Selenium WebDriver',36),(50,'http://google.com/url?q=https://www.softwaretestinghelp.com/test-automation-frameworks-selenium-tutorial-20/&sa=U&ved=2ahUKEwjVyarl6NT1AhUk63MBHfuaA_0QFnoECAkQAg&usg=AOvVaw1ElKaVKzSBX6OfVk2rsrTm','Most Popular Test Automation Frameworks with Pros and Cons',36),(51,'http://google.com/url?q=https://techbeacon.com/app-dev-testing/top-11-open-source-testing-automation-frameworks-how-choose&sa=U&ved=2ahUKEwjVyarl6NT1AhUk63MBHfuaA_0QFnoECAgQAg&usg=AOvVaw3msnALnld6cfi5c0F1cgbl','11 top open-source test automation frameworks: How to choose',36),(52,'http://google.com/url?q=https://www.intel.com/content/www/us/en/developer/tools/oneapi/commercial-base-hpc.html&sa=U&ved=2ahUKEwjdw62s6dT1AhWITWwGHfoqARcQFnoECAoQAg&usg=AOvVaw2iw2aae-13Cqq9PuO8Y2nM','Priority Support for Intel® oneAPI Base & HPC Toolkit',37),(53,'http://google.com/url?q=https://www.intel.com/content/www/us/en/developer/articles/release-notes/intel-parallel-studio-xe-supported-and-unsupported-product-versions.html&sa=U&ved=2ahUKEwjdw62s6dT1AhWITWwGHfoqARcQFnoECAgQAg&usg=AOvVaw1raizoU18fpVcr7QoscHj2','Intel® oneAPI Toolkits and Intel® Parallel Studio XE Supported and ...',37),(54,'http://google.com/url?q=https://en.wikipedia.org/wiki/Intel_Parallel_Studio&sa=U&ved=2ahUKEwjdw62s6dT1AhWITWwGHfoqARcQFnoECAkQAg&usg=AOvVaw1kfGeageiEq2gv6z0-AelT','Intel Parallel Studio - Wikipedia',37),(55,'http://google.com/url?q=https://www.scalable-networks.com/products/qualnet-network-simulation-software/&sa=U&ved=2ahUKEwiMnKTc6dT1AhUYTWwGHUqjCj8QFnoECAoQAg&usg=AOvVaw13R-my4bi6Uv2tyhQGt0HX','QualNet® Network Simulation Software',38),(56,'http://google.com/url?q=https://www.ncs-in.com/product/qualnet-network-simulator-software/&sa=U&ved=2ahUKEwiMnKTc6dT1AhUYTWwGHUqjCj8QFnoECAcQAg&usg=AOvVaw2sxY3tv90Vvhrv6KMla9y0','QualNet Network Simulator Software - NCS',38),(57,'http://google.com/url?q=https://networksimulationtools.com/qualnet-network-simulator/&sa=U&ved=2ahUKEwiMnKTc6dT1AhUYTWwGHUqjCj8QFnoECAkQAg&usg=AOvVaw2i2fVk0moG3ogg2Kp0U_kT','Qualnet Network simulator | Planning, Testing, Training',38),(58,'http://google.com/url?q=https://www.arduino.cc/education/explore-iot-kit&sa=U&ved=2ahUKEwjX1e706dT1AhXRTWwGHXd_DxMQFnoECAkQAg&usg=AOvVaw1uHGnz_RTeWu0mbf_Jf_kN','Explore IoT Kit - Arduino',39),(59,'http://google.com/url?q=https://www.amazon.in/KOOKYE-Internet-Starter-Raspberry-Projects/dp/B01HTE5SGA&sa=U&ved=2ahUKEwjX1e706dT1AhXRTWwGHXd_DxMQFnoECAoQAg&usg=AOvVaw1hFW-AcVRmQ9cvGd6FwvD0','KOOKYE Internet of Things IoT Starter Kit for Raspberry Pi (6 Projects)',39),(60,'http://google.com/url?q=https://www.electronicshub.org/best-iot-starter-kits/&sa=U&ved=2ahUKEwjX1e706dT1AhXRTWwGHXd_DxMQFnoECAQQAg&usg=AOvVaw2SydBSRgasLl4I9CMGGr7J','5 Best IOT Starter Kits with Overview Guide [2022 Updated]',39),(61,'http://google.com/url?q=https://www.neuroelectrics.com/solutions/enobio&sa=U&ved=2ahUKEwil-MCO6tT1AhVISWwGHSBdBF4QFnoECAkQAg&usg=AOvVaw0h-AOepR0xuo8Izl3wYfqv','Enobio® EEG systems | Neuroelectrics',40),(62,'http://google.com/url?q=https://www.neuroelectrics.com/solutions/enobio/8/&sa=U&ved=2ahUKEwil-MCO6tT1AhVISWwGHSBdBF4QFnoECAgQAg&usg=AOvVaw25oqYsk54kyAigcsLk7-C5','Enobio 8 | Solutions | Neuroelectrics',40),(63,'http://google.com/url?q=https://www.neuroelectrics.com/solutions/enobio/20&sa=U&ved=2ahUKEwil-MCO6tT1AhVISWwGHSBdBF4QFnoECAAQAg&usg=AOvVaw33sVA9Sv9GMxjaESy7t563','Enobio 20 | Solutions | Neuroelectrics',40),(64,'http://google.com/url?q=https://robu.in/product-category/raspberry-pi/raspberry-pi-kit/&sa=U&ved=2ahUKEwjzh76q6tT1AhWC63MBHY0PA3kQFnoECAgQAg&usg=AOvVaw2-DmubN1FNLdG4wRLSGuMI','Official Raspberry Pi Kits - Robu.in',41),(65,'http://google.com/url?q=https://robu.in/product-category/raspberry-pi/&sa=U&ved=2ahUKEwjzh76q6tT1AhWC63MBHY0PA3kQFnoECAkQAg&usg=AOvVaw1JhF7az1ZeQM_gs09FZe4f','Buy Raspberry Pi Boards, Displays, Hat, Kit in India at Low Price',41),(66,'http://google.com/url?q=https://www.raspberrypi.com/products/raspberry-pi-4-desktop-kit/&sa=U&ved=2ahUKEwjzh76q6tT1AhWC63MBHY0PA3kQFnoECAcQAg&usg=AOvVaw0hVs2_Esa6ApYGGIBjR8_E','Buy a Raspberry Pi 4 Desktop Kit',41),(67,'http://google.com/url?q=https://www.guru99.com/computer-forensics-tools.html&sa=U&ved=2ahUKEwjniL7J6tT1AhWkW3wKHTxnBnoQFnoECAkQAg&usg=AOvVaw0czNJPPY_3WWBzvogODq_S','15 BEST Computer (Digital) Forensic Tools & Software in 2022',42),(68,'http://google.com/url?q=https://h11dfs.com/the-best-open-source-digital-forensic-tools/&sa=U&ved=2ahUKEwjniL7J6tT1AhWkW3wKHTxnBnoQFnoECAcQAg&usg=AOvVaw2VVfCzlZ354j86EHuijkzh','The Best Open Source Digital Forensic Tools',42),(69,'http://google.com/url?q=https://www.forensicscolleges.com/blog/resources/guide-digital-forensics-tools&sa=U&ved=2ahUKEwjniL7J6tT1AhWkW3wKHTxnBnoQFnoECAYQAg&usg=AOvVaw32X5Wgp0GC5K8mVB1tHMsL','A Guide to Digital Forensics and Cybersecurity Tools (2021)',42),(70,'http://google.com/url?q=https://ldra.com/&sa=U&ved=2ahUKEwiSpNHk6tT1AhWG4nMBHfoQDcIQFnoECAkQAg&usg=AOvVaw2J-Qkjfa3mFL8AocneCaxm','LDRA are market leaders in verification and ...',43),(71,'http://google.com/search?ie=UTF-8&q=LDRA+Testbed&stick=H4sIAAAAAAAAAONgVuLSz9U3MDIztyiKBwB7NUgUDgAAAA&sa=X&ved=2ahUKEwiSpNHk6tT1AhWG4nMBHfoQDcIQ6RN6BAgIEAM','LDRA Testbed (Software company)',43),(72,'http://google.com/url?q=https://en.wikipedia.org/wiki/LDRA_Testbed&sa=U&ved=2ahUKEwiSpNHk6tT1AhWG4nMBHfoQDcIQFnoECAIQAg&usg=AOvVaw2x6psl6N8uRO27nTa3KuD1','LDRA Testbed - Wikipedia',43),(73,'http://google.com/url?q=https://ka-naada.com/&sa=U&ved=2ahUKEwjTr6mc69T1AhXOwjgGHb-DDNQQFnoECAEQAg&usg=AOvVaw07piYMQR43D5V_mF4F9uzO','Ka-Naada',44),(74,'http://google.com/url?q=https://www.amazon.in/Total-Kannada-Ka-Naada-Keyboard/dp/B07R5VP9NY&sa=U&ved=2ahUKEwjTr6mc69T1AhXOwjgGHb-DDNQQFnoECAMQAg&usg=AOvVaw2ubnMUzuToC5qBvsezFkmr','Ka-Naada (Kannada Keyboard) - Amazon.in',44),(75,'http://google.com/url?q=https://www.amazon.in/Ka-Naada-Keyboard-for-Indian-Languages/dp/B07RC2T7RL&sa=U&ved=2ahUKEwjTr6mc69T1AhXOwjgGHb-DDNQQFnoECAcQAg&usg=AOvVaw21kkVEA4i61RoIqAG90NoG','Ka-Naada (Keyboard for Indian Languages) - Amazon.in',44),(84,'http://google.com/url?q=https://www.guru99.com/creating-keyword-hybrid-frameworks-with-selenium.html&sa=U&ved=2ahUKEwisqLWG59b1AhUSGbkGHcwEB_wQFnoECAwQAg&usg=AOvVaw33NrbtUi1_S9rwY5_6O3yL','Selenium Automation Framework: Data Driven, Keyword ... - Guru99',47),(85,'http://google.com/url?q=https://www.mindtree.com/insights/resources/selenium-automation-framework-saf&sa=U&ved=2ahUKEwisqLWG59b1AhUSGbkGHcwEB_wQFnoECAkQAg&usg=AOvVaw1osCaARB1mSpsSF-VaTCL-','Selenium Automation Framework (SAF) | Mindtree',47),(86,'http://google.com/url?q=https://www.toolsqa.com/selenium-webdriver/automation-framework-introduction/&sa=U&ved=2ahUKEwisqLWG59b1AhUSGbkGHcwEB_wQFnoECAgQAg&usg=AOvVaw3ZBQV0TsH3pjzmwZ7H7EPi','Automation Framework Introduction - Selenium-Webdriver - Tools QA',47),(87,'http://google.com/url?q=https://www.selenium.dev/&sa=U&ved=2ahUKEwisqLWG59b1AhUSGbkGHcwEB_wQFnoECAYQAg&usg=AOvVaw1oTSvHMXvbKdideZ1IPGeq','Selenium',47),(88,'http://google.com/url?q=https://www.softwaretestingmaterial.com/explain-test-automation-framework/&sa=U&ved=2ahUKEwisqLWG59b1AhUSGbkGHcwEB_wQtwJ6BAgHEAE&usg=AOvVaw2YfxXdYYn8EmIDWsNKVs9c','How To Explain Test Automation Framework To The Interviewer',47);
/*!40000 ALTER TABLE `resourcerelatedlinks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources`
--

DROP TABLE IF EXISTS `resources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resources` (
  `resource_id` int NOT NULL AUTO_INCREMENT,
  `resource_name` varchar(250) NOT NULL,
  `OEM` varchar(100) NOT NULL,
  `resource_type` varchar(50) NOT NULL,
  `department_name` varchar(100) NOT NULL,
  `unit_cost` int NOT NULL,
  `location` varchar(250) NOT NULL,
  `purchase_date` date DEFAULT NULL,
  `quantity` int NOT NULL,
  `image` varchar(100) NOT NULL,
  `about` varchar(1000) NOT NULL,
  `admin_id` varchar(100) NOT NULL,
  PRIMARY KEY (`resource_id`),
  KEY `resources_admin_id_7bd29f19_fk_admins_user_id` (`admin_id`),
  CONSTRAINT `resources_admin_id_7bd29f19_fk_admins_user_id` FOREIGN KEY (`admin_id`) REFERENCES `admins` (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources`
--

LOCK TABLES `resources` WRITE;
/*!40000 ALTER TABLE `resources` DISABLE KEYS */;
INSERT INTO `resources` VALUES (20,'Arduino','Simple Projects','Hardware','ISE',450,'R&D Lab - Dept. of ISE','2022-01-01',19,'hello/arduino.jfif','Arduino is an open-source hardware and software company, project, and user community that designs and manufactures single-board microcontrollers and microcontroller kits for building digital devices. Its hardware products are licensed under a CC-BY-SA license, while software is licensed under the GNU Lesser General Public License (LGPL) or the GNU General Public License (GPL), permitting the manufacture of Arduino boards and software distribution by anyone. Arduino boards are available commercially from the official website or through authorized distributors.\r\n\r\nArduino board designs use a variety of microprocessors and controllers. The boards are equipped with sets of digital and analog input/output (I/O) pins that may be interfaced to various expansion boards (\'shields\') or breadboards (for prototyping) and other circuits.  ','bkMNVE886xPuadmT1MUI3uIB1tO2'),(24,'Beaglebone','Beaglebone.org','Hardware','ISE',1500,'Room IS100, IS department','2022-01-21',5,'hello/beaglebone.webp','The BeagleBoard is a low-power open-source single-board computer produced by Texas Instruments in association with Digi-Key and Newark element14. The BeagleBoard was also designed with open source software development in mind, and as a way of demonstrating the Texas Instrument\'s OMAP3530 system-on-a-chip. The board was developed by a small team of engineers as an educational board that could be used in colleges around the world to teach open source hardware and software capabilities. It is also sold to the public under the Creative Commons share-alike license. The board was designed using Cadence OrCAD for schematics and Cadence Allegro for PCB manufacturing; no simulation software was used.    ','bkMNVE886xPuadmT1MUI3uIB1tO2'),(33,'Dev Kit 8500D Evaluation kit','N/A','Hardware','ISE',3000,'R&D Lab - Dept. of ISE','2013-04-26',2,'hello/noImageAvailable.jpg','•	Professional Embedded System Solution Provider - 2 Nos. •	CD\'s - 3 Nos.•	Manual - 1 No.•	USB Cable - 4 Nos.•	VGA - 4 Nos.•	2 Pin Power cable - 4 Nos.•	Connecting Wires - 2 Nos.•	Micro SD 4GB chip - 2 Nos.•	Texas Instruments JTAG Emulator - 2 Nos. - contains EM Board•	VGA Driver & Manual CD\'s - 3 Nos.•	Chip with USB - 1 No.•	High Resolution Box Camera - 2 Nos.•	Venir CCTV Lens - 2 Nos.•	ASUS VGA HDMI Clamps - Big (12 Nos.) and Small (16 Nos.)  ','bkMNVE886xPuadmT1MUI3uIB1tO2'),(34,'Wireless Sensor Network Educational Kit','N/A','Hardware','ISE',2500,'R&D Lab - Dept. of ISE','2013-10-23',1,'hello/WSN_kit_4PJ8KCF.jpg','•	Data Acquisition Boards-20 Nos.\r\n•	Iris Processor with radio boards – 30 Nos.\r\n•	Mote View Support CD\'s -09 Nos.\r\n•	USB PC interface Board -10 Nos.\r\n•	Cables -10 Nos.\r\n','bkMNVE886xPuadmT1MUI3uIB1tO2'),(35,'Natural Language Processing Kit','N/A','Hardware','ISE',3000,'R&D Lab - Dept. of ISE','2013-03-24',1,'hello/NLP_kit_aEZNaJL.jpg','•	SimBoard – 2 Nos.\r\n•	GPS Antenna -2 Nos.\r\n•	Wenxin Cable -2 Nos.\r\n•	Digital CCTV - 2 Nos.\r\n•	Manual CD\'s – 4 Nos.\r\n•	CCTV Lens - 2 Nos.\r\n•	Bracket Bundle - 1Box\r\n•	Emulation Board with Sony Speakers (2) – 1 No.\r\n•	Verification Board with Sony Speakers (2) – 1 No.\r\n•	ZView IDE with C Compiler & USB debugging probe- 1 No.\r\n','bkMNVE886xPuadmT1MUI3uIB1tO2'),(36,'Selenium Automation framework Software','Selenium','Software','ISE',1000,'R&D Lab - Dept. of ISE','2013-03-20',7,'hello/noImageAvailable_BWN8wgk.jpg','•	Selenium Automation framework','bkMNVE886xPuadmT1MUI3uIB1tO2'),(37,'Intel Parallel & Cluster Studio XE 2013','Intel','Software','ISE',1000,'R&D Lab - Dept. of ISE','2014-04-14',50,'hello/noImageAvailable_1HNUOT3.jpg','•	 Intel Software Development Suite Student Edition for Linux OS -25 Seats\r\n•	Intel Software Development Suite Student Edition for Windows OS -25 Seats\r\n','bkMNVE886xPuadmT1MUI3uIB1tO2'),(38,'Qualnet Network Simulation Software','Scalable Networks','Software','ISE',1000,'R&D Lab - Dept. of ISE','2014-12-09',2,'hello/noImageAvailable_fqiMlet.jpg','•	Advanced Wireless  Library\r\n•	Sensor Networks Library\r\n','bkMNVE886xPuadmT1MUI3uIB1tO2'),(39,'IoT Kit','N/A','Hardware','ISE',2549,'R&D Lab - Dept. of ISE','2016-12-14',5,'hello/Iot_Kit_PvRmZ7h.jpg','•	UbiSense - 10\r\n•	 Cmote - 10 \r\n•	 Wi-Fi mote -10 \r\n•	 WINGZ gateway -1 \r\n•	 Tiny  OS Zigbee IDE SDK -1 \r\n•	 BLE mote -10 \r\n•	 Ubidaq - 10q\r\n','bkMNVE886xPuadmT1MUI3uIB1tO2'),(40,'Enobio Headset','Enobio','Hardware','ISE',1500,'R&D Lab - Dept. of ISE','2017-03-17',1,'hello/Enobio_headset_sRhaA8M.jpg','•	NE003-ENOBIO 8 Channel \r\n•	 NE010 ENOBIO NECBOX - 1 \r\n•	 NE013 micro USB NECBOX charger - 1 \r\n•	 NE014 Curved Syringe - 1 \r\n•	 NE015 USB card with software - 1 \r\n•	 NE016 Gel Bottle 60cl - 1 \r\n•	 NE017 10 Electrode cable - 1 \r\n•	 NE019 Neoprene HeadCap - 1 \r\n•	 NE020 Neoprene Headband - 1 \r\n•	 NE021 Frontal dry electrode front-end - 4 \r\n•	 NE022 Gel electrode front-end - 8 \r\n•	 NE031 USB Bluetooth Dongle -1 \r\n•	 NE025 Adhesive Electrode Front-end -25 \r\n•	 NE023-Dry Electrodes – 8 \r\n•	 NE027-Ear Clip \r\n','bkMNVE886xPuadmT1MUI3uIB1tO2'),(41,'Raspberry Pi kits','Raspberry','Hardware','ISE',1200,'R&D Lab - Dept. of ISE','2018-02-01',12,'hello/Raspberry_pi.jpg','•	A 1.2GHz 64-bit quad-core ARMv8 CPU \r\n•	 802.11n Wireless LAN \r\n•	 Bluetooth 4.1 \r\n•	 Bluetooth Low Energy (BLE) \r\n•	 1GB RAM \r\n•	 USB ports- 4 \r\n•	  GPIO pins - 40 \r\n•	 Full HDMI port \r\n•	 Ethernet port \r\n•	 Combined 3.5mm audio jack and composite video \r\n•	 Camera interface (CSI) \r\n•	 Display interface (DSI) \r\n•	 Micro SD card slot (now push-pull rather than push-push) \r\n•	 Video Core IV 3D graphics core \r\n','bkMNVE886xPuadmT1MUI3uIB1tO2'),(42,'Cyber Forensic Tools ','N/A','Hardware','ISE',800,'R&D Lab - Dept. of ISE','2017-08-28',30,'hello/noImageAvailable_LdzLydm.jpg','•	Cyber Check Suite V6.0 consisting of TrueBackWin V2.0, CyberCheck V5.0, F-DaC, V2.0, F-Ran V2.0, F-Tex V1.0, Hasher V1.0\r\n•	MobileCheck Suite V3.1\r\n•	NetForce Suite V3.1 consistes of NeSA V2.0, CyberInvestigator V1.0, EmailTracer V3.0\r\n•	WinLiFT V3.0\r\n•	Advik CDR Analyser V3.5\r\n','bkMNVE886xPuadmT1MUI3uIB1tO2'),(43,'LDRA','N/A','Software','ISE',500,'R&D Lab - Dept. of ISE','2019-02-15',18,'hello/noImageAvailable_ySY9HX7.jpg','•	Test Analysis\r\n•	LDRArules®+TBmisra®+TBsecure®(coding rules checking and softwre quality analysis bundle)\r\n•	LDRAcover®+TBsafe®(Code Coverage bundlle) \r\n•	LDRAunit®+TBsafe®+TBeXtreme® (unit Testing bundle)\r\n','bkMNVE886xPuadmT1MUI3uIB1tO2'),(44,'Ka-naada Keyboard','Ka-naada','Hardware','ISE',450,'R&D Lab - Dept. of ISE','2021-11-18',5,'hello/Ka-naada_Keyboard_NcFrhiB.jpeg','Ka-naada Keyboard special edition ','bkMNVE886xPuadmT1MUI3uIB1tO2'),(47,'Selenium Automation framework ','N/A','Software','ISE',1245,'R&D Lab - Dept. of ISE','2022-01-29',12,'hello/noImageAvailable_jQmq4jr.jpg','qwwerwrwaweswr','bkMNVE886xPuadmT1MUI3uIB1tO2');
/*!40000 ALTER TABLE `resources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resourceupdatelogbook`
--

DROP TABLE IF EXISTS `resourceupdatelogbook`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resourceupdatelogbook` (
  `update_id` int NOT NULL AUTO_INCREMENT,
  `dateTime` datetime(6) NOT NULL,
  `resource_name` varchar(250) DEFAULT NULL,
  `OEM` varchar(100) DEFAULT NULL,
  `resource_type` varchar(50) DEFAULT NULL,
  `department_name` varchar(100) DEFAULT NULL,
  `unit_cost` int DEFAULT NULL,
  `location` varchar(250) DEFAULT NULL,
  `purchase_date` date DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `about` varchar(1000) DEFAULT NULL,
  `admin_id` varchar(100) NOT NULL,
  `resource_id` int NOT NULL,
  PRIMARY KEY (`update_id`),
  KEY `USERVIEW_resourceupd_admin_id_360a033e_fk_admins_us` (`admin_id`),
  KEY `USERVIEW_resourceupd_resource_id_3f67a228_fk_resources` (`resource_id`),
  CONSTRAINT `USERVIEW_resourceupd_admin_id_360a033e_fk_admins_us` FOREIGN KEY (`admin_id`) REFERENCES `admins` (`admin_id`),
  CONSTRAINT `USERVIEW_resourceupd_resource_id_3f67a228_fk_resources` FOREIGN KEY (`resource_id`) REFERENCES `resources` (`resource_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resourceupdatelogbook`
--

LOCK TABLES `resourceupdatelogbook` WRITE;
/*!40000 ALTER TABLE `resourceupdatelogbook` DISABLE KEYS */;
INSERT INTO `resourceupdatelogbook` VALUES (1,'2022-04-12 15:35:58.376558',NULL,NULL,NULL,NULL,NULL,NULL,NULL,5,'',NULL,'bkMNVE886xPuadmT1MUI3uIB1tO2',39),(2,'2022-04-12 18:26:29.559834',NULL,NULL,NULL,NULL,NULL,NULL,NULL,20,'',NULL,'bkMNVE886xPuadmT1MUI3uIB1tO2',20);
/*!40000 ALTER TABLE `resourceupdatelogbook` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test`
--

DROP TABLE IF EXISTS `test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test` (
  `name` varchar(100) NOT NULL,
  `image` varchar(100) NOT NULL,
  `test_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`test_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test`
--

LOCK TABLES `test` WRITE;
/*!40000 ALTER TABLE `test` DISABLE KEYS */;
/*!40000 ALTER TABLE `test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usermessage`
--

DROP TABLE IF EXISTS `usermessage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usermessage` (
  `message_id` int NOT NULL AUTO_INCREMENT,
  `message` varchar(1500) NOT NULL,
  `member_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`message_id`),
  KEY `userMessage_member_id_aa37eaaf_fk_users_user_id` (`member_id`),
  CONSTRAINT `userMessage_member_id_aa37eaaf_fk_users_user_id` FOREIGN KEY (`member_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usermessage`
--

LOCK TABLES `usermessage` WRITE;
/*!40000 ALTER TABLE `usermessage` DISABLE KEYS */;
/*!40000 ALTER TABLE `usermessage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` varchar(100) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `department_name` varchar(100) NOT NULL,
  `phone_no` varchar(20) NOT NULL,
  `emailID` varchar(100) NOT NULL,
  `USN` varchar(20) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('0kTpKjsllcQqnSajax3aru40AkH3','Ameya ','Mahadev','Gonal','ISE','+919869335123','a@rvce.edu.in','1RV19IS005'),('ow4y6eKqPQXf07pOt8t42BBHKKA3','Atharv','Prashant','Wani','ISE','8390233977','atharvpw.is19@rvce.edu.in','1RV19IS010'),('P8fdzPMQFsf35yRG3C18Gimm3ni2','Ameya ','Mahadev','Test','ASE','9869335123','dawodoc867@yeafam.com','1RV19IS005'),('PnGv5h0U9vOgM46elzuHa6O6QOL2','Ameya','Mahadev','Gonal','ISE','9869335123','ameyamgonal.is19@rvce.edu.in','1RV19IS005'),('rLUf89RJd0hFpmwYyGeHNgr2HBp2','Ketan ','M','Vaish','ISE','9876543210','ketanvaish@rvce.edu.in','1RV19IS023'),('tlkvHOJOlxPqFGKWbaVR8E3KhjH3','Ameya','Mahadev','Gonal','ISE','9869335123','ameya@rvce.edu.in','1RV19IS111'),('WrEcXgMu1ZORFws1jTzF4066Ndx1','Ameya ','Mahadev','Gonal','ISE','9869335123','admin.ise@rvce.edu.in','1RV19IS005'),('yWykmqhYFVdJQQaDYhZPJjcwEQV2','Atharv','Prashant','Wani','ISE','9999999999','atharvwani@rvce.edu.in','1RV19IS010');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-11 12:31:13
