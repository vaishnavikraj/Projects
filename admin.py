from flask import *
from database import *
from livevideo import *

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')

@admin.route('/admin_manage_authorities',methods=['get','post'])
def admin_manage_authorities():

	data={}

	q="SELECT * FROM `authorities`"
	res=select(q)
	data['authorities']=res

	if 'submit' in request.form:
		uname=request.form['uname']
		pword=request.form['pword']
		aname=request.form['aname']
		place=request.form['place']
		lmark=request.form['lmark']
		pin=request.form['pin']
		phone=request.form['phone']
		email=request.form['email']

		q1="INSERT INTO `login`(`username`,`password`,`usertype`)VALUES('%s','%s','authority')"%(uname,pword)
		id=insert(q1)
		q="INSERT INTO `authorities`(`login_id`,`authority_name`,`place`,`landmark`,`pincode`,`phone`,`email`) VALUES('%s','%s','%s','%s','%s','%s','%s')"%(id,aname,place,lmark,pin,phone,email)
		insert(q)

		flash('success')

		return redirect(url_for('admin.admin_manage_authorities'))

	if 'action' in request.args:
		action=request.args['action']
		aid=request.args['aid']
		lid=request.args['lid']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM `authorities` WHERE `authority_id`='%s'"%(aid)
		res=select(q)
		data['upauthorities']=res

	if 'submits' in request.form:
		aname=request.form['aname']
		place=request.form['place']
		lmark=request.form['lmark']
		pin=request.form['pin']
		phone=request.form['phone']
		email=request.form['email']

		q="UPDATE `authorities` SET `authority_name`='%s',`place`='%s',`landmark`='%s',`pincode`='%s',`phone`='%s',`email`='%s' WHERE `authority_id`='%s'"%(aname,place,lmark,pin,phone,email,aid)
		update(q)

		flash('updated')

		return redirect(url_for('admin.admin_manage_authorities'))

	if action=='delete':
		q="DELETE FROM `authorities` WHERE `authority_id`='%s'"%(aid)
		delete(q)
		q1="DELETE FROM login WHERE login_id='%s'"%(lid)
		delete(q1)


		flash('deleted')

		return redirect(url_for('admin.admin_manage_authorities'))




	return render_template('admin_manage_authorities.html',data=data)



@admin.route('/admin_manage_police_station',methods=['get','post'])
def admin_manage_police_station():

	data={}
	q="SELECT * FROM `police_stations` INNER JOIN `districts` USING(`district_id`)"
	res=select(q)
	data['police_stations']=res

	if 'submit' in request.form:

		dist=request.form['dist']
		sname=request.form['sname']
		place=request.form['place']
		lmark=request.form['lmark']
		pin=request.form['pin']
		phone=request.form['phone']
		email=request.form['email']

		q="INSERT INTO `districts`(`district_name`)VALUES('%s')"%(dist)
		id=insert(q)
		q1="INSERT INTO `police_stations`(`district_id`,`station_name`,`place`,`landmark`,`pincode`,`phone`,`email`)VALUES('%s','%s','%s','%s','%s','%s','%s')"%(id,sname,place,lmark,pin,phone,email)
		insert(q1)

		flash('success')

		return redirect(url_for('admin.admin_manage_police_station'))

	if 'action' in request.args:
		action=request.args['action']
		sid=request.args['sid']
		did=request.args['did']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM `police_stations` INNER JOIN `districts` USING(`district_id`) WHERE `station_id`='%s'"%(sid)
		res=select(q)
		data['uppol']=res

	if 'submits' in request.form:

		sname=request.form['sname']
		place=request.form['place']
		lmark=request.form['lmark']
		pin=request.form['pin']
		phone=request.form['phone']
		email=request.form['email']
		dname=request.form['dist']

		q="UPDATE `police_stations` SET `station_name`='%s',`place`='%s',`landmark`='%s',`pincode`='%s',`phone`='%s',`email`='%s' WHERE `station_id`='%s'"%(sname,place,lmark,pin,phone,email,sid)
		update(q)
		q1="UPDATE `districts` SET `district_name`='%s' WHERE `district_id`='%s'"%(dname,did)
		update(q1)

		flash('updated')

		return redirect(url_for('admin.admin_manage_police_station'))

	if action=='delete':
		q="DELETE FROM `police_stations` WHERE station_id='%s'"%(sid)
		delete(q)
		q1="DELETE FROM `districts` WHERE `district_id`='%s'"%(did)
		delete(q1)

		flash('deleted')

		return redirect(url_for('admin.admin_manage_police_station'))



	return render_template('admin_manage_police_station.html',data=data)



