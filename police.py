from flask import *
from database import *
import uuid

police=Blueprint('police',__name__)

@police.route('/police_home')
def police_home():
	return render_template('police_home.html')

@police.route('/police_manage_criminals',methods=['get','post'])
def police_manage_criminals():

	data={}

	q="SELECT * FROM `crime_categories`"
	res=select(q)
	data['crimes']=res

	if 'submit' in request.form:

		cid=request.form['cat']
		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']
		place=request.form['place']
		pin=request.form['pin']
		age=request.form['age']
		gender=request.form['gender']

		photo=request.files['photo']
		path='static/criminals/'+str(uuid.uuid4())+photo.filename
		photo.save(path)

		status=request.form['Status']

		q="INSERT INTO `criminals`( `category_id`,`first_name`,`last_name`,`house_name`,`place`,`pincode`,`age`,`gender`,`photo`,`status`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(cid,fname,lname,hname,place,pin,age,gender,path,status)
		insert(q)

		flash('success')

		return redirect(url_for('police.police_manage_criminals'))

	q="SELECT * FROM `criminals`"
	res=select(q)
	data['criminals']=res

	if 'action' in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM `criminals` WHERE `criminal_id`='%s'"%(cid)
		res=select(q)
		data['upcri']=res

	if 'submits' in request.form:

		cidd=request.form['cat']
		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']
		place=request.form['place']
		pin=request.form['pin']
		age=request.form['age']
		gender=request.form['gender']

		photo=request.files['photo']
		path='static/criminals/'+str(uuid.uuid4())+photo.filename
		photo.save(path)

		status=request.form['Status']

		q="UPDATE `criminals` SET `category_id`='%s',`first_name`='%s',`last_name`='%s',`house_name`='%s',`place`='%s',`pincode`='%s',`age`='%s',`gender`='%s',`photo`='%s',`status`='%s' WHERE `criminal_id`='%s'"%(cidd,fname,lname,hname,place,pin,age,gender,path,status,cid)
		update(q)

		flash('updated')

		return redirect(url_for('police.police_manage_criminals'))

	if action=='delete':
		q="DELETE FROM `criminals` WHERE `criminal_id`='%s'"%(cid)
		delete(q)

		flash('deleted')

		return redirect(url_for('police.police_manage_criminals'))

	if action=='mw':
		q="UPDATE `criminals` SET `most_wanted`='most_wanted' WHERE `criminal_id`='%s'"%(cid)
		update(q)

		flash('listed')

		return redirect(url_for('police.police_manage_criminals'))






	return render_template('police_manage_criminals.html',data=data)


@police.route('/police_manage_missing_person_details',methods=['get','post'])
def police_manage_missing_person_details():

	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']
		place=request.form['place']
		pin=request.form['pin']

		photo=request.files['photo']
		path='static/missing/'+str(uuid.uuid4())+photo.filename
		photo.save(path)
		
		cperson=request.form['cperson']
		relation=request.form['relation']
		phone=request.form['phone']

		q="INSERT INTO `missing_persons`(`first_name`,`last_name`,`house_name`,`place`,`pincode`,`photo`,`contact_person`,`relation`,`phone`,`status`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','missing')"%(fname,lname,hname,place,pin,path,cperson,relation,phone)
		insert(q)

		flash('success')

		return redirect(url_for('police.police_manage_missing_person_details'))

	data={}

	q="SELECT * FROM `missing_persons` WHERE `status`='missing'"
	res=select(q)
	data['missing']=res

	if 'action' in request.args:
		action=request.args['action']
		mpid=request.args['mpid']
	else:
		action=None

	if action=='update':

		q="SELECT * FROM `missing_persons` WHERE `missing_person_id`='%s'"%(mpid)
		res=select(q)
		data['upmiss']=res

	if 'submits' in request.form:

		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']
		place=request.form['place']
		pin=request.form['pin']

		photo=request.files['photo']
		path='static/missing/'+str(uuid.uuid4())+photo.filename
		photo.save(path)
		
		cperson=request.form['cperson']
		relation=request.form['relation']
		phone=request.form['phone']

		q="UPDATE `missing_persons` SET `first_name`='%s',`last_name`='%s',`house_name`='%s',`place`='%s',`pincode`='%s',`photo`='%s',`contact_person`='%s',`relation`='%s',`phone`='%s' WHERE `missing_person_id`='%s'"%(fname,lname,hname,place,pin,path,cperson,relation,phone,mpid)
		update(q)

		flash('updated')

		return redirect(url_for('police.police_manage_missing_person_details'))

	if action=='delete':
		q="DELETE FROM `missing_persons` WHERE `missing_person_id`='%s'"%(mpid)
		delete(q)

		flash('deleted')

		return redirect(url_for('police.police_manage_missing_person_details'))

	return render_template('police_manage_missing_person_details.html',data=data)

