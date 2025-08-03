-- PostgreSQL / MySQL compatible
CREATE TABLE customers (
  id_customer SERIAL PRIMARY KEY,
  name VARCHAR(100),
  description VARCHAR(255),
  email VARCHAR(150),
  age INT
);

CREATE TABLE plans (
  id_plan SERIAL PRIMARY KEY,
  name VARCHAR(100),
  price INT,
  description VARCHAR(255)
);

CREATE TABLE transactions (
  id_transaction SERIAL PRIMARY KEY,
  id_customer INT NOT NULL REFERENCES customers(id_customer),
  amount INT NOT NULL,
  description VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE invoices (
  id_invoice SERIAL PRIMARY KEY,
  id_customer INT NOT NULL REFERENCES customers(id_customer),
  total INT NOT NULL,
  issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Enum type (PostgreSQL syntax)
CREATE TYPE plan_status_type AS ENUM ('active', 'inactive');

CREATE TABLE customer_plans (
  id_customer INT NOT NULL REFERENCES customers(id_customer),
  id_plan INT NOT NULL REFERENCES plans(id_plan),
  status plan_status_type NOT NULL,
  PRIMARY KEY (id_customer, id_plan)
);
