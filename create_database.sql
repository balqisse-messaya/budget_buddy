
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(50),
    first_name VARCHAR(50),
    balance FLOAT,
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    description VARCHAR(100),
    category VARCHAR(100),
    amount DECIMAL(10, 2),
    date DATE,
    type ENUM('withdrawal', 'deposit', 'transfer'),
    id_recipient INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
