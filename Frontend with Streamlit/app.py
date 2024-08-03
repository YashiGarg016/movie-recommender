import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=a5abf6c3b2f96f98ace0d92029780baa&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

     recommended_mov = []
     recommended_mov_poster = []
     for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_mov.append(movies.iloc[i[0]].title)
        recommended_mov_poster.append(fetch_poster(movie_id))

     return recommended_mov, recommended_mov_poster



movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Flick-Picks')

selected_movie = st.selectbox(
    'Choose a movie!', movies['title'].values
)

if st.button('Recommend!'):
    recs, posters = recommend(selected_movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
      st.text(recs[0])
      st.image(posters[0])

    with col2:
      st.text(recs[1])
      st.image(posters[1])

    with col3:
      st.text(recs[2])
      st.image(posters[2])
 
    with col4:
      st.text(recs[3])
      st.image(posters[3])
    
    with col5:
      st.text(recs[4])
      st.image(posters[4])
  