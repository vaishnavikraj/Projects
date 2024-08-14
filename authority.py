from flask import *
from database import *

authority=Blueprint('authority',__name__)

@authority.route('/authority_home')
def authority_home():
	return render_template('authority_home.html')

@authority.route('/authority_manage_meeting_for_localbody',methods=['get','post'])
def authority_manage_meeting_for_localbody():

	data={}

	q="SELECT * FROM `local_body`"
	res=select(q)
	data['localbody']=res

	if 'submit' in request.form:
		lid=request.form['localbody']
		mdt=request.form['time']

		q="INSERT INTO `meetings`(`localbody_id`,`meet_date_time`,`date_time`)VALUES('%s','%s',CURDATE())"%(lid,mdt)
		insert(q)

		
		flash('success')

		return redirect(url_for('authority.authority_manage_meeting_for_localbody'))

	q="SELECT * FROM `local_body` INNER JOIN meetings USING(`localbody_id`)"
	res=select(q)
	data['meetings']=res

	if 'action' in request.args:
		action=request.args['action']
		mid=request.args['mid']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM `local_body` INNER JOIN meetings USING(`localbody_id`)"
		res=select(q)
		data['upmeet']=res

	if 'submits' in request.form:
		lid=request.form['localbody']
		mdt=request.form['time']
		q="UPDATE `meetings` SET `localbody_id`='%s',`meet_date_time`='%s',`date_time`=CURDATE() WHERE meeting_id='%s'"%(lid,mdt,mid)
		update(q)

		flash('updated')

		return redirect(url_for('authority.authority_manage_meeting_for_localbody'))

	if action=='delete':
		q="DELETE FROM meetings WHERE meeting_id='%s'"%(mid)
		delete(q)

		return redirect(url_for('authority.authority_manage_meeting_for_localbody'))



	return render_template('authority_manage_meeting_for_localbody.html',data=data)


@authority.route('/authority_view_user_complaints')
def authority_view_user_complaints():

	data={}

	q="SELECT * FROM `complaints` INNER JOIN users USING(user_id)"
	res=select(q)
	data['complaints']=res

	return render_template('authority_view_user_complaints.html',data=data)


@authority.route('/authority_view_missing_person_found',methods=['get','post'])
def authority_view_missing_person_found():

	data={}

	q="SELECT *,`missing_found`.`place` AS found_place FROM `missing_found` INNER JOIN `missing_persons` USING (`missing_person_id`)"
	res=select(q)
	data['missingfound']=res

	if 'action' in request.args:
		action=request.args['action']
		mid=request.args['mid']
	else:
		action=None

	if action=='update':
		q="UPDATE `missing_persons` SET `status`='found' WHERE `missing_person_id`='%s'"%(mid)
		update(q)

		return redirect(url_for('authority.authority_view_missing_person_found'))

	return render_template('authority_view_missing_person_found.html',data=data)

@authority.route('/authority_view_nearby_police_station')
def authority_view_nearby_police_station():

	data={}

	q="SELECT * FROM `police_stations`"
	res=select(q)
	data['police_stations']=res

	return render_template('authority_view_nearby_police_station.html',data=data)



@authority.route('authority_view_vehicle_request_and_assign_vehicle')
def authority_view_vehicle_request_and_assign_vehicle():

	data={}

	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS police_name FROM `vehicle_request` INNER JOIN `police` USING(`police_id`) INNER JOIN vehicles USING(vehicle_id)"
	
	res=select(q)

	data['vehiclerequest']=res

	if 'action' in request.args:
		action=request.args['action']
		rid=request.args['rid']
		vid=request.args['vid']
	else:
		action=None

	if action=='assign':

		q="UPDATE `vehicle_request` SET `status`='assigned' WHERE `request_id`='%s'"%(rid)
		update(q)
		q1="UPDATE `vehicles` SET `status`='assigned' WHERE vehicle_id='%s'"%(vid)
		update(q1)
		

		flash('updated')

		return redirect(url_for('authority.authority_view_vehicle_request_and_assign_vehicle'))

	return render_template('authority_view_vehicle_request_and_assign_vehicle.html',data=data)

@authority.route('/authority_view_criminal_alert')
def authority_view_criminal_alert():

	data={}

	q="SELECT *,CONCAT(`users`.`first_name`,' ',`users`.`last_name`)AS username,CONCAT(`criminals`.`first_name`,' ',`criminals`.`last_name`) AS `criminal_name`,`criminal_alert`.`status` AS criminal_status FROM `criminal_alert` INNER JOIN `users` USING(user_id) INNER JOIN `criminals` USING(criminal_id)"
	res=select(q)
	data['criminaalert']=res
	
	return render_template('authority_view_criminal_alert.html',data=data)

@authority.route('/authority_view_police')
def authority_view_police():
	data={}

	crid=request.args['crid']
	data['crid']=crid

	q="SELECT * FROM `police` INNER JOIN `police_stations` USING (station_id)"
	res=select(q)
	data['police']=res

	if 'action' in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None

	if action=='assign':
		q="UPDATE `criminal_alert` SET `police_id`='%s',`status`='assigned' WHERE `criminal_alert_id`='%s'"%(pid,crid)
		update(q)

		flash('success')

		return redirect(url_for('authority.authority_view_criminal_alert'))

	return render_template('authority_view_police.html',data=data)


@authority.route('/authorty_view_vehicle_details')
def authorty_view_vehicle_details():

	data={}

	q="SELECT * FROM `vehicles`"
	res=select(q)
	data['vehicles']=res

	return render_template('authorty_view_vehicle_details.html',data=data)