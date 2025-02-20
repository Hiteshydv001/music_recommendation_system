Cool Music Recommender
======================

**Deployment Link:** [Demo at Streamlit](https://content-based-movie-recommend.streamlit.app/)
=========================================

![Screenshot](https://github.com/Hiteshydv001/music_recommendation_system/blob/main/Screenshot%202024-10-21%20013114.png)

![Screenshot](https://github.com/Hiteshydv001/music_recommendation_system/blob/main/Screenshot%202024-10-21%20013142.png)



Overview
--------

The **Cool Music Recommender** is a web application built with Streamlit that provides personalized music recommendations based on users' favorite songs. Leveraging the power of the Spotify API and a music similarity model, users can easily find new music they might enjoy.

Features
--------

*   **Personalized Recommendations**: Get song recommendations based on your favorite tracks.
    
*   **User-Friendly Interface**: A modern and intuitive UI designed using Streamlit for an engaging user experience.
    
*   **Music Metadata**: Displays album covers, song titles, and Spotify links for easy access to music.

Structure:
----------

```
Directory structure:
└── hiteshydv001-music_recommendation_system/
    ├── README.md
    ├── Model Training.ipynb
    ├── app.py
    ├── df.pkl.gz
    ├── requirements.txt
    └── similarity.pkl.gz

```
    

Technologies Used
-----------------

*   **Python**: The primary programming language for backend development.
    
*   **Streamlit**: A framework for building interactive web applications in Python.
    
*   **Spotipy**: A lightweight Python library for the Spotify Web API.
    
*   **Pandas**: For data manipulation and analysis.
    

Usage
-----

*   Type or select a song from the dropdown menu.
    
*   Click the **Show Recommendation** button to retrieve personalized song recommendations.
    
*   The application will display a list of recommended songs along with album covers and links to listen on Spotify.
