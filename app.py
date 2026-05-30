from flask import Flask, render_template, request
import pickle
import requests

app = Flask(__name__)

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    api_key = "PASTE_YOUR_API_KEY_HERE"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    return "https://image.tmdb.org/t/p/w500/" + poster_path if poster_path else ""

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
