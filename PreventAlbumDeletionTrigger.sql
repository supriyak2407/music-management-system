DELIMITER $$

CREATE TRIGGER PreventAlbumDeletion
BEFORE DELETE ON Song
FOR EACH ROW
BEGIN
    DECLARE awardCount INT;

    -- Check if the album has received any awards
    SELECT COUNT(*) INTO awardCount
    FROM Awards
    WHERE Song_ID = OLD.Song_ID;

    -- If the album has received awards, prevent deletion
    IF awardCount > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot delete album with associated awards';
    END IF;
END $$

DELIMITER ;

