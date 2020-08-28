import config
import time
from sqlalchemy import Table,MetaData,Column,Integer,String,ForeignKey,Binary,Boolean
from sqlalchemy.orm import mapper
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

# ---INIT---
engine = create_engine(config.db_url, echo=False)
session = scoped_session(sessionmaker(bind=engine,autoflush=False))
Base = declarative_base()

class User(Base):
	__tablename__ = 'bot_user'
	user_id = Column(String, primary_key=True)
	user_name = Column(String)
	language = Column(String)


	def __init__(self, user_id, user_name, language):
		self.user_id = user_id
		self.user_name = user_name,
		self.language = language


	def __repr__(self):
		return "<User(user_id='%s', user_name='%s', language='%s')>" % (
								 self.user_id, self.user_name, self.language)


class DrawProgress(Base):
	__tablename__ = 'draw_progress'
	id = Column(Integer, primary_key=True)
	user_id = Column(String)
	chanel_id = Column(String)
	chanel_name = Column(String)
	text = Column(String)
	file_type = Column(String)
	file_id = Column(String)
	winers_count = Column(Integer)
	post_time = Column(String)
	end_time = Column(String)


	def __init__(self, user_id, chanel_id, chanel_name, text, file_type, file_id, winers_count, post_time, end_time):
		self.user_id = str(user_id)
		self.chanel_id = str(chanel_id)
		self.chanel_name = chanel_name
		self.text = text
		self.file_type = file_type
		self.file_id = file_id
		self.winers_count = winers_count
		self.post_time = post_time
		self.end_time = end_time


	def __repr__(self):
		return "<DrawProgress(id='%s', user_id='%s', chanel_id='%s', chanel_name='%s', text='%s', file_type='%s', file_id='%s', winers_count='%s', post_time='%s', end_time='%s')>" % (
								self.id,
								self.user_id,
								self.chanel_id,
								self.chanel_name,
								self.text,
								self.file_type,
								self.file_id,
								self.winers_count,
								self.post_time,
								self.end_time)

class DrawNot(Base):
	__tablename__ = 'notposted'
	id = Column(Integer, primary_key=True)
	user_id = Column(String)
	chanel_id = Column(String)
	chanel_name = Column(String)
	text = Column(String)
	file_type = Column(String)
	file_id = Column(String)
	winers_count = Column(Integer)
	post_time = Column(String)
	end_time = Column(String)


	def __init__(self, id, user_id, chanel_id, chanel_name, text, file_type, file_id, winers_count, post_time, end_time):
		self.id = id
		self.user_id = str(user_id)
		self.chanel_id = str(chanel_id)
		self.chanel_name = chanel_name
		self.text = text
		self.file_type = file_type
		self.file_id = file_id
		self.winers_count = winers_count
		self.post_time = post_time
		self.end_time = end_time


	def __repr__(self):
		return "<notposted(id='%s', user_id='%s', chanel_id='%s', chanel_name='%s', text='%s', file_type='%s', file_id='%s', winers_count='%s', post_time='%s', end_time='%s')>" % (
								self.id,
								self.user_id,
								self.chanel_id,
								self.chanel_name,
								self.text,
								self.file_type,
								self.file_id,
								self.winers_count,
								self.post_time,
								self.end_time)



class Draw(Base):
	__tablename__ = 'draw_'
	id = Column(Integer, primary_key=True)
	user_id = Column(String)
	message_id = Column(String)
	chanel_id = Column(String)
	chanel_name = Column(String)
	text = Column(String)
	file_type = Column(String)
	file_id = Column(String)
	winers_count = Column(Integer)
	post_time = Column(String)
	end_time = Column(String)


	def __init__(self, id, user_id, message_id, chanel_id, chanel_name, text, file_type, file_id, winers_count, post_time, end_time):
		self.id = id
		self.user_id = str(user_id)
		self.message_id = str(message_id)
		self.chanel_id = str(chanel_id)
		self.chanel_name = chanel_name
		self.text = text
		self.file_type = file_type
		self.file_id = file_id
		self.winers_count = winers_count
		self.post_time = post_time
		self.end_time = end_time


	def __repr__(self):
		return "<DrawProgress(id='%s', user_id='%s', message_id='%s' chanel_id='%s', chanel_name='%s', text='%s', file_type='%s', file_id='%s', winers_count='%s', post_time='%s', end_time='%s')>" % (
								self.id,
								self.user_id,
								self.message_id,
								self.chanel_id,
								self.chanel_name,
								self.text,
								self.file_type,
								self.file_id,
								self.winers_count,
								self.post_time,
								self.end_time)






class SubscribeChannel(Base):
	__tablename__ = 'channel'
	id = Column(Integer, primary_key=True)
	draw_id = Column(Integer)
	user_id = Column(String)
	channel_id = Column(String)


	def __init__(self, draw_id, user_id, channel_id):
		self.draw_id = draw_id
		self.user_id = user_id
		self.channel_id = channel_id


	def __repr__(self):
		return "<channel(id='%s', draw_id='%s', user_id='%s', channel_id='%s')>" % (
			self.id, self.draw_id, self.user_id, self.channel_id)



class DrawPlayer(Base):
	__tablename__ = 'players'
	id = Column(Integer, primary_key=True)
	draw_id = Column(Integer)
	user_id = Column(String)
	user_name = Column(String)


	def __init__(self, draw_id, user_id, user_name):
		self.draw_id = draw_id
		self.user_id = user_id
		self.user_name = user_name


	def __repr__(self):
		return "<Player(draw_id='%s', user_id='%s', user_name='%s')>" % (
			self.draw_id, self.user_id, self.user_name)



class State(Base):
	__tablename__ = 'user_state'
	user_id = Column(Integer, primary_key=True)
	state = Column(String)
	arg = Column(Binary)

	def __init__(self, user_id, state, arg):
		self.user_id = user_id
		self.state = state
		self.arg = arg

	def __repr__(self):
		return "<State(user_id='%s', state='%s', arg='%s')>" % (
								 self.user_id, self.state, self.arg)




