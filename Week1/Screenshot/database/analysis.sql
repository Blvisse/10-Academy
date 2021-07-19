 CREATE TABLE IF NOT EXISTS `useranalysis` 
(
    `id` INT NOT NULL AUTO_INCREMENT,
    `MSISDNNumber` VARCHAR(200) NOT NULL,
    `Experience Score` VARCHAR(200) NOT NULL,
    `Engagement Score` VARCHAR(200) NOT NULL,
    `Satisfaction score` VARCHAR(200) NOT NULL,
    
    PRIMARY KEY (`id`)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;


