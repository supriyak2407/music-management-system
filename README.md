# Musicana - Music Management System

## Project Overview


**Introduction:**
Musicana is a robust Music Management System designed to meet the diverse needs of artists, record labels, and music enthusiasts. The system integrates powerful features for exploring, managing, and elevating musical journeys. Users can log in to unlock a world of musical possibilities, curate their own experiences, discover new music, and stay updated on musical trends.

## Database Design

### Tables and Schemas
- **Artist:** Artist_ID, Name, Birthdate, Nationality, Gender, Height
- **Label:** Label_ID, Label_Name, Country, Founded_Year, Headquarters
- **Album:** Album_ID, Album_Title, Release_Date, Artist_ID, Label_ID
- **Genre:** Genre_ID, Genre_Name
- **Song:** Song_ID, Song_Title, Time_Period, Musical_Key, Album_ID, Artist_ID, Genre_ID
- **Users:** User_ID, User_Name, Email, User_Password, Date_Of_Birth
- **Playlists:** Playlist_ID, Playlist_Name, Created_Date, User_ID
- **User_Song_Rating:** User_Song_Rating_ID, Rating, User_ID, Song_ID
- **User_Favourite_Song_and_Album:** ID, Song_ID, Album_ID
- **Billboard_Chart_Data:** Chart_ID, Song_ID, Daily_Rank, Daily_Movement, Weekly_Movement
- **Song_Features:** Feature_ID, Danceability, Energy, Loudness, Mode, Speechiness, Acousticness, Instrumentalness, Liveness, Valence, Tempo, Time_Signature, Song_ID
- **Awards:** Award_ID, Award_Name, Song_ID

### Design Decisions
- Many-to-Many, One-to-Many, Many-to-One, One-to-One relations identified.
- Normalization in the 3rd Normal Form for efficient and structured data.

### Final ERD

![ERD Image]("C:\Users\91998\Desktop\musicfinalproject.jpg")


## Use of Triggers, Functions, Stored Procedures, and Views

### Stored Procedures (11)
1. New user registration.
2. Song search based on a term.
3. Retrieve artist information by Artist_ID.
4. List top-rated songs based on user ratings.
5. Update information about a specific artist.
6. Retrieve billboard chart data for a song.
7. Calculate average song duration for each genre.
8. Add songs to user favorites.
9. Add songs to user playlist.
10. Delete songs from user playlist.
11. Delete songs from user favorites.

### Functions (3)
1. GetTotalAlbumsByArtist
2. GetGenreForSong
3. GetMostRecentAlbumReleaseDate

### Triggers (1)
- Prevent deletion of a song if it has received awards.

### Views (3)
1. TopRatedSongs
2. LabelAlbumStatistics
3. GenreStatistics

## Data Sources

Data primarily from Spotify Datasets on Kaggle, including artists.csv and tracks.csv. Manual efforts for refinement and completion of attributes within Artist, Album, and Song tables.

[Link to Kaggle Dataset](https://www.kaggle.com/datasets/lehaknarnauli/spotify-datasets?select=artists.csv)

## Application Description

### Features
1. Log-in/Sign-up
2. Homepage - Play songs, add to favorites/playlists
3. Album Page - Play album songs, add to favorites/playlists
4. Playlists - View and manage user playlists
5. Billboard Chart Data - Song rankings and movement
6. Favorites - View and manage favorite songs
7. Trends - Analytical insights based on user data
8. Queries - Run SQL queries on the database

### Analysis

1. Popular Songs - Top 5 songs based on play counts.
2. User Activity - Daily user activity chart.
3. Song Length Distribution - Distribution of song lengths.

The final ERD and the application snippets can be seen in the images.pdf file.

## Conclusion

Musicana, our Music Management System, offers an immersive music experience. Although a sophisticated recommendation system was not included due to time constraints, the system is poised for future enhancements. The use of SQL queries and analytical tools adds a unique dimension to the platform.

---
