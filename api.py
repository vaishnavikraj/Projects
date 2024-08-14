from flask import *
from database import *

import demjson
import uuid


api=Blueprint('api',__name__)

@api.route('/login',methods=['get','post'])
def login():
	data={}
	
	username = request.args['username']
	password = request.args['password']
	q="SELECT * from login where username='%s' and password='%s'" % (username,password)
	res = select(q)
	if res :
		data['status']  = 'success'
		data['data'] = res
		data['method']='login'
	else:
		data['status']	= 'failed'
		data['method']='login'
	return  demjson.encode(data)

@api.route('/userregister',methods=['get','post'])
def userregister():

	data = {}

	fname=request.args['fname']
	lname=request.args['lname']
	phone=request.args['phone']
	pin=request.args['pin']
	email=request.args['email']
	hname=request.args['hname']
	place=request.args['place']
	uname=request.args['uname']
	passw=request.args['pass']

	q1="SELECT * FROM login WHERE username='%s'" %(uname)
	print(q1)
	r=select(q1)
	print(r)
	if r:
		data['status']='duplicate'
		data['method']='userregister'
	else:
		q= "INSERT INTO `login` VALUES(NULL,'%s','%s','user')"%(uname,passw)
		lid = insert(q)
		qr="INSERT INTO `users` VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,fname,lname,hname,place,pin,phone,email)
		id=insert(qr)
		if id>0:
			data['status'] = 'success'
		else:
			data['status'] = 'failed'
		data['method']='userregister'
	return demjson.encode(data)

@api.route('/usersendfeedback',methods=['get','post'])
def usersendfeedback():

	data={}
	login_id=request.args['loginid']
	feed_des=request.args['feed_des']

	q= "INSERT INTO `feedbacks` VALUES(NULL,'%s','%s',NOW())"% (login_id,feed_des)
	print(q)
	id=insert(q)
	if id>0:
		data['status'] = 'success'
		data['method'] = 'usersendfeedback'
	else:
		data['status'] = 'failed'
		data['method'] = 'usersendfeedback'
	return demjson.encode(data)

@api.route('/userviewfeedback',methods=['get','post'])
def userviewfeedback():
	data = {}

	log_id=request.args['loginid']
	
	q="SELECT * FROM `feedbacks` WHERE `sender_id`='%s'"%(log_id)
	print(q)
	result = select(q)
	if result:
		data['status'] = 'success'
		data['data'] = result
		data['method'] = 'userviewfeedback'
	else:
		data['status'] = 'failed'
		data['method'] = 'userviewfeedback'
	return demjson.encode(data)


@api.route('/user_view_em_contact',methods=['get','post'])
def user_view_em_contact():
	data = {}

	
	q="SELECT * FROM `contacts`"
	result = select(q)
	print(q)
	if result:
		data['status'] = 'success'
		data['data'] = result
	else:
		data['status'] = 'failed'
	data['method'] = 'user_view_em_contact'
	return demjson.encode(data)




@api.route('/user_view_missing_persons',methods=['get','post'])
def user_view_missing_persons():
	data = {}

	
	q="SELECT *,CONCAT(first_name,' ',last_name) as pname FROM `missing_persons` WHERE `status` !='found'"
	print(q)
	result = select(q)
	if result:
		data['status'] = 'success'
		data['data'] = result
	else:
		data['status'] = 'failed'
	data['method'] = 'user_view_missing_persons'
	return demjson.encode(data)


@api.route('/user_view_wanted_criminals',methods=['get','post'])
def user_view_wanted_criminals():
	data = {}

	
	q="SELECT *,concat(first_name,' ',last_name) as cname FROM `criminals` INNER JOIN `crime_categories` USING(`category_id`) WHERE `status`='missing'"
	result = select(q)
	if result:
		data['status'] = 'success'
		data['data'] = result
	else:
		data['status'] = 'failed'
	data['method'] = 'user_view_wanted_criminals'
	return demjson.encode(data)



@api.route('/user_send_found_report',methods=['get','post'])
def user_send_found_report():

	data={}
	loginid=request.args['loginid']
	mp_ids=request.args['mp_ids']
	details=request.args['details']
	placename=request.args['placename']


	q= "INSERT INTO `missing_found` VALUES(NULL,'%s','%s','%s','%s',NOW())"%(loginid,mp_ids,placename,details)
	print(q)
	id=insert(q)
	if id>0:
		data['status'] = 'success'
	else:
		data['status'] = 'failed'
	data['method'] = 'user_send_found_report'
	return demjson.encode(data)


@api.route('/user_view_found_report',methods=['get','post'])
def user_view_found_report():
	data = {}

	mp_ids=request.args['mp_ids']

	
	q="SELECT * FROM `missing_found` WHERE `missing_person_id`='%s'"%(mp_ids)
	result = select(q)
	if result:
		data['status'] = 'success'
		data['data'] = result
	else:
		data['status'] = 'failed'
	data['method'] = 'user_view_found_report'
	return demjson.encode(data)


@api.route('/user_send_complaints',methods=['get','post'])
def user_send_complaints():

	data={}
	path = ""
	title=request.form['title']
	desc=request.form['desc']
	logid=request.form['logid']
	image=request.files['image']
	ftype = request.form['ftype']

	if ftype == 'video':
		path='static/uploads/'+str(uuid.uuid4())+ ".mp4"
		image.save(path)
	else:
		path='static/uploads/'+str(uuid.uuid4())+ ".jpg"
		image.save(path)


	q="INSERT INTO `complaints` VALUES(NULL,(SELECT `user_id` FROM `users` WHERE `login_id`='%s'),'user','%s','%s',NOW(),'pending')"%(logid,title,desc)
	print(q)
	ids=insert(q)
	q="INSERT INTO `files` VALUES(NULL,'%s','%s',NOW())"%(ids,path)
	id=insert(q)
	if id>0:
		data['status'] = 'success'
	else:
		data['status'] = 'failed'
	data['method'] = 'user_send_complaints'
	return demjson.encode(data)


@api.route('/user_view_complaints',methods=['get','post'])
def user_view_complaints():
	data = {}

	login_id=request.args['login_id']

	
	q="SELECT * FROM `complaints` INNER JOIN `files` USING(`complaint_id`) WHERE `user_id`=(SELECT `user_id` FROM `users` WHERE `login_id`='%s')"%(login_id)
	result = select(q)
	if result:
		data['status'] = 'success'
		data['data'] = result
	else:
		data['status'] = 'failed'
	data['method'] = 'user_view_complaints'
	return demjson.encode(data)


@api.route('/updatepasslocation',methods=['get','post'])
def updatepasslocation():
	data={}

	latti=request.args['latti']
	longi=request.args['longi']
	logid=request.args['log_id']
	
	q="UPDATE `vehicle_locations` SET `latitude`='%s',`longitude`='%s',`date_time`=NOW() WHERE `vehicle_id`=(SELECT `vehicle_id` FROM `vehicles` WHERE `login_id`='%s')"%(latti,longi,logid)
	print(q)
	id=update(q)
	
	data['status'] = 'success'
	
	data['method'] = 'updatepasslocation'
	return demjson.encode(data)

