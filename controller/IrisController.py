from flask import Flask, request, Blueprint, jsonify, json,redirect, url_for,flash, render_template,session, app
from core.model.IrisModel import IrisModel

app = Blueprint('Iris', __name__)



@app.route('/view_signup',methods = ["GET" ])
def Viewsignup():
	# data=IrisModel().get_user()
	return render_template('Iris/signup.html',)

@app.route('/view_signup',methods = [ "POST"])
def SaveIrissignup():
	email_id	=	request.form.get('email_id')
	password	=	request.form.get('password')
	data	=	{
		'user_email':email_id,
		'user_password':password
	}

	user_email_id = IrisModel().check_user_email(email_id)
	if user_email_id:
			flash("Your email is already exists","Msgerror")
			return render_template('Iris/signup.html')
	else:
			IrisModel().insert_user(data)
			flash("Registration successfully.Please login","MsgSuccess")
			return redirect(url_for('Iris.Viewsignin'))



		

@app.route('/set_session', methods = ["GET","POST"])
def set_session():
	session['Viewsignin'] = 1
	return "session set done"

@app.route('/get_session', methods = ["GET","POST"])
def get_session():
	return str(session['Viewsignin'])

@app.route('/check_session', methods = ["GET","POST"])
def check_session():
	return str(session['Viewsignin'])




@app.route('/view_signin',methods = ["GET","POST" ])
def Viewsignin():
	data=IrisModel().get_user()
	return render_template('Iris/signin.html',data=data)


@app.route('/post_view_signin',methods = ["GET", "POST"])
def PostSignin():
	email_id = request.values.get('email_id')
	password = request.values.get('password')
	user_data = IrisModel().check_user_data(email_id)
	if user_data:
		user_email_id    = user_data['user_email']
		user_password = user_data['user_password']
		if (user_email_id== email_id) and (user_password==password):
			session['Viewsignin'] = user_data
   
			return redirect(url_for('Iris.Viewwebsite'))
		else:
			flash("Please login using your registered email and password","Msgerror")
		return redirect(url_for('Iris.Viewsignin'))
	else:
		flash(" Please Signup","Msgerror")
		return redirect(url_for('Iris.Viewsignup'))

# @app.route('/View_layout', methods = ["GET","POST"])
# def ayout():
# 		return render_template('Iris.layout.html')




   
@app.route('/view_website',methods = ["GET", "POST"])
def Viewwebsite():
	if session.get('Viewsignin',None) :
		return render_template('Iris/website.html')
	flash("Please Login...","Msgerror")	 
	return redirect(url_for('Iris.Viewsignin'))
	



@app.route('/view_about',methods = ["GET", "POST"])
def Viewabout():
	if session.get('Viewsignin',None) :
		return render_template('Iris/about.html')
	flash("Please Login...","Msgerror")
	return redirect(url_for('Iris.Viewsignin'))
	





@app.route('/view_face',methods = ["GET", "POST"])
def Viewface():
	if session.get('Viewsignin',None) :
		session_user = session.get('Viewsignin',None)
		get_product_type = IrisModel().get_product_type('FACE')
		return render_template('Iris/face.html',get_product_type=get_product_type)
	flash("Please Login...","Msgerror")	 
	return redirect(url_for('Iris.Viewsignin'))




@app.route('/view_nail',methods = ["GET", "POST"])
def Viewnail():
	if session.get('Viewsignin',None) :
		session_user = session.get('Viewsignin',None)
		get_product_type = IrisModel().get_product_type('NAIL')
		return render_template('Iris/nail.html',get_product_type=get_product_type)
	flash("Please Login...","Msgerror")	 
	return redirect(url_for('Iris.Viewsignin'))



@app.route('/view_lips',methods = ["GET", "POST"])
def Viewlips():
	if session.get('Viewsignin',None) :
		session_user = session.get('Viewsignin',None)
		get_product_type = IrisModel().get_product_type('LIPS')
		return render_template('Iris/lips.html',get_product_type=get_product_type)
	flash("Please Login...","Msgerror")	 
	return redirect(url_for('Iris.Viewsignin'))



