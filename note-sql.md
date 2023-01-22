# Create database
CREATE DATABASE grocery_store;

# Create db user
CREATE USER IF NOT EXISTS 'devmsuser'@'%' IDENTIFIED BY 'devmsuser123';

# Grant permissions
GRANT SELECT, INSERT, CREATE, DELETE  ON grocery_store.* TO 'devmsuser'@'%';
FLUSH PRIVILEGES;

SHOW GRANTS FOR 'devmsuser'@'%';

# Create Tablse
CREATE TABLE `grocery_store`.`products` (
  `product_id` INT NOT NULL,
  `name` VARCHAR(100) NOT NULL,
  `uom_id` INT NOT NULL,
  `price_per_unit` DOUBLE NOT NULL,
  PRIMARY KEY (`product_id`));

CREATE TABLE `grocery_store`.`uom` (
  `uom_id` INT NOT NULL AUTO_INCREMENT,
  `uom_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`uom_id`));

CREATE TABLE `grocery_store`.`orders` (
  `order_id` INT NOT NULL AUTO_INCREMENT,
  `customer_name` VARCHAR(100) NOT NULL,
  `total` DOUBLE NOT NULL,
  `datetime` DATETIME NOT NULL,
  PRIMARY KEY (`order_id`));

CREATE TABLE `grocery_store`.`order_details` (
  `order_id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `quantity` DOUBLE NOT NULL,
  `total_price` DOUBLE NOT NULL,
  PRIMARY KEY (`order_id`),
  CONSTRAINT `fk_product_id`
    FOREIGN KEY (`product_id`)
    REFERENCES `grocery_store`.`products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE RESTRICT,
  CONSTRAINT `fk_order_id`
    FOREIGN KEY (`order_id`)
    REFERENCES `grocery_store`.`orders` (`order_id`)
    ON DELETE NO ACTION
    ON UPDATE RESTRICT);

# Insert Values
INSERT INTO `grocery_store`.`uom` (`uom_id`, `uom_name`) VALUES ('1', 'each');
INSERT INTO `grocery_store`.`uom` (`uom_id`, `uom_name`) VALUES ('2', 'kg');

# Set up foreign key for products table
ALTER TABLE `grocery_store`.`products` 
ADD CONSTRAINT `fk_uom_id`
  FOREIGN KEY (`uom_id`)
  REFERENCES `grocery_store`.`uom` (`uom_id`)
  ON DELETE RESTRICT
  ON UPDATE NO ACTION;