@admin.route('/admin_manage_police',methods=['get','post'])
def admin_manage_police():

	data={}
	q="SELECT * FROM `police`"
	res=select(q)
	data['police']=res

	q1="SELECT * FROM `police_stations`"
	ress=select(q1)
	data['polstn']=ress

	if 'submit' in request.form:
		uname=request.form['uname']
		pword=request.form['pword']
		fname=request.form['fname']
		lname=request.form['lname']
		age=request.form['age']
		quali=request.form['qualification']
		yoj=request.form['year']
		phone=request.form['phone']
		email=request.form['email']
		sname=request.form['sname']
		q="INSERT INTO `login`(`username`,`password`,`usertype`)VALUES('%s','%s','police')"%(uname,pword)
		id=insert(q)
		q1="INSERT INTO `police`(`login_id`,`station_id`,`first_name`,`last_name`,`age`,`qualification`,`year_of_join`,`phone`,`email`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,sname,fname,lname,age,quali,yoj,phone,email)
		insert(q1)

		flash('success')

		return redirect(url_for('admin.admin_manage_police'))

	if 'action' in request.args:
		action=request.args['action']
		
		
		pid=request.args['pid']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM `police_stations` INNER JOIN `police` USING(`station_id`) WHERE police_id='%s'"%(pid)
		res=select(q)
		data['uppol']=res

	if 'submits' in request.form:

		sid=request.args['sid']

		sid=request.form['sname']
		fname=request.form['fname']
		lname=request.form['lname']
		age=request.form['age']
		quali=request.form['qualification']
		yoj=request.form['year']
		phone=request.form['phone']
		email=request.form['email']

		q="UPDATE `police` SET `station_id`='%s',`first_name`='%s',`last_name`='%s',`age`='%s',`qualification`='%s',`year_of_join`='%s',`phone`='%s',`email`='%s' WHERE police_id='%s'"%(sid,fname,lname,age,quali,yoj,phone,email,pid)
		update(q)

		flash('updated')

		return redirect(url_for('admin.admin_manage_police'))

	if action=='delete':
		lid=request.args['id']
		q="DELETE FROM `login` WHERE `login_id`='%s'"%(lid)
		delete(q)
		q1="DELETE FROM `police` WHERE `police_id`='%s'"%(pid)
		delete(q1)

		flash('deleted')

		return redirect(url_for('admin.admin_manage_police'))




	return render_template('admin_manage_police.html',data=data)


@admin.route('/admin_manage_crime_category',methods=['get','post'])
def admin_manage_crime_category():

	data={}

	q="SELECT * FROM `crime_categories`"
	res=select(q)
	data['crime_categories']=res

	if 'submit' in request.form:
		cname=request.form['cname']
		des=request.form['description']
		q="INSERT INTO `crime_categories`(`category_name`,`description`) VALUES('%s','%s')"%(cname,des)
		insert(q)

		flash('success')

		return redirect(url_for('admin.admin_manage_crime_category'))

	if 'action' in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM `crime_categories` WHERE `category_id`='%s'"%(cid)
		res=select(q)
		data['upcat']=res

	if 'submits' in request.form:
		cname=request.form['cname']
		des=request.form['description']
		q="UPDATE `crime_categories` SET `category_name`='%s',`description`='%s' WHERE `category_id`='%s'"%(cname,des,cid)
		update(q)

		flash('updated')

		return redirect(url_for('admin.admin_manage_crime_category'))

	if action=='delete':
		q="DELETE FROM `crime_categories` WHERE `category_id`='%s'"%(cid)
		delete(q)

		flash('deleted')

		return redirect(url_for('admin.admin_manage_crime_category'))


	return render_template('admin_manage_crime_category.html',data=data)


