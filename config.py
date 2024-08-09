from datetime import timedelta

class Config(object):
	DEBUG = False
	TESTING = False
	DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
	DATABASE_URI = 'mysql+mysqldb://root:1234@127.0.0.1:3306/iris'
 	# DATABASE_URI = 'mysql+mysqldb://root:@127.0.0.1:3306/iris'
	BASE_URL     = 'http://127.0.0.1:5000'
	UPLOAD_FOLDER = '/static/uploads'

	SESSION_TYPE = 'filesystem'
	PERMANENT_SESSION_LIFETIME = timedelta(minutes=120)

class DevelopmentConfig(Config):
	DEBUG = True

class SECRET_KEY(Config):
	SECRET_KEY = '3480d3b6d4c6729a3f31d4f544e0a52f'
