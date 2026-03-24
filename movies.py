import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies_data=pd.read_csv(r"C:\Users\DELL\Desktop\MovieRecommendation\movies.csv")
movies_data.head()
selected_features=['genres','keywords','tagline','cast','director']
for feature in selected_features:
  movies_data[feature]=movies_data[feature].fillna('')
combined_features=movies_data['genres']+" "+movies_data['keywords']+" "+movies_data['tagline']+' '+movies_data['cast']+" "+movies_data['director']
vectorizer=TfidfVectorizer()
feature_vectors=vectorizer.fit_transform(combined_features)
movie_name=input("Enter Your Favourite Movie Name:")
listofallmovienames=movies_data['title'].tolist()
close_match=difflib.get_close_matches(movie_name,listofallmovienames)
very_close_mathch=close_match[0]
index_movie=movies_data[movies_data['title']==very_close_mathch]['index'].values[0]
similarity=cosine_similarity(feature_vectors)
listofallmovienames=movies_data['title'].tolist()
close_match=difflib.get_close_matches(movie_name,listofallmovienames)
very_close_mathch=close_match[0]
similarity_score=list(enumerate(similarity[index_movie]))
sort_movies=sorted(similarity_score,key= lambda x:x[1],reverse=True)
print("Movies that Suggested for you:\n")
i=1
for movie in sort_movies:
  index=movie[0]
  title_from_index=movies_data[movies_data['index']==index]['title'].values[0]
  if (i<10):
    print(i,'.',title_from_index)
    i=i+1
