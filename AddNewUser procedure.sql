DELIMITER $$

CREATE PROCEDURE AddNewUser(
    IN p_user_name VARCHAR(255),
    IN p_email VARCHAR(255),
    IN p_user_password VARCHAR(512),
    IN p_date_of_birth DATE,
    IN p_user_id INT
)
BEGIN
    -- Insert new user details into the users table
    INSERT INTO users (User_Name, Email, User_Password, Date_Of_Birth,User_ID)
    VALUES (p_user_name, p_email, p_user_password, p_date_of_birth, p_user_id);
END $$

DELIMITER ;