@police.route('/police_manage_complaints',methods=['get','post'])
def police_manage_complaints():

	data={}
	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS username FROM `complaints` INNER JOIN `users` USING (user_id)"
	res=select(q)
	data['complaints']=res

	return render_template('police_manage_complaints.html',data=data)

@police.route('/police_manage_crime_records',methods=['get','post'])
def police_manage_crime_records():

	data={}

	cid=request.args['cid']

	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS username FROM `complaints` INNER JOIN `users` USING (user_id) WHERE complaint_id='%s'"%(cid)
	res=select(q)
	data['comp']=res

	if 'submit' in request.form:
		title=request.form['titlee']
		des=request.form['des']

		file=request.files['file']
		path="static/crime_records/"+str(uuid.uuid4())+file.filename
		file.save(path)

		q="INSERT INTO `crime_records`(`complaint_id`,`police_id`,`title`,`description`,`file`,`date_time`)VALUES('%s','%s','%s','%s','%s',NOW())"%(cid,session['pid'],title,des,path)
		insert(q)
		q="UPDATE `complaints` SET `status`='FIR_filed' WHERE complaint_id='%s'"%(cid)
		update(q)

		flash('success')

		return redirect(url_for('police.police_manage_complaints'))

	return render_template('police_manage_crime_records.html',data=data)

@police.route('/police_view_crime_records')
def police_view_crime_records():

	data={}

	cid=request.args['cid']

	q="SELECT * FROM `crime_records` WHERE complaint_id='%s'"%(cid)
	res=select(q)
	data['crime_records']=res

	return render_template('police_view_crime_records.html',data=data)

@police.route('/police_add_feedback',methods=['get','post'])
def police_add_feedback():
	data={}

	if 'submit' in request.form:

		feedback=request.form['feedback']

		q="INSERT INTO `feedbacks`(`sender_id`,`feedback`,`date_time`)VALUES('%s','%s',NOW())"%(session['login_id'],feedback)
		insert(q)

		flash('success')

		return redirect(url_for('police.police_add_feedback'))

	

	q="SELECT * FROM `feedbacks` inner join police on sender_id=login_id WHERE `sender_id`='%s'"%(session['login_id'])
	res=select(q)
	data['feedback']=res

	return render_template('police_add_feedback.html',data=data)

@police.route('/police_crime_records_on_home')
def police_crime_records_on_home():

	data={}

	q1="SELECT * FROM `crime_records` WHERE police_id='%s'"%(session['pid'])
	ress=select(q1)
	data['record']=ress

	if 'action' in request.args:
		action=request.args['action']
		crid=request.args['crid']
	else:
		action=None

	# if action=='update':
	# 	q="SELECT * FROM `crime_records` WHERE `crime_record_id`='%s'"%(crid)
	# 	res=select(q)
	# 	data['upcrime']=res

	if action=='delete':
		q="DELETE FROM `crime_records` WHERE `crime_record_id`='%s'"%(crid)
		delete(q)

		flash('success')

		return redirect(url_for('police.police_crime_records_on_home'))

	return render_template('police_crime_records_on_home.html',data=data)