@app.route('/view_eyes',methods = ["GET", "POST"])
def Vieweyes():
	if session.get('Viewsignin',None) :
		session_user = session.get('Viewsignin',None)
		get_product_type = IrisModel().get_product_type('EYES')
		return render_template('Iris/eyes.html',get_product_type=get_product_type)
	flash("Please Login...","Msgerror")	 
	return redirect(url_for('Iris.Viewsignin'))



@app.route('/view_accessories',methods = ["GET", "POST"])
def Viewaccessories():
	if session.get('Viewsignin',None) :
		session_user = session.get('Viewsignin',None)
		get_product_type = IrisModel().get_product_type('ACCESSORIES')
		return render_template('Iris/accessories.html',get_product_type=get_product_type)
	flash("Please Login...","Msgerror")
	return redirect(url_for('Iris.Viewsignin'))


# @app.route('/view_checkout',methods = ["GET"])
# def Viewcheckout():
# 	if session.get('Viewsignin',None) :	
# 		return render_template('Iris/checkout.html')
# 	flash("Please Login...","Msgerror")	
# 	return redirect(url_for('Iris.Viewsignin'))

# @app.route('/view_checkout',methods = [ "POST"])
# def SaveIrischeckout():
# 	email_id	=	request.form.get('email_id')
# 	password	=	request.form.get('password')
# 	data	=	{
# 		'user_email':email_id,
# 		'user_password':password
# 	}
 
# 	IrisModel().insert_user(data)
# 	flash("Profile Updated Successfully !","MsgSuccess",)
 
# 	return redirect(url_for('Iris.Viewcheckout'))

@app.route('/view_checkout', methods=["GET", "POST"])
def Viewcheckout():
	if session.get('Viewsignin', None):
		session_user = session.get('Viewsignin',None)
		data = IrisModel().get_user_by_id(session_user['user_id'])
		summary = IrisModel().get_summary(session_user['user_id'])
		print(summary)
		return render_template('Iris/checkout.html', data=data,summary=summary)

	flash("Please Login...", "Msgerror")
	return redirect(url_for('Iris.Viewsignin'))

@app.route('/save_checkout', methods=["POST"])
def Savecheckout():
	name = request.form.get('name')
	email_id = request.form.get('email_id')
	mobileno = request.form.get('mobileno')
	area = request.form.get('area')
	city = request.form.get('city')
	state = request.form.get('state')
	skintype= request.form.get('skintype')
	

	data = {
		'user_name': name,
		'user_email': email_id,
		'user_mobile': mobileno,
		'user_area': area,
		'user_city': city,
		'user_state': state,
		'user_skintype':skintype,
		
	}
	IrisModel().update_user(data)
	flash("PROFILE UPDATED SUCCESSFULLY","MsgSuccess")
	return redirect(url_for('Iris.Viewcheckout'))
	
	

	




@app.route('/view_assist',methods = ["GET", "POST"])
def Viewassist():
	if session.get('Viewsignin',None) :	
		return render_template('Iris/assist.html')
	flash("Please Login...","Msgerror")	
	return redirect(url_for('Iris.Viewsignin'))


@app.route('/view_signout',methods = ["GET", "POST"])
def Viewsignout():
	if session.get('Viewsignin',None) :
		return render_template('Iris/signout.html')
	flash("Please Login...","Msgerror")	
	return redirect(url_for('Iris.Viewsignin'))

		


@app.route('/signout',methods = ["GET", "POST"])
def Signout():
	if session.get('Viewsignin',None) :
		session.pop('Viewsignin', None)
		flash("signed Out Successfully...","MsgSuccess")
		return redirect(url_for('Iris.Viewsignin'))

	flash("Please Login...","Msgerror")	
	return redirect(url_for('Iris.Viewsignin'))

	






