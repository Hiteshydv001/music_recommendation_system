import pickle
import streamlit as st
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import gzip

# Spotify API credentials
CLIENT_ID = "70a9fb89662f4dac8d07321b259eaad7"
CLIENT_SECRET = "4d6710460d764fbbb8d8753dc094d131"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        track_url = track["external_urls"]["spotify"]
        return album_cover_url, track_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png", None

def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    recommended_music_urls = []
    for i in distances[1:11]:  # Loading 10 songs instead of 5
        artist = music.iloc[i[0]].artist
        album_cover_url, track_url = get_song_album_cover_url(music.iloc[i[0]].song, artist)
        recommended_music_posters.append(album_cover_url)
        recommended_music_names.append(music.iloc[i[0]].song)
        recommended_music_urls.append(track_url)

    return recommended_music_names, recommended_music_posters, recommended_music_urls


def decompress_pickle(compressed_file_path):
    with gzip.open(compressed_file_path, 'rb') as f:
        data = pickle.load(f)
    return data


# Load data
music = decompress_pickle('df.pkl.gz')
similarity = decompress_pickle('similarity.pkl.gz')

# Set up Streamlit page
st.set_page_config(page_title="Cool Music Recommender", page_icon="🎧", layout="wide")


# Custom CSS for modern UI design
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #2c3e50, #3498db);  /* Updated gradient background */
        padding: 2rem;
        height: 100vh;  /* Full height for gradient */
        color: white;   /* Default text color */
    }
    .music-card {
        background-color: white;
        border-radius: 15px;
        padding: 15px;
        margin: 10px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s;
    }
    .music-card:hover {
        transform: scale(1.05);
    }
    .music-title {
        font-size: 1.3rem;
        font-weight: bold;
        text-align: center;
        color: #1e3c72; /* Dark text color for contrast */
    }
    .music-desc {
        font-size: 0.9rem;
        text-align: justify;
        margin-bottom: 5px;
    }
    .star-rating {
        text-align: center;
        font-size: 1rem;
        color: gold;
    }
    .header-section {
        text-align: center;
        color: white;
        margin-bottom: 30px;
    }
    .header-section h1 {
        font-size: 3rem;
    }
    .header-section p {
        font-size: 1.2rem;
        max-width: 800px;
        margin: auto;
        opacity: 0.8;
    }
    .recommend-button {
        background-color: #ff4b4b;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 1rem;
    }
    </style>
""", unsafe_allow_html=True)



# Header with project explanation
st.markdown("""
    <div class="header-section">
        <h1>🎧 Cool Music Recommender System</h1>
        <p>
            Welcome to the Cool Music Recommender System! This project provides personalized music recommendations 
            based on your favorite songs. Powered by the Spotify API, it uses music metadata to suggest songs 
            similar to the one you select. Simply choose a song and see our recommendations.
        </p>
    </div>
""", unsafe_allow_html=True)

# Music selection
music_list = music['song'].values
selected_song = st.selectbox(
    "🔍 Type or select a song from the dropdown:",
    music_list,
    help="Choose your favorite song to get recommendations!"
)

# Display recommendations
if st.button('🎶 Show Recommendation'):
    with st.spinner("Loading recommendations..."):
        recommended_music_names, recommended_music_posters, recommended_music_urls = recommend(selected_song)

        st.markdown("<h2 style='text-align: center; color: white;'>Recommended Songs for You</h2>", unsafe_allow_html=True)
        st.markdown("---")

        # Displaying 2 rows, each with 5 recommended songs (total 10)
        for row in range(2):
            cols = st.columns(5)
            for i, col in enumerate(cols):
                song_index = row * 5 + i
                if song_index < len(recommended_music_names):
                    with col:
                        st.markdown('<div class="music-card">', unsafe_allow_html=True)
                        st.markdown(f"<h4 style='text-align: center;'>{recommended_music_names[song_index]}</h4>", unsafe_allow_html=True)
                        st.image(recommended_music_posters[song_index], width=150)
                        if recommended_music_urls[song_index]:
                            embed_url = recommended_music_urls[song_index].replace("/track/", "/embed/track/")
                            st.markdown(f'<iframe src="{embed_url}" width="100%" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>', unsafe_allow_html=True)
                        st.markdown('</div>', unsafe_allow_html=True)  # Close music card div

    st.success("Recommendations loaded successfully!")

# Footer with GitHub and X.com social icons
st.markdown("""
    <style>
    .footer {
        font-size: 0.85rem;
        margin-top: 3rem;
        text-align: center;
        color: #888;
    }
    .social-icons {
        font-size: 1.5rem;
    }
    .social-icons a {
        margin: 0 10px;
        color: inherit;
        text-decoration: none;
    }
    </style>
    <div class="footer">
        <div class="social-icons">
            <a href="https://github.com/Hiteshydv001" target="_blank">🐱‍💻 GitHub</a>
            <a href="https://x.com/Hitesh_0003" target="_blank">🐦 X.com</a>
        </div>
        Made with 💖 using Streamlit and Spotify API
    </div>
""", unsafe_allow_html=True)
