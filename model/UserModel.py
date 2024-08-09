from sqlalchemy import create_engine, MetaData, Table, insert, select,update,delete,text
from sqlalchemy.sql import and_, or_
from core import app


engine = create_engine(app.config['DATABASE_URI'],pool_recycle=3600)



class UserModel():
	def __init__(self):
		try:
			self.meta = MetaData()
			self.sample_users = Table("sample_users", self.meta, autoload_with=engine)
			
		except Exception as e:
			print(e)

#---View---
	def get_sample_users(self):
		with engine.connect() as conn:
			stmt    = text("select * from sample_users")
			result  = conn.execute(stmt).all()
			return [dict(r._mapping) for r in result] if result else None

#---Insert---	
	def insert_sample_users(self,data):
		with engine.connect() as conn:
			result = conn.execute(self.sample_users.insert(), data)
			conn.commit()
			return result

#--View---	
	def get_user_data_by_id(self,user_id):
		with engine.connect() as conn:
			stmt = text(f"select * from sample_users where user_id = {user_id};")
			result = conn.execute(stmt).first()
			if result:
				return dict(result._mapping)
			else:
				return None
			
#--Update---

	def update_user_data(self,user_id,data):
		with engine.connect() as conn:
			stmt   = self.sample_users.update().where(self.sample_users.c.user_id.in_([user_id])).values(data)
			result = conn.execute(stmt)
			conn.commit()
			return result
		
#--delete---

	def delete_user_data_by_id(self,user_id):
		with engine.connect() as conn:
			stmt = text(f"delete from sample_users WHERE user_id = {user_id}")
			result = conn.execute(stmt)
			conn.commit()
			return result
		
	
