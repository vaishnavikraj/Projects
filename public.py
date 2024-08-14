from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def mainhome():
	return render_template('public_home.html')

@public.route('/login',methods=['get','post'])
def public_login():

	if 'submit' in request.form:
		uname=request.form['uname']
		pword=request.form['pword']
		q="SELECT * FROM `login` WHERE `username`='%s' AND `password`='%s'"%(uname,pword)
		res=select(q)

		if res:
	
			login_id=res[0]['login_id']
			session['login_id']=login_id
			print(login_id)
			if res[0]['usertype']=='admin':

				flash('log in success')

				return redirect(url_for('admin.admin_home'))

			if res[0]['usertype']=='authority':
				print(":ress")
				q="SELECT * FROM `authorities` WHERE `login_id`='%s'"%(login_id)
				ress=select(q)

				if ress:
					print(ress)
					session['aid']=ress[0]['authority_id']
					

					flash('log in success')

					return redirect(url_for('authority.authority_home'))

			if res[0]['usertype']=='police':

				q="SELECT * FROM police WHERE `login_id`='%s'"%(login_id)
				res=select(q)

				if res:
					session['pid']=res[0]['police_id']

					flash('log in success')

					return redirect(url_for('police.police_home'))

			# if res[0]['usertype']=='user':

			# 	q="SELECT * FROM `login` WHERE `log_id`='%s'"%(log_id)
			# 	res=select(q)

			# 	if res:
			# 		session['eid']=res[0]['log_id']

			# 		flash('log in success')

			# 		return redirect(url_for('employee.employee_home'))

	return render_template('public_login.html')

@public.route('/public_view_criminals')
def public_view_criminals():

	data={}

	q="SELECT * FROM `criminals` WHERE most_wanted='most_wanted'"
	res=select(q)
	data['criminals']=res

	return render_template('public_view_criminals.html',data=data)

@public.route('/public_view_crime_history')
def public_view_crime_history():

	data={}

	q="SELECT * FROM `crime_records`"
	res=select(q)
	data['fir']=res

	return render_template('public_view_crime_history.html',data=data)

@public.route('/public_view_awareness_programs')
def public_view_awareness_programs():

	data={}

	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS first_name FROM `awareness` INNER JOIN `police` USING(police_id)"
	res=select(q)
	data['awareness']=res

	return render_template('public_view_awareness_programmes.html',data=data)

@public.route('/public_view_police_stations')
def public_view_nearest_police_stations():

	data={}

	q="SELECT * FROM `police_stations`"
	res=select(q)
	data['police_stations']=res

	return render_template('public_view_police_stations.html',data=data)


@public.route('/public_view_missing_persons')
def public_view_missing_persons():

	data={}

	q="SELECT * FROM `missing_persons`"
	res=select(q)
	data['missing']=res

	return render_template('public_view_missing_persons.html',data=data)

@public.route('/public_view_emergency_contacts')
def public_view_emergency_contacts():

	data={}

	q="SELECT * FROM `contacts`"
	res=select(q)
	data['emergency']=res

	return render_template('public_view_emergency_contacts.html',data=data)