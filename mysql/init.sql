CREATE DATABASE IF NOT EXISTS nlp_db;

USE nlp_db;

CREATE TABLE IF NOT EXISTS news (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title TEXT,
    content MEDIUMTEXT,
    font VARCHAR(255),
    publish_date DATETIME,
    processed BOOLEAN DEFAULT 0
);

CREATE TABLE IF NOT EXISTS topics_entities (
    news_id INT PRIMARY KEY,
    topic INT,
    persons TEXT,
    organizations TEXT,
    locations TEXT,
    FOREIGN KEY (news_id) REFERENCES news(id)
);