@app.route('/view_cart',methods = ["GET", "POST"])
def Viewcart():
	if session.get('Viewsignin',None) :
		session_user = session.get('Viewsignin',None)
		user_id = session_user['user_id']
		user_add_to_cart = IrisModel().get_user_add_to_cart(user_id)
		print(user_add_to_cart)
		return render_template('Iris/cart.html',user_add_to_cart=user_add_to_cart)
	flash("Please Login...","Msgerror")	
	return redirect(url_for('Iris.Viewsignin'))


# Post Add cart function

@app.route('/post_cart',methods = ["GET", "POST"])
def Postcart():
	print("<<<<<<<<<<<<< POST cart >>>>>>>>>>>>>")
	if session.get('Viewsignin',None) :
	 
		print(request.values)
		user_id        = request.values.get('user_id')
		product_id 	   = request.values.get('product_id')
		quantity 	   = request.values.get('product_quantity') or 1
		product_amount = request.values.get('product_amount')
		total_qua_amt  = int(quantity) *  int(product_amount)

		data	=	{
				'user_id':user_id,
				'product_id':product_id,
				'quantity':quantity,
				'total_product_amount':total_qua_amt,
				'product_status':0
	
				
				
			}
		print(data)
		IrisModel().insert_add_to_cart(data)
		flash("Added to cart !","MsgSuccess")
		return redirect(url_for('Iris.Viewcart'))
	else:
		flash("Please enter the quantity !","Msgerror")	
		flash("Please Login...","Msgerror")	
		return redirect(url_for('Iris.Viewsignin'))

@app.route('/delete_add_to_cart/<int:added_id>' ,methods = ["GET","POST"])
def Delete_add_to_cart(added_id):
	output = IrisModel().delete_add_to_cart(added_id) 
	print(output)

	flash("REMOVED successfully ! ","MsgSuccess" )
	return redirect (url_for('Iris.Viewcart'))
			


@app.route('/postsignin', methods = ["GET","POST"])
def Postsignin():
	email_id    =  request.values.get('email_id') 
	password    =  request.values.get('password') 
	if email_id == 'admin' and password == '123':
		
		return redirect(url_for('Iris.Layout'))
	else:
		flash("Invalid UserName and Password","Msgerror")
		return redirect(url_for('Iris.signin'))



@app.route('/layout', methods = ["GET","POST"])
def Layout():
		return render_template('layout.html')





@app.route('/view_yourorders',methods = ["GET", "POST"])
def Viewyourorders():
	if session.get('Viewsignin',None) :
		session_user = session.get('Viewsignin',None)
		user_id = session_user['user_id']

		yourorders = IrisModel().get_yourorders(user_id)
		print(yourorders)
		return render_template('Iris/yourorders.html',yourorders=yourorders)
	flash("Please Login...","Msgerror")	
	return redirect(url_for('Iris.Viewsignin'))

@app.route('/post_yourorders',methods = ["GET", "POST"])
def Postyourorders():
	print("<<<<<<<<<<<<< POST yourorders >>>>>>>>>>>>>")
	if session.get('Viewsignin',None) :
	 
		print(request.values)
		session_user   = session.get('Viewsignin',None)
		user_id 	   = session_user['user_id']		
		payment 	   = request.values.get('payment1')
		utr	   		   = request.values.get('utr1')

		data	=	{
				'product_status':2,
				'payment_method':payment,
				'payment_utr':utr
	
				
				
			}
		print(data)
		IrisModel().update_yourorders(data,user_id)
		flash("Your Order is Confirmed !.","MsgSuccess")
		return redirect(url_for('Iris.Viewyourorders'))
	else:
		
		flash("Please Login...","Msgerror")	
		return redirect(url_for('Iris.Viewsignin'))

@app.route('/delete_myorders' ,methods = ["GET","POST"])
def Delete_myorders():
	if session.get('Viewsignin',None) :
		session_user = session.get('Viewsignin',None)
		user_id = session_user['user_id']
		output = IrisModel().delete_myorders(user_id) 
		print(output)

		flash("Order cancelled successfully ! ","MsgSuccess" )
		return redirect (url_for('Iris.Viewyourorders'))
 