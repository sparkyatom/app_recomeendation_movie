import streamlit as st
import pickle
import pandas as pd
import requests
import requests
import numpy as np

def fetch_movie_poster(movie_title, api_key):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if 'Poster' in data and data['Poster'] != 'N/A':
        poster_url = data['Poster']
        # Now you can use this poster URL to display the image or download it
        return (poster_url)
    else:
        print("No poster found for this movie.")

# Replace 'your_api_key' with your actual OMDb API key
api_key = 'ed7d4a0'
movie_title = 'Inception'  # Example movie title
fetch_movie_poster(movie_title, api_key)

similarity1 = pickle.load(open('similarity1.pkl','rb'))
similarity2 = pickle.load(open('similarity2.pkl','rb'))

movies_dict = pickle.load(open('MOVIES_dict.pkl','rb'))
movies_dict=pd.DataFrame(movies_dict)
st.title("Movie Recomender System")
def recommend(movie):
    #fetching event
    movie_index = movies_dict[movies_dict['title'] == movie].index[0]
    distance1=similarity1[movie_index]
    distance2=similarity2[movie_index]
    
    distance=np.concatenate((distance1,distance2),axis=0)
    movies_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    re=[]
    for i in movies_list:
        movie_id=i[1]
        re.append(movies_dict.iloc[i[0]].title)
    return re
option = st.selectbox(
    "Search some movies my brother",
    movies_dict['title'].values)
def fetch_poster(movie_id):
    pass
    
if st.button('RECOMEND'):
    import time
    with st.spinner('Wait for it...'):
         time.sleep(1)
    rm=recommend(option)
    for i in rm:
     #st.write(i)
     poster_url = fetch_movie_poster(i, api_key)

rm=recommend(option)
l=[] 
k=0
import time
with st.spinner('Wait for it...'):
         time.sleep(1)
for i in rm:
    #st.write(i)
    l.append(i)
#st.write(l)
col1, col2 = st.columns(2)

with col1:
   st.header(l[0])
   st.image(fetch_movie_poster(l[0], api_key))

with col2:
   st.header(l[1])
   st.image(fetch_movie_poster(l[1], api_key))
col3, col4 = st.columns(2)
with col3:
   st.header(l[2])
   st.image(fetch_movie_poster(l[2], api_key))
with col4:
   st.header(l[3])
   st.image(fetch_movie_poster(l[3], api_key))
col5,col6= st.columns(2)
with col5:
   st.header(l[4])
   st.image(fetch_movie_poster(l[4], api_key))