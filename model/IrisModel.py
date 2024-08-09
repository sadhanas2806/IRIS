from sqlalchemy import create_engine, MetaData, Table, insert, select,update,delete,text
from sqlalchemy.sql import and_, or_
from core import app


engine = create_engine(app.config['DATABASE_URI'],pool_recycle=3600)

class IrisModel():
	def __init__(self):
		try:
			self.meta = MetaData()
			self.user = Table("user", self.meta, autoload_with=engine)
			self.user_by_id = Table("user", self.meta, autoload_with=engine)
			self.add_to_cart = Table("add_to_cart", self.meta, autoload_with=engine)
			self.total_product_amount = Table("add_to_cart", self.meta, autoload_with=engine)
			self.yourorders= Table("add_to_cart", self.meta, autoload_with=engine)


   			
   
			
		except Exception as e:
			print(e)	
#    view
	def get_user(self):
		with engine.connect() as conn:
			stmt    = text("select * from user ")
			result  = conn.execute(stmt).all()
			return [dict(r._mapping) for r in result] if result else None

	

#---Insert---	
	def insert_user(self,data):
		with engine.connect() as conn:
			result = conn.execute(self.user.insert(), data)
			conn.commit()
			return result

	def get_user_by_id(self,user_id):
		with engine.connect() as conn:
			stmt    = text(f"select * from user where user_id={user_id}")
			print(stmt)
			result = conn.execute(stmt).first()
			results = dict(result._mapping) if result else None
			return results 

	def update_user(self,data):
		with engine.connect() as conn:
			result = conn.execute(self.user.update(), data)
			conn.commit()
			return result

	def check_user_data(self,email_id):
		with engine.connect() as conn:
			stmt    = text(f"select * from user where user_email='{email_id}'")
			result = conn.execute(stmt).first()
			results = dict(result._mapping) if result else None
			return results
		
	def check_user_email(self,email_id):
		with engine.connect() as conn:
			stmt    = text(f"select * from user where user_email='{email_id}'")
			result  = conn.execute(stmt).all()
			return [dict(r._mapping) for r in result] if result else None

	
	def get_product_type(self,product_type):
		with engine.connect() as conn:
			stmt    = text(f"select * from products where product_type = '{product_type}'")
			result  = conn.execute(stmt).all()
			# Result
			# [{"key1":"value1","key2":"value2"},{"key1":"value1","key2":"value2"},{"key1":"value1","key2":"value2"}]
			return [dict(r._mapping) for r in result] if result else None

	def get_user_add_to_cart(self,user_id):
		with engine.connect() as conn:
			stmt    = text("select * from add_to_cart a"
							+" inner join user u on a.user_id = u.user_id"
							+" inner join products p  on a.product_id = p.product_id"
							+" where u.user_id= "+str(user_id)+" and product_status=0;")
			result  = conn.execute(stmt).all()
			return [dict(r._mapping) for r in result] if result else None
#---Insert---	
	def insert_add_to_cart(self,data):
			print("insert_add_to_cart")
			with engine.connect() as conn:
				result = conn.execute(self.add_to_cart.insert(), data)
				conn.commit()
				return result

	def delete_add_to_cart(self,added_id):
			with engine.connect() as conn:

				print('in Delete Function')
				print(added_id)
				stmt = self.add_to_cart.delete().where(self.add_to_cart.c.added_id.in_([added_id]))
				result = conn.execute(stmt)
				conn.commit()
				return result
				

	def get_summary(self,user_id):
		with engine.connect() as conn:
			stmt    = text("select sum(a.total_product_amount) as total_product_amount from add_to_cart a"
							+" inner join user u on a.user_id = u.user_id"
							+" inner join products p  on a.product_id = p.product_id"
							+" where u.user_id= "+str(user_id)+" and product_status = 0;")
			print(stmt)
			result = conn.execute(stmt).first()
			results = dict(result._mapping) if result else None
			return results 

	def get_yourorders(self,user_id):
		with engine.connect() as conn:
			stmt    = text("select * from add_to_cart a"
							+" inner join user u on a.user_id = u.user_id"
							+" inner join products p  on a.product_id = p.product_id"
							+" where u.user_id= "+str(user_id)+" and product_status=2;")
			result  = conn.execute(stmt).all()
			return [dict(r._mapping) for r in result] if result else None

	
	def update_yourorders(self,data,user_id):
		with engine.connect() as conn:
			stmt   = self.add_to_cart.update().where(self.add_to_cart.c.user_id.in_([user_id])).values(data)
			print(stmt)
			result = conn.execute(stmt)
			conn.commit()
			return result


	def delete_myorders(self,user_id):
		with engine.connect() as conn:
			stmt = text(f"delete from add_to_cart WHERE user_id = {user_id} and product_status=2;")
			result = conn.execute(stmt)
			conn.commit()
			return result

	
		

