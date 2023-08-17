import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

   #Generics
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable = False)
    email = Column(String(200), nullable = False)
    name = Column(String(50), nullable = False)
    last_name = Column(String(50), nullable = True)
    birth_day = Column(String(8), nullable = False)
    age = Column(Integer, nullable = True)
    personal_description = Column(String(30), nullable = True)

    #Relations
    posts = relationship("Post", back_populates = "user")
    likes = relationship("Like", back_populates = "user")
    commets = relationship("Comment", back_populates = "user")
    stories = relationship("Story", back_populates = "user")
    followers = relationship("Follower", back_populates = "user")

class Post(Base):
    __tablename__ = 'post'

    #Generics
    id = Column(Integer, primary_key = True)
    content = Column(String(5000), nullable = False)

    #Relations
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False) 
    likes = relationship("Like", back_populates = "post")
    posts = relationship("Post", back_populates = "post")
    commets = relationship("Comment", back_populates = "user")


class Like(Base):
    __tablename__ = 'like'

    #Generics
    id = Column(Integer, primary_key = True)

    #Relations
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False) 
    comment_id = Column(Integer, ForeignKey("comment.id"), nullable=False)
    story_id = Column(Integer, ForeignKey("story.id"), nullable=False) 

class Comment(Base):
    __tablename__ = 'comment'

    #Generics
    id = Column(Integer, primary_key = True)

    #Relations
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False) 
    comment_id = Column(Integer, ForeignKey("comment.id"), nullable=False)
    likes = relationship("Like", back_populates = "comment")


class Story(Base):
    __tablename__ = 'story'

    #Generics
    id = Column(Integer, primary_key = True)
    content = Column(String(30), nullable = False)
    message = Column(String(30), nullable = True)

    #Relations
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    likes = relationship("Like", back_populates = "story")

class Follower(Base):
    __tablename__ = 'follower'

    #Generics
    id = Column(Integer, primary_key = True)

    #Relations
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
