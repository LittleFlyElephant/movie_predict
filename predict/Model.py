# encoding: utf-8
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INT, String
from sqlalchemy.dialects.mysql import DOUBLE

Base = declarative_base()

class MovieModel(Base):
    __tablename__ = 'movie'
    id = Column(INT, primary_key=True)
    color = Column(String)
    director_name = Column(String)
    num_critic_for_reviews = Column(String)
    duration = Column(String)
    director_facebook_likes = Column(String)
    actor_3_facebook_likes = Column(String)
    actor_2_name = Column(String)
    actor_1_facebook_likes = Column(String)
    gross = Column(String)
    genres = Column(String)
    actor_1_name = Column(String)
    movie_title = Column(String)
    num_voted_users = Column(String)
    cast_total_facebook_likes = Column(INT)
    actor_3_name = Column(String)
    facenumber_in_poster = Column(String)
    plot_keywords = Column(String)
    movie_imdb_link = Column(String)
    num_user_for_reviews = Column(String)
    lang = Column(String)
    country = Column(String)
    content_rating = Column(String)
    budget = Column(String)
    title_year = Column(String)
    actor_2_facebook_likes = Column(String)
    imdb_score = Column(DOUBLE)
    aspect_ratio = Column(String)
    movie_facebook_likes = Column(INT)