USE askdb_db;
drop table if exists departments;
drop table if exists users;
drop table if exists clients;
drop table if exists projects;
drop table if exists sales;
drop table if exists tasks;

-- ------------------------------
-- 表1：departments 部门表
-- ------------------------------
CREATE TABLE departments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    manager_id INT
);

-- ------------------------------
-- 表2：users 员工表
-- ------------------------------
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    department_id INT,
    hire_date DATE,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- ------------------------------
-- 表3：clients 客户表
-- ------------------------------
CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    industry VARCHAR(50),
    location VARCHAR(50)
);

-- ------------------------------
-- 表4：projects 项目表
-- ------------------------------
CREATE TABLE projects (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department_id INT,
    start_date DATE,
    end_date DATE,
    budget DECIMAL(10,2),
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

-- ------------------------------
-- 表5：sales 销售记录表
-- ------------------------------
CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sale_date DATE NOT NULL,
    employee_id INT,
    client_id INT,
    project_id INT,
    amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES users(id),
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (project_id) REFERENCES projects(id)
);

-- ------------------------------
-- 表6：tasks 员工任务表
-- ------------------------------
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    project_id INT,
    task_name VARCHAR(100),
    status VARCHAR(20), -- pending/completed
    hours_spent DECIMAL(5,2),
    FOREIGN KEY (employee_id) REFERENCES users(id),
    FOREIGN KEY (project_id) REFERENCES projects(id)
);




INSERT INTO departments (id, name) VALUES
(1, '技术'),
(2, '销售'),
(3, '客服'),
(4, '市场'),
(5, '人事');

INSERT INTO users (name, email, department_id, hire_date, salary) VALUES
('Alice', 'alice@example.com', 1, '2023-01-15', 8000),
('Bob', NULL, 2, '2022-06-20', 6000),
('Charlie', 'charlie@example.com', 3, '2023-03-10', 5000),
('David', 'david@example.com', 1, '2021-11-05', 9000),
('Eva', NULL, 2, '2022-08-18', 6200),
('Frank', 'frank@example.com', 4, '2022-02-10', 7000),
('Grace', 'grace@example.com', 5, '2021-09-12', 6500),
('Hank', NULL, 1, '2023-04-01', 7800),
('Ivy', 'ivy@example.com', 3, '2022-11-05', 5200),
('Jack', NULL, 2, '2023-01-25', 6100);

INSERT INTO clients (name, industry, location) VALUES
('客户A', '互联网', '北京'),
('客户B', '金融', '上海'),
('客户C', '制造', '深圳'),
('客户D', '教育', '广州'),
('客户E', '医疗', '成都');

INSERT INTO projects (name, department_id, start_date, end_date, budget) VALUES
('项目X', 1, '2025-08-01', '2025-09-30', 50000),
('项目Y', 2, '2025-08-15', '2025-09-20', 30000),
('项目Z', 3, '2025-07-10', '2025-09-10', 20000),
('项目M', 4, '2025-08-05', '2025-09-25', 40000),
('项目N', 5, '2025-07-20', '2025-09-15', 25000);

INSERT INTO sales (sale_date, employee_id, client_id, project_id, amount) VALUES
('2025-09-01', 1, 1, 1, 1200),
('2025-09-02', 2, 1, 2, 1500),
('2025-09-03', 1, 2, 1, 1300),
('2025-09-04', 3, 2, 3, 1600),
('2025-09-05', 4, 1, 1, 1800),
('2025-09-05', 5, 3, 2, 1400),
('2025-09-06', 6, 4, 4, 2000),
('2025-09-06', 7, 5, 5, 1700),
('2025-09-07', 8, 2, 1, 1600),
('2025-09-07', 9, 3, 3, 1300),
('2025-09-08', 10, 4, 2, 1500),
('2025-09-08', 1, 1, 1, 1800),
('2025-09-09', 2, 2, 2, 1200),
('2025-09-09', 3, 3, 3, 1400),
('2025-09-10', 4, 5, 1, 1900);

INSERT INTO tasks (employee_id, project_id, task_name, status, hours_spent) VALUES
(1, 1, '开发模块A', 'completed', 12),
(2, 2, '销售跟进', 'completed', 8),
(3, 3, '客服支持', 'pending', 5),
(4, 1, '开发模块B', 'completed', 15),
(5, 2, '销售电话', 'completed', 7),
(6, 4, '市场调研', 'completed', 10),
(7, 5, '招聘流程', 'pending', 6),
(8, 1, '开发模块C', 'completed', 9),
(9, 3, '客户培训', 'completed', 8),
(10, 2, '销售合同整理', 'completed', 7);
