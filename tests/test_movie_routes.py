from flask.testing import FlaskClient

from src.models import Movie, db
#from tests.utils import create_movie, refresh_db
#, db


def test_get_all_movies(test_app: FlaskClient):
    
    # Setup
    test_movie = Movie(title='Star Wars', director='George Lucas', rating=5)    
    db.session.add(test_movie)
    db.session.commit()

    # Run action
    res = test_app.get('/movies')
    page_data: str = res.data.decode()

    assert res.status_code == 200
    assert  f'<td><a href="/movies/{test_movie.movie_id}">Star Wars</a></td>' in page_data
    assert '<td>George Lucas</td>' in page_data
    assert '<td>5</td>' in page_data