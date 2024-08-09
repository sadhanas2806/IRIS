from flask import Flask, request, Blueprint, jsonify, json,redirect, url_for,flash, render_template,session, app
from core.model.UserModel import UserModel

app = Blueprint('user', __name__)

@app.route('/view_sample_index',methods = ["GET", "POST"])
def ViewSampleIndex():
	data=UserModel().get_sample_users()
	return render_template('sample/sample_index.html',data=data)

@app.route('/add_new',methods = ["GET", "POST"])
def AddNew():
	return render_template('sample/sample_window.html')

@app.route('/post_add_new',methods = ["GET", "POST"])
def PostAddNew():
	name = request.values.get("name") or None
	email = request.values.get("email") or None
	mobile = request.values.get("mobile") or None
	data ={
		'user_name':name,
		'user_email':email,
		'user_mobile':mobile
	}
	UserModel().insert_sample_users(data)
	flash("Successfully added!","successMsg")
	return redirect(url_for('user.ViewSampleIndex'))

@app.route('/edit_user/<int:user_id>',methods = ["GET", "POST"])
def EditUser(user_id):
	data = UserModel().get_user_data_by_id(user_id)
	return render_template('sample/edit_user.html',data=data)

@app.route('/post_edit_user',methods = ["GET", "POST"])
def PostEditUser():
	user_id = request.values.get("user_id") or None
	name = request.values.get("name") or None
	email = request.values.get("email") or None
	mobile = request.values.get("mobile") or None
	data ={
		'user_name':name,
		'user_email':email,
		'user_mobile':mobile
	}
	UserModel().update_user_data(user_id,data)
	flash("Successfully updated!","successMsg")
	return redirect(url_for('user.ViewSampleIndex'))

@app.route('/delete_user/<int:user_id>',methods = ["GET", "POST"])
def DeleteUser(user_id):
	data = UserModel().delete_user_data_by_id(user_id)
	flash("Successfully deleted!","successMsg")
	return redirect(url_for('user.ViewSampleIndex'))




