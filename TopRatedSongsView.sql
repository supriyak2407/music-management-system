CREATE VIEW TopRatedSongs AS
SELECT
    s.Song_ID,
    s.Song_Title,
    a.Full_Name AS Artist_Name,
    AVG(usr.Rating) AS Average_Rating
FROM
    Song s
JOIN
    User_Song_Rating usr ON s.Song_ID = usr.Song_ID
JOIN
    Artist a ON s.Artist_ID = a.Artist_ID
GROUP BY
    s.Song_ID, s.Song_Title, a.Full_Name;            
