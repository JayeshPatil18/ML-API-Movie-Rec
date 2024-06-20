from flask import Flask,request,jsonify
import numpy as np
import pickle
import requests
from flask_cors import CORS
# import sys

# Risky Code added
num_parts = 8
combined_parts = []
for i in range(1, num_parts + 1):
    filename = f'part{i}.pkl'
    with open(filename, 'rb') as f:
        part = pickle.load(f)
        combined_parts.append(part)
        print(f"Part {i} loaded from {filename}")

# Combine all parts into a complete dataset
similarity = np.concatenate(combined_parts, axis=0)

# similarity = pickle.load(open('similarity.pkl','rb'))
main_df = pickle.load(open('main.pkl','rb'))

app = Flask(__name__)
CORS(app)

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# Functions
def recommend(movie):
    index = main_df[main_df['title'].str.lower() == movie.lower()].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    
    movieIds = []
    # Range from 1 to 100
    for i in distances[1:71]:
        movieIds.append(main_df.iloc[i[0]].movie_id)
    return movieIds

def movies(input):

    recommended_movie_ids = []
    
    for i in range(len(input)):
        recommended_movie_ids += recommend(input[i])


    similar_movie_df = main_df[main_df['movie_id'].isin(recommended_movie_ids)]
    similar_movie_df = similar_movie_df.drop_duplicates(subset='movie_id')
    
    recommended_movie = similar_movie_df.sort_values(by='vote_count', ascending=False)

    return recommended_movie


@app.route('/')
def index():
    return "Hello world"

@app.route('/movies')
def movies():
    
    try:
        
        movies_df = main_d.head(50)

        movies_json = movies_df.to_json(orient='records')
        return jsonify({'recommendations':str(movies_json)})

    except Exception as e:
        
        return jsonify({"error": str(e)}), 500


@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json()
    input_movies = data.get('movielist')

    try:

        movies_df = movies(input_movies).head(50)

        # Fetch Images 
        # for index, row in movies_df.iterrows():
        #     movie_id = row['id']
        #     poster_url = fetch_poster(movie_id)
        #     print(f'###{poster_url}', file=sys.stderr)
        #     movies_df.at[index, 'poster_path'] = poster_url

        movies_json = movies_df.to_json(orient='records')
        return jsonify({'recommendations':str(movies_json)})

    except Exception as e:

        # if "out of bounds" in str(e):
        #     return jsonify({"error": "entered movie on in dataset"}), 49

        # print(f'Error: {e}', file=sys.stderr)  # Print any error to stderr
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
