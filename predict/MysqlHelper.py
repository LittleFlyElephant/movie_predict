
from sqlalchemy import create_engine, func, and_
from sqlalchemy.orm import sessionmaker
from Model import MovieModel

def getData():
    engine = create_engine('mysql+mysqlconnector://test:chen123@localhost:3306/movie_imdb')
    Session = sessionmaker(bind = engine)
    session = Session()

    res = session.query(MovieModel).all()
    movies=[]
    for re in res:
        movies.append(getMovie(re))
    return movies

def getMovie(rs):
    movie=[]
    movie.append(float(rs.imdb_score))
    movie.append(getInt(rs.director_facebook_likes))
    movie.append(getInt(rs.duration))
    movie.append(getInt(rs.actor_1_facebook_likes))
    movie.append(getInt(rs.actor_2_facebook_likes))
    movie.append(getInt(rs.actor_3_facebook_likes))
    movie.append(getInt(rs.facenumber_in_poster))
    movie.append(getInt(rs.budget))
    return movie

def getInt(val):
    if len(val)==0:
        return 0
    return int(val)


#     imdb_score
# director_facebook_likes
# duration
# actor_1_facebook_likes
# actor_2_facebook_likes
# actor_3_facebook_likes
# facenumber_in_poster
# budget

