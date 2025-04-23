-- This is a sample SQL script

-- Create a table
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    UserName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO Users (UserID, UserName, Email) VALUES
(1, 'JoshuaJohnson', 'joshuadallasjohnson@hotmail.com'),
(2, 'JaneSmith', 'janesmith@example.com');

-- Query the table
SELECT * FROM Users;