CREATE VIEW LabelAlbumStatistics AS
SELECT
    l.Label_ID,
    l.Label_Name,
    l.Country AS Label_Country,
    COUNT(DISTINCT a.Album_ID) AS Total_Albums
FROM
    Label l
LEFT JOIN
    Album a ON l.Label_ID = a.Label_ID
WHERE
    a.Album_ID IS NOT NULL
GROUP BY
    l.Label_ID, l.Label_Name, l.Country;
