
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50),
    balance FLOAT,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255)
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category VARCHAR(100),
    amount DECIMAL(10, 2),
    date DATE,
    type ENUM('withdrawal', 'deposit', 'transfer') NOT NULL,
    id_recipient INT,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
