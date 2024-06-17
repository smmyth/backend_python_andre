/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `demo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL DEFAULT '',
  `hint` text NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `membros` (
  `membro_id` int(11) NOT NULL,
  `nome` varchar(20) DEFAULT NULL,
  `cargo` varchar(20) DEFAULT NULL,
  `genero` char(1) DEFAULT NULL,
  PRIMARY KEY (`membro_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tarefas` (
  `tarefa_id` int(11) NOT NULL,
  `descricao` varchar(50) DEFAULT NULL,
  `membro_id` int(11) DEFAULT NULL,
  `data_inicio` date DEFAULT NULL,
  PRIMARY KEY (`tarefa_id`),
  KEY `membro_id` (`membro_id`),
  CONSTRAINT `tarefas_ibfk_1` FOREIGN KEY (`membro_id`) REFERENCES `membros` (`membro_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
