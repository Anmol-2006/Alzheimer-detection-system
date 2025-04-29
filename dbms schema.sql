-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Chat Logs Table
CREATE TABLE IF NOT EXISTS chatlogs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    message TEXT,
    sender ENUM('user', 'bot'),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS knowledge_base;
CREATE TABLE knowledge_base (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic TEXT NOT NULL,
    sub_topic TEXT,
    question TEXT UNIQUE NOT NULL,
    answer TEXT NOT NULL
);

DROP TABLE IF EXISTS chat_history;
CREATE TABLE chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_message TEXT NOT NULL,
    bot_response TEXT
);

-- Sample data related to Alzheimer's
INSERT INTO knowledge_base (topic, question, answer) VALUES
('Overview', 'What is Alzheimer\'s disease?', 'Alzheimer\'s disease is a progressive neurodegenerative disorder that gradually erodes memory and cognitive abilities.');

INSERT INTO knowledge_base (topic, sub_topic, question, answer) VALUES
('Symptoms', 'Early Signs', 'What are the early signs of Alzheimer\'s?', 'Early symptoms often include forgetting recent events or conversations, difficulty with familiar tasks, and problems with language.');

INSERT INTO knowledge_base (topic, sub_topic, question, answer) VALUES
('Symptoms', 'Memory Loss', 'What kind of memory loss is associated with Alzheimer\'s?', 'The memory loss is persistent and worsens over time, affecting the ability to recall recent information, conversations, appointments, and eventually even familiar names.');

INSERT INTO knowledge_base (topic, 'Causes', 'What are the main causes of Alzheimer\'s?', 'The exact causes aren\'t fully understood, but it\'s believed to be a combination of genetic, lifestyle, and environmental factors affecting brain proteins, leading to plaques and tangles.');

INSERT INTO knowledge_base (topic, 'Diagnosis', 'How is Alzheimer\'s disease diagnosed?', 'Diagnosis typically involves a medical history, mental status tests, physical and neurological exams, and sometimes brain imaging and biomarker tests.');

INSERT INTO knowledge_base (topic, 'Treatment', 'Is there a cure for Alzheimer\'s?', 'Currently, there is no cure for Alzheimer\'s disease, but treatments are available to help manage symptoms and slow down the progression in some individuals.');

INSERT INTO knowledge_base (topic, 'Treatment', 'What types of treatments are available?', 'Treatments include medications to help with memory and thinking, as well as strategies to manage behavioral symptoms and provide support for patients and caregivers.');

INSERT INTO knowledge_base (topic, 'Caregiving', 'What are some tips for caregivers?', 'Caregiving for someone with Alzheimer\'s can be challenging. Tips include establishing a routine, simplifying tasks, ensuring safety, and seeking support from family, friends, and support groups.');

INSERT INTO knowledge_base (topic, 'Research', 'What is the current status of Alzheimer\'s research?', 'Research is ongoing in various areas, including understanding the underlying causes, developing new treatments, and improving diagnostic methods.');
