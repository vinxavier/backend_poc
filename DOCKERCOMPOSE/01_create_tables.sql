-- Define the business_role_enum enum type
CREATE TYPE business_role_enum AS ENUM ('CompanyAdmin', 'Member', 'Accountant');
CREATE TYPE system_role_enum AS ENUM ('Admin', 'User');

-- Create person table
CREATE TABLE person (
    id SERIAL PRIMARY KEY,
    cognito_id VARCHAR(100),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    birthdate DATE,
    email VARCHAR(255),
    phone_number VARCHAR(20),
    system_role system_role_enum,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    consents JSONB,
    is_active BOOLEAN
);

-- Create company table
CREATE TABLE company (
    id SERIAL PRIMARY KEY,
    address VARCHAR(255),
    name VARCHAR(100),
    country VARCHAR(100),
    id_number VARCHAR(50),
    vat_number VARCHAR(50),
    industry VARCHAR(100),
    detailed_activity VARCHAR(255),
    company_site VARCHAR(255),
    size INT,
    bank_account_country VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN
);

-- Create employment table to represent the many-to-many relationship
CREATE TABLE employment (
    person_id INT REFERENCES person(id),
    company_id INT REFERENCES company(id),
    business_role business_role_enum,
    position VARCHAR(100),
    PRIMARY KEY (person_id, company_id)
);

