-- MariaDB dump 10.18  Distrib 10.5.8-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: Morelia
-- ------------------------------------------------------
-- Server version	10.5.8-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Clientes`
--

DROP TABLE IF EXISTS `Clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Clientes` (
  `Id` char(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Nombre` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Apellido_Paterno` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Apellido_Materno` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `RFC` varchar(13) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Clientes`
--

LOCK TABLES `Clientes` WRITE;
/*!40000 ALTER TABLE `Clientes` DISABLE KEYS */;
INSERT INTO `Clientes` VALUES ('U1b7s1W2','Pedro','Olivares','Juarez','RFCPedroOJ'),('U1s7L2f5','Arturo','Echeverria','Juarez','RFCArturoEJ'),('U3j0P7e5','Brian','Garcia','Olivares','rfcBrian'),('U3Q4K6e8','Mariana','Suarez','Smith','RFCMarianaSS'),('U4p7N5Q9','Jose','Argueta','Cerecero','RFCJoseAC'),('U6d5a0Z6','Juan Luis','Ruiz','Vanegas','1234567890123'),('U7T4Q9R4','Manuel','Rodriguez','Chavez','RFCManuelRC');
/*!40000 ALTER TABLE `Clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Direcciones`
--

DROP TABLE IF EXISTS `Direcciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Direcciones` (
  `Calle` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Colonia` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Estado` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `CP` char(5) COLLATE utf8mb4_unicode_ci NOT NULL,
  `Id_Cliente` char(8) COLLATE utf8mb4_unicode_ci NOT NULL,
  KEY `Id_Cliente` (`Id_Cliente`),
  CONSTRAINT `Direcciones_ibfk_1` FOREIGN KEY (`Id_Cliente`) REFERENCES `Clientes` (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Direcciones`
--

LOCK TABLES `Direcciones` WRITE;
/*!40000 ALTER TABLE `Direcciones` DISABLE KEYS */;
INSERT INTO `Direcciones` VALUES ('Conocida','Tlalpujahua','Michoacan','61060','U6d5a0Z6'),('Colibri','Centro','Michoacan','58060','U3j0P7e5'),('Cosmos','Juarez','Michoacan','58123','U7T4Q9R4'),('Libertad','Heroes de la independencia','Michoacan','58470','U4p7N5Q9'),('Golondrinas','Vasco de Quiroga','Michoacan','58900','U3Q4K6e8'),('Nardo','Las Flores','Michoacan','58125','U1s7L2f5'),('Gardenias','Las Flores','Michoacan','58125','U1b7s1W2');
/*!40000 ALTER TABLE `Direcciones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-21 20:19:24