@admin.route('/admin_view_criminals',methods=['get','post'])
def admin_view_criminals():

	data={}

	q="SELECT * FROM `criminals` WHERE `most_wanted`='most_wanted'"
	res=select(q)
	data['criminals']=res

	return render_template('admin_view_criminals.html',data=data)

@admin.route('/admin_view_complaints')
def admin_view_complaints():

	data={}

	q="SELECT * FROM `complaints` INNER JOIN `users` USING(user_id)"
	res=select(q)
	data['complaints']=res

	return render_template('admin_view_complaints.html',data=data)




@admin.route('/admin_view_feedback')
def admin_view_feedback():

	data={}

	q="SELECT * FROM `feedbacks` INNER JOIN `users` ON feedbacks.sender_id=users.login_id"
	res=select(q)
	data['user_feedbacks']=res
	q="SELECT * FROM feedbacks INNER JOIN `police` ON `police_id`=`sender_id`"
	res=select(q)
	data['police_feedbacks']=res


	return render_template('admin_view_feedback.html',data=data)

@admin.route('/admin_view_awareness_program')
def admin_view_awareness_program():

	data={}

	q="SELECT * FROM `awareness` INNER JOIN `police` USING(police_id)"
	res=select(q)
	data['awareness']=res

	return render_template('admin_view_awareness_program.html',data=data)

@admin.route('/admin_view_missing_persons_details')
def admin_view_missing_persons_details():

	data={}

	q="SELECT * FROM `missing_persons`"
	res=select(q)
	data['missing']=res

	return render_template('admin_view_missing_persons_details.html',data=data)

@admin.route('/admin_add_local_body',methods=['get','post'])
def admin_add_local_body():

	data={}

	q="SELECT * FROM `police_stations`"
	res=select(q)
	data['polstn']=res

	if 'submit' in request.form:
		sid=request.form['stations']
		name=request.form['name']
		description=request.form['description']
		q="INSERT INTO `local_body`(`station_id`,`name`,`description`)VALUES('%s','%s','%s')"%(sid,name,description)
		insert(q)

		flash('success')

		return redirect(url_for('admin.admin_add_local_body'))

	q="SELECT * FROM `local_body` INNER JOIN `police_stations` USING(station_id)"
	res=select(q)
	data['localbodies']=res

	if 'action' in request.args:
		action=request.args['action']
		lid=request.args['lid']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM `local_body` WHERE `localbody_id`='%s'"%(lid)
		res=select(q)
		data['uploc']=res

	if 'submits' in request.form:
		sid=request.form['stations']
		name=request.form['name']
		description=request.form['description']

		q="UPDATE `local_body` SET `station_id`='%s',`name`='%s',`description`='%s' WHERE `localbody_id`='%s'"%(sid,name,description,lid)
		update(q)

		flash('success')

		return redirect(url_for('admin.admin_add_local_body'))

	if action=='delete':
		q="DELETE FROM `local_body` WHERE `localbody_id`='%s'"%(lid)
		delete(q)

		flash('success')

		return redirect(url_for('admin.admin_add_local_body'))

	return render_template('admin_add_local_body.html',data=data)

