-- creates the MySQL server user user_0d_1
-- creates a new user
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
-- grants privileges
GRANT ALL PRIVILEGES ON * . * TO user_0d_1@localhost;
(base) vinny@Vincents-MacBook-Pro 0x0E-SQL_more_queries % cat 2-create_read_user.sql
-- creates the database hbtn_0d_2 and the user user_0d_2
-- creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates a user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- grants SELECT privileges to a user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