@police.route('/police_manage_awareness_program',methods=['get','post'])
def police_manage_awareness_program():

	if 'submit' in request.form:
		title=request.form['title']
		des=request.form['des']

		file=request.files['file']
		path="static/awareness/"+str(uuid.uuid4())+file.filename
		file.save(path)

		place=request.form['place']
		edt=request.form['date']


		q="INSERT INTO `awareness`(`police_id`,`title`,`description`,`file`,`place`,`event_date_time`,`date_time`) VALUES('%s','%s','%s','%s','%s','%s',NOW())"%(session['pid'],title,des,path,place,edt)
		insert(q)

		flash('success')

		return redirect(url_for('police.police_manage_awareness_program'))

	data={}

	q="SELECT * FROM `awareness` WHERE `police_id`='%s'"%(session['pid'])
	res=select(q)
	data['awareness']=res

	if 'action' in request.args:
		action=request.args['action']
		aid=request.args['aid']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM `awareness` WHERE `awareness_id`='%s'"%(aid)
		res=select(q)
		data['upawr']=res

	if 'submit' in request.form:
		title=request.form['title']
		des=request.form['des']

		file=request.files['file']
		path="static/awareness/"+str(uuid.uuid4())+file.filename
		file.save(path)

		place=request.form['place']
		edt=request.form['date']

		q="UPDATE `awareness` SET `title`='%s',`description`='%s',`file`='%s',`place`='%s',`event_date_time`='%s',`date_time`=now() WHERE `awareness_id`='%s'"%(title,des,path,place,edt,aid)
		update(q)

		flash('updated')

		return redirect(url_for('police.police_manage_awareness_program'))

	if action=='delete':
		q="DELETE FROM `awareness` WHERE `awareness_id`='%s'"%(aid)
		delete(q)

		flash('deleted')

		return redirect(url_for('police.police_manage_awareness_program'))

	return render_template('police_manage_awareness_program.html',data=data)


@police.route('/police_view_control_room_vehicle')
def police_view_control_room_vehicle():

	data={}

	q="SELECT * FROM `vehicles`"
	res=select(q)
	data['vehicles']=res

	return render_template('police_view_control_room_vehicle.html',data=data)

@police.route('/police_request_vehicle',methods=['get','post'])
def police_request_vehicle():

	if 'submit' in request.form:
		vid=request.args['vid']
		pid=session['pid']
		reason=request.form['reason']
		dt=request.form['datetime']

		q="INSERT INTO `vehicle_request`(`vehicle_id`,`police_id`,`reason`,`date_time`,`status`)VALUES('%s','%s','%s','%s','requested')"%(vid,pid,reason,dt)
		insert(q)
		q1=" UPDATE `vehicles` SET `status`='requested' WHERE vehicle_id='%s'"%(vid)
		update(q1)

		flash('success')

		return redirect(url_for('police.police_view_control_room_vehicle'))

	return render_template('police_request_vehicle.html')

@police.route('/police_view_criminal_alert')
def police_view_criminal_alert():

	data={}

	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS criminal_name,`criminal_alert`.`status` AS criminal_status FROM `criminal_alert` INNER JOIN `criminals` USING (criminal_id) WHERE police_id='%s'"%(session['pid'])
	res=select(q)
	data['criminal_alert']=res

	if 'action' in request.args:
		action=request.args['action']
		caid=request.args['caid']
		cid=request.args['cid']
	else:
		action=None

	if action=='investigate':
		q="UPDATE `criminal_alert` SET `status`='arrested' WHERE `criminal_alert_id`='%s'"%(caid)
		update(q)
		q1="UPDATE `criminals` SET `status`='arrested' WHERE criminal_id='%s'"%(cid)
		update(q1)

		flash('success')

		return redirect(url_for('police.police_view_criminal_alert'))

	return render_template('police_view_criminal_alert.html',data=data)