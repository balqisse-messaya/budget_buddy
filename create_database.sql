CREATE DATABASE budget_buddy;

USE budget_buddy;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(50),
    first_name VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    balance FLOAT
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    description VARCHAR(100),
    category VARCHAR(2100),
    amount DECIMAL(10, 2),
    date DATE,
    type ENUM('withdrawal', 'deposit', 'transfer'),
    id_recipient INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
