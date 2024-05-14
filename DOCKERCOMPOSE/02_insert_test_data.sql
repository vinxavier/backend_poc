-- Insert sample data into the person table
INSERT INTO person (cognito_id, first_name, last_name, birthdate, email, phone_number, system_role, created_at, updated_at, consents, is_active) VALUES
    ('cognito_id_1', 'John', 'Doe', '1990-01-01', 'john@example.com', '123-456-7890', 'Admin', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '{"consent1": true}', TRUE),
    ('cognito_id_2', 'Alice', 'Smith', '1995-05-15', 'alice@example.com', '987-654-3210', 'User', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '{"consent2": true}', TRUE),
    ('cognito_id_3', 'Bob', 'Johnson', '1985-09-30', 'bob@example.com', '555-555-5555', 'User', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, '{"consent3": true}', TRUE);

-- Insert sample data into the company table
INSERT INTO company (address, name, country, id_number, vat_number, industry, detailed_activity, company_site, size, bank_account_country, created_at, updated_at, is_active) VALUES
    ('123 Main St', 'Tech Corp', 'USA', '123456789', '987654321', 'Technology', 'Software Development', 'https://www.techcorp.com', 100, 'USA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, TRUE),
    ('456 Elm St', 'Health Inc', 'USA', '987654321', '123456789', 'Healthcare', 'Medical Services', 'https://www.healthinc.com', 50, 'USA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, TRUE),
    ('789 Oak St', 'Consulting Co', 'USA', '456789123', '456123789', 'Consulting', 'Business Consulting', 'https://www.consultingco.com', 200, 'USA', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, TRUE);

-- Insert sample data into the employment table
INSERT INTO employment (person_id, company_id, business_role, position) VALUES
    (1, 1, 'CompanyAdmin', 'CEO'),
    (2, 1, 'Member', 'Software Engineer'),
    (3, 2, 'Member', 'Doctor'),
    (1, 3, 'Accountant', 'Financial Analyst');