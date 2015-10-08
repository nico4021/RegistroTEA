-- MySQL dump 10.13  Distrib 5.6.26, for Linux (x86_64)
--
-- Host: localhost    Database: proyectotea
-- ------------------------------------------------------
-- Server version	5.6.26

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

--
-- Table structure for table `AppTEA_area`
--

DROP TABLE IF EXISTS `AppTEA_area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AppTEA_area` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AppTEA_area`
--

LOCK TABLES `AppTEA_area` WRITE;
/*!40000 ALTER TABLE `AppTEA_area` DISABLE KEYS */;
/*!40000 ALTER TABLE `AppTEA_area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AppTEA_cobranza`
--

DROP TABLE IF EXISTS `AppTEA_cobranza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AppTEA_cobranza` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `porcentaje_aporte` int(11) NOT NULL,
  `profesional_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `AppTEA_cobranza_6e88626c` (`profesional_id`),
  CONSTRAINT `D40341b00262e81752820c4090d1861b` FOREIGN KEY (`profesional_id`) REFERENCES `AppTEA_profesional` (`user_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AppTEA_cobranza`
--

LOCK TABLES `AppTEA_cobranza` WRITE;
/*!40000 ALTER TABLE `AppTEA_cobranza` DISABLE KEYS */;
/*!40000 ALTER TABLE `AppTEA_cobranza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AppTEA_paciente`
--

DROP TABLE IF EXISTS `AppTEA_paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AppTEA_paciente` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dni` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `apellidos` varchar(30) NOT NULL,
  `diagnostico` varchar(300) NOT NULL,
  `obra_social` varchar(20) NOT NULL,
  `foto` varchar(100) NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `numero_afiliado` varchar(30) NOT NULL,
  `nombres` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AppTEA_paciente`
--

LOCK TABLES `AppTEA_paciente` WRITE;
/*!40000 ALTER TABLE `AppTEA_paciente` DISABLE KEYS */;
/*!40000 ALTER TABLE `AppTEA_paciente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AppTEA_presupuesto`
--

DROP TABLE IF EXISTS `AppTEA_presupuesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AppTEA_presupuesto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tratamiento_prestacion` varchar(50) NOT NULL,
  `horas_semanales` int(11) NOT NULL,
  `horas_mensuales` int(11) NOT NULL,
  `domicilio_prestacion` varchar(40) NOT NULL,
  `costo_hora` int(11) NOT NULL,
  `dias_semanales` varchar(100) NOT NULL,
  `horario` varchar(6) NOT NULL,
  `frecuencia` int(11) NOT NULL,
  `costo_mensual` int(11) NOT NULL,
  `paciente_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `AppTEA_presup_paciente_id_544ba23816e0006c_fk_AppTEA_paciente_id` (`paciente_id`),
  CONSTRAINT `AppTEA_presup_paciente_id_544ba23816e0006c_fk_AppTEA_paciente_id` FOREIGN KEY (`paciente_id`) REFERENCES `AppTEA_paciente` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AppTEA_presupuesto`
--

LOCK TABLES `AppTEA_presupuesto` WRITE;
/*!40000 ALTER TABLE `AppTEA_presupuesto` DISABLE KEYS */;
/*!40000 ALTER TABLE `AppTEA_presupuesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AppTEA_presupuesto_cobranza`
--

DROP TABLE IF EXISTS `AppTEA_presupuesto_cobranza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AppTEA_presupuesto_cobranza` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `presupuesto_id` int(11) NOT NULL,
  `cobranza_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `presupuesto_id` (`presupuesto_id`,`cobranza_id`),
  KEY `AppTEA_presup_cobranza_id_718be0dd1fd37fb9_fk_AppTEA_cobranza_id` (`cobranza_id`),
  CONSTRAINT `AppTEA__presupuesto_id_77deee6891e526e7_fk_AppTEA_presupuesto_id` FOREIGN KEY (`presupuesto_id`) REFERENCES `AppTEA_presupuesto` (`id`),
  CONSTRAINT `AppTEA_presup_cobranza_id_718be0dd1fd37fb9_fk_AppTEA_cobranza_id` FOREIGN KEY (`cobranza_id`) REFERENCES `AppTEA_cobranza` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AppTEA_presupuesto_cobranza`
--

LOCK TABLES `AppTEA_presupuesto_cobranza` WRITE;
/*!40000 ALTER TABLE `AppTEA_presupuesto_cobranza` DISABLE KEYS */;
/*!40000 ALTER TABLE `AppTEA_presupuesto_cobranza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AppTEA_presupuesto_profesional`
--

DROP TABLE IF EXISTS `AppTEA_presupuesto_profesional`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AppTEA_presupuesto_profesional` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `presupuesto_id` int(11) NOT NULL,
  `profesional_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `presupuesto_id` (`presupuesto_id`,`profesional_id`),
  KEY `D497257a04fafd29daf001ef4cbd6a71` (`profesional_id`),
  CONSTRAINT `AppTEA__presupuesto_id_50ef51764476fa08_fk_AppTEA_presupuesto_id` FOREIGN KEY (`presupuesto_id`) REFERENCES `AppTEA_presupuesto` (`id`),
  CONSTRAINT `D497257a04fafd29daf001ef4cbd6a71` FOREIGN KEY (`profesional_id`) REFERENCES `AppTEA_profesional` (`user_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AppTEA_presupuesto_profesional`
--

LOCK TABLES `AppTEA_presupuesto_profesional` WRITE;
/*!40000 ALTER TABLE `AppTEA_presupuesto_profesional` DISABLE KEYS */;
/*!40000 ALTER TABLE `AppTEA_presupuesto_profesional` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `AppTEA_profesional`
--

DROP TABLE IF EXISTS `AppTEA_profesional`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `AppTEA_profesional` (
  `user_ptr_id` int(11) NOT NULL,
  `rnp` int(11) NOT NULL,
  `dni` varchar(10) NOT NULL,
  `num_matricula` int(11) NOT NULL,
  `tel_personal` int(11) NOT NULL,
  `area_id` int(11) NOT NULL,
  PRIMARY KEY (`user_ptr_id`),
  KEY `AppTEA_profesional_area_id_14b61fd4e1c718d1_fk_AppTEA_area_id` (`area_id`),
  CONSTRAINT `AppTEA_profesional_area_id_14b61fd4e1c718d1_fk_AppTEA_area_id` FOREIGN KEY (`area_id`) REFERENCES `AppTEA_area` (`id`),
  CONSTRAINT `AppTEA_profesional_user_ptr_id_afd97349a534584_fk_auth_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `AppTEA_profesional`
--

LOCK TABLES `AppTEA_profesional` WRITE;
/*!40000 ALTER TABLE `AppTEA_profesional` DISABLE KEYS */;
/*!40000 ALTER TABLE `AppTEA_profesional` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add area',7,'add_area'),(20,'Can change area',7,'change_area'),(21,'Can delete area',7,'delete_area'),(22,'Can add paciente',8,'add_paciente'),(23,'Can change paciente',8,'change_paciente'),(24,'Can delete paciente',8,'delete_paciente'),(25,'Can add profesional',9,'add_profesional'),(26,'Can change profesional',9,'change_profesional'),(27,'Can delete profesional',9,'delete_profesional'),(28,'Can add cobranza',10,'add_cobranza'),(29,'Can change cobranza',10,'change_cobranza'),(30,'Can delete cobranza',10,'delete_cobranza'),(31,'Can add presupuesto',11,'add_presupuesto'),(32,'Can change presupuesto',11,'change_presupuesto'),(33,'Can delete presupuesto',11,'delete_presupuesto');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$O0m6k0qfkBdk$5WIuN9iYykyQe8Jqn/veZAseKT3SmgEjC/fCMEerfMI=','2015-10-06 15:24:04.130755',1,'nico','','','nico-bone@hotmail.com',1,1,'2015-10-06 15:23:49.028211');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'AppTEA','area'),(10,'AppTEA','cobranza'),(8,'AppTEA','paciente'),(11,'AppTEA','presupuesto'),(9,'AppTEA','profesional'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-10-06 15:23:01.968459'),(2,'contenttypes','0002_remove_content_type_name','2015-10-06 15:23:03.178204'),(3,'auth','0001_initial','2015-10-06 15:23:10.686156'),(4,'auth','0002_alter_permission_name_max_length','2015-10-06 15:23:11.504865'),(5,'auth','0003_alter_user_email_max_length','2015-10-06 15:23:12.330787'),(6,'auth','0004_alter_user_username_opts','2015-10-06 15:23:12.386211'),(7,'auth','0005_alter_user_last_login_null','2015-10-06 15:23:13.002103'),(8,'auth','0006_require_contenttypes_0002','2015-10-06 15:23:13.047645'),(9,'AppTEA','0001_initial','2015-10-06 15:23:23.435453'),(10,'admin','0001_initial','2015-10-06 15:23:25.626662'),(11,'sessions','0001_initial','2015-10-06 15:23:26.489111');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('cmtr71kxezjuid5hhigcbavrodi40t59','ODg4ZTIzZWZkYzJhN2U3ZDZkZWJmMjEzMzdiM2JiNzA0ZDBhYmUwMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjMyOTUwMTNkMzM2MWJkNWQxYjAxNjY2ZmQxNGJhMmEzOTZjMmM4YTciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-10-20 15:24:04.220120');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-06 12:50:27