@admin.route('/admin_add_control_room_vehicle',methods=['get','post'])
def admin_add_control_room_vehicle():

	if 'submit' in request.form:
		vnum=request.form['vnum']
		cnum=request.form['cnum']
		enum=request.form['enum']
		yom=request.form['yom']
		company=request.form['company']
		model=request.form['model']
		username=request.form['uname']
		password=request.form['passw']
		q="SELECT * FROM `login` WHERE `username`='%s'"%(username)
		res=select(q)
		if res:
			flash("Username Already Exist")
		else:
			q="INSERT INTO `login` VALUES(NULL,'%s','%s','vehicle')"%(username,password)
			id=insert(q)
			q="INSERT INTO `vehicles`(login_id,`vehicle_number`,`chasis_number`,`engine_number`,`year_of_manufacture`,`company`,`model`,`status`)VALUES('%s','%s','%s','%s','%s','%s','%s','pending')"%(id,vnum,cnum,enum,yom,company,model)
			ids=insert(q)
			q="INSERT INTO `vehicle_locations` VALUES(NULL,'%s','NA','NA',NOW())"%(ids)
			insert(q)

			flash('success')

		return redirect(url_for('admin.admin_add_control_room_vehicle'))

	data={}

	q="SELECT * FROM `vehicles`"
	res=select(q)
	data['vehicles']=res

	if 'action' in request.args:
		action=request.args['action']
		vid=request.args['vid']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM `vehicles` WHERE `vehicle_id`='%s'"%(vid)
		res=select(q)
		data['upveh']=res

	if 'submits' in request.form:
		vnum=request.form['vnum']
		cnum=request.form['cnum']
		enum=request.form['enum']
		yom=request.form['yom']
		company=request.form['company']
		model=request.form['model']
		q="UPDATE `vehicles` SET `vehicle_number`='%s',`chasis_number`='%s',`engine_number`='%s',`year_of_manufacture`='%s',`company`='%s',`model`='%s',`status`='on' WHERE `vehicle_id`='%s'"%(vnum,cnum,enum,yom,company,model,vid)
		update(q)

		flash('success')

		return redirect(url_for('admin.admin_add_control_room_vehicle'))

	if action=='delete':
		q="DELETE FROM `vehicles` WHERE `vehicle_id`='%s'"%(vid)
		delete(q)

		flash('success')

		return redirect(url_for('admin.admin_add_control_room_vehicle'))

	return render_template('admin_add_control_room_vehicle.html',data=data)

@admin.route('/admin_track_vehicle')
def admin_track_vehicle():

	data={}

	q="SELECT * FROM `vehicle_locations` INNER JOIN `vehicles` USING(`vehicle_id`)"
	res=select(q)
	data['vehicle_locations']=res

	return render_template('admin_track_vehicle.html',data=data)

@admin.route('/admin_add_emergency_contact_details',methods=['get','post'])
def admin_add_emergency_contact_details():

	data={}

	q="SELECT * FROM `authorities`"
	res=select(q)
	data['authorities']=res

	if 'submit' in request.form:
		authority=request.form['authority']
		details=request.form['details']
		number=request.form['number']
		q="INSERT INTO `contacts`(`authority`,`details`,`number`)VALUES('%s','%s','%s')"%(authority,details,number)
		insert(q)

		flash('success')

		return redirect(url_for('admin.admin_add_emergency_contact_details'))

	q="SELECT * FROM `contacts`"
	res=select(q)
	data['emergency']=res

	if 'action' in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM `contacts` WHERE `contact_id`='%s'"%(cid)
		res=select(q)
		data['upcon']=res

	if 'submits' in request.form:

		authority=request.form['authority']
		details=request.form['details']
		number=request.form['number']
		q="UPDATE `contacts` SET `authority`='%s',`details`='%s',`number`='%s' WHERE `contact_id`='%s'"%(authority,details,number,cid)
		update(q)

		flash('success')

		return redirect(url_for('admin.admin_add_emergency_contact_details'))

	if action=='delete':
		q="DELETE FROM `contacts` WHERE `contact_id`='%s'"%(cid)
		delete(q)

		flash('success')

		return redirect(url_for('admin.admin_add_emergency_contact_details'))

	return render_template('admin_add_emergency_contact_details.html',data=data)


@admin.route('/admin_view_criminal_alert')
def admin_view_criminal_alert():

	data={}

	q="SELECT *,`criminals`.`first_name` AS criminal_name,`criminal_alert`.status AS crime_status,`users`.`first_name` AS user_name FROM `criminal_alert` INNER JOIN `users` USING (user_id) INNER JOIN `criminals` USING(criminal_id)"
	res=select(q)
	data['criminal_alert']=res
	
	return render_template('admin_view_criminal_alert.html',data=data)

@admin.route('/admin_view_mw_criminals')
def admin_view_mw_criminals():

	data={}

	q="SELECT * FROM `criminals` WHERE `most_wanted`='most_wanted'"
	res=select(q)
	data['wanted']=res

	return render_template('admin_view_mw_criminals.html',data=data)

@admin.route('/adminviewlivecamera')
def adminviewlivecamera():

	data={}

	video()

	return render_template('admin_home.html',data=data)
