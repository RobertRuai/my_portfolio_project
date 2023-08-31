-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS crime_report;
CREATE USER IF NOT EXISTS 'crime_user'@'localhost' IDENTIFIED BY 'crime_pwd';
GRANT ALL PRIVILEGES ON `crime_report`.* TO 'crime_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'crime_user'@'localhost';
FLUSH PRIVILEGES;
