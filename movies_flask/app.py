from flask import Flask, render_template, request
import imdb

app = Flask(__name__)
ia = imdb.Cinemagoer()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        movie_name = request.form.get('movie_name')
        items = ia.search_movie(movie_name)
        return render_template('results.html', items=items, movie_name=movie_name)
    return render_template('index.html')

@app.route('/movie/<int:movie_id>')
def movie_info(movie_id):
    movie_info = ia.get_movie(movie_id)
    return render_template('movie_info.html', movie_info=movie_info)

if __name__ == '__main__':
    app.run(debug=True)
