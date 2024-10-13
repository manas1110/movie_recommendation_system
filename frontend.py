import pickle
import streamlit as st
import pandas as pd

def recommend(movie):
    index = movies[movies['name'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:7]:
        movie_data = {
            'name': movies.iloc[i[0]]['name'],
            'image': movies.iloc[i[0]]['image']  # Assuming there is an 'image' column
        }
        recommended_movies.append(movie_data)
    return recommended_movies

# Page background styling
page_bg_img = '''
<style>
.stApp {
  background-image: url("https://www.shutterstock.com/shutterstock/photos/1655872747/display_1500/stock-vector-clean-sky-blue-gradient-background-with-text-space-editable-blurred-white-blue-vector-illustration-1655872747.jpg");
  background-size: cover;
}
.title {
  font-size: 50px;
  color: black;
  text-align: center;
  margin-bottom: 30px;
  font-weight: bold;
}
.center-button {
  display: flex;
  justify-content: center;
  margin-top: 20px;
  align-items: center;


}
.stButton button {
  background-color: #1DA1F2;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  margin-left:200px;
  border-radius: 5px;
  transition: all 0.3s ease;  /* Smooth transition for hover effect */
  
}
.stButton button:hover {
  transform: scale(1.1);  /* Slightly increase the button size on hover */
}
.movie-container {
  display: flex;
  justify-content: space-around;
  margin-bottom: 30px;
}
.movie-box {
  text-align: center;
  margin: 10px;
}
.movie-image {
  width: 200px;
  height: 300px;
  border-radius: 10px;
}
.movie-name {
  font-size: 18px;
  font-weight: bold;
  color: #333;
  margin-top: 10px;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)
st.markdown('<div class="title">Movie Recommendation System</div>', unsafe_allow_html=True)

# Load movie data and similarity matrix
movies = pickle.load(open('pkl_file/movie_list.pkl', 'rb'))
similarity = pickle.load(open('pkl_file/similarity.pkl', 'rb'))

# Search bar with placeholder inside (shows "Type movie here")
selected_movie = st.selectbox(" ",movies['name'].values,index=None,placeholder="Select or Write Movie Here")

# Center the "Show Recommendation" button
st.markdown('<div class="center-button">', unsafe_allow_html=True)
if st.button('Show Recommendation'):
    recommended_movies = recommend(selected_movie)

    # Display movies in a row with proper alignment
    for row_start in range(0, len(recommended_movies), 3):
        cols = st.columns(3)  # 3 movies per row
        for i, movie in enumerate(recommended_movies[row_start:row_start+3]):
            with cols[i]:
                st.markdown(f'''
                <div class="movie-box">
                    <img class="movie-image" src="{movie['image']}" alt="{movie['name']}" />
                    <div class="movie-name">{movie['name']}</div>
                </div>
                ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
