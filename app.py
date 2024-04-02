
import pickle
import streamlit as st
import requests
from streamlit_lottie import st_lottie

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def load_loturl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --ASSETS--
lottie_bot = load_loturl("https://lottie.host/26778581-1a00-4cfe-a3f7-5f5785505488/I1sFdjnwaA.json")


# --PRINCIPAL FUNCTION--
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


# --HEADER SECTION--
st.header('Movie Recommender :wave:')
movies = pickle.load(open('artifacts/movie_list.pkl','rb'))
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))

# --END HEADER--

with st.container():
   left_column, right_column = st.columns(2)

with right_column:
    st_lottie(lottie_bot, height = 100, key= 'bot')


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "search a movie!",
    movie_list
)

if st.button('show me!'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])


st.write("MY SOCIALS!")
st.write("[Github](https://github.com/Samuel-Buarque)     [Linkedin](https://br.linkedin.com/in/samuel-buarque)")

        

