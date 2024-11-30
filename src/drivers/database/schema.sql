DROP TABLE IF EXISTS `books`;
CREATE TABLE `books` (`id` varchar(255) NOT NULL, `title` text DEFAULT NULL, `author` text, `image` text, `year` varchar(255) DEFAULT NULL, `isbn` varchar(255) DEFAULT NULL, `itemcount` int NOT NULL, PRIMARY KEY (`id`));
DROP TABLE IF EXISTS `loans`;
CREATE TABLE `loans` (`id` int NOT NULL AUTO_INCREMENT,`start_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,`end_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,`returned` tinyint(1) NOT NULL,`reader_id` int NOT NULL,`book_id` varchar(255) NOT NULL, PRIMARY KEY (`id`));
DROP TABLE IF EXISTS `readers`;
CREATE TABLE `readers` (`id` int NOT NULL AUTO_INCREMENT,`firstname` text NOT NULL,`lastname` text, PRIMARY KEY (`id`));
INSERT INTO `readers` (`id`, `firstname`, `lastname`) VALUES (1, 'Jan', 'Kowalski');