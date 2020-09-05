import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer,primary_key=True)
    user_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    profile_picture = Column(String(250), nullable=False)
    posts = relationship("Post",backref="author",foreign_keys="post.user_id") #uselist=False-->para que no sea una lista relationship 1 -1
    stories=relationship("Story",backref="stories",foreign_keys="story.user_id")
    like_post = relationship("Like_post",back_populates="user")
    comment = relationship("Comment",back_populates="user")
    def to_dict(self):
        return {}

class Post(Base):
    __tablename__="post"
    id = Column(Integer,primary_key=True)
    picture= Column(String(250),nullable=False)
    user_id=Column(Integer,ForeignKey('user.id'))
    filter_id=Column(Integer,ForeignKey('filter.id'))
    caption=Column(String,nullable=False)
    comment_id=Column(Integer,ForeignKey('comment.id'))
    comment=relationship("Comment")
    filters=relationship("Filter",backref="filter")
    like=relationship("Like_post",backref="like")
    like_comment=relationship("Like_comment",backref="like_comment")
    def to_dict(self):
        return {}


# class Public(Base):
#     __tablename__ = 'public'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     picture= Column(String(250))
#     id_filtro=Column(String,nullable=False)
#     story=Column(String,nullable=False)
#     caption=Column(String,nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id')) #nombre de la tabla NO DE LA CLASE !
#     def to_dict(self):
#         return {}

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key=True)
    post_id=Column(Integer,ForeignKey('post.id'))
    emojis=Column(String,nullable=False)
    user_id=Column(Integer,ForeignKey('user.id'))
    filter_id=Column(Integer,ForeignKey('filter.id'))
    def to_dict(self):
        return {}

class Filter(Base):
    __tablename__="filter"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__="comment"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('user.id'))
    post_id=Column(Integer,ForeignKey('post.id'))
    user=relationship("User",back_populates="comment")
    def to_dict(self):
        return {}

class Like_post(Base):
    __tablename__="like_post"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('user.id'))
    post_id=Column(Integer,ForeignKey('post.id'))
    user=relationship("User",back_populates="like_post")

class Like_comment(Base):
    __tablename__="like_comment"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey('user.id'))
    post_id=Column(Integer,ForeignKey('post.id'))
    user=relationship("User",back_populates="like")
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')