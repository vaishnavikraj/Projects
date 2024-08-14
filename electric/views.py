from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage

# SESSION
from django.conf import settings
import math
import pandas as pd
import joblib 


def assign_slot(row):
    start_time = row['startTime']
    end_time = row['endTime']
    if 18 <= start_time <= 24 and 18 <= end_time <= 24:
        return 1
    elif 12 <= start_time <= 24 and 12 <= end_time <= 24:
        return 2
    elif 6 <= start_time <= 24 and 6 <= end_time <= 24:
        return 3
    elif 0 <= start_time <= 24 and 0 <= end_time <= 24:
        return 4
    else:
        return None
    
def peak_hour(slot):

	df = pd.read_csv('dataset.csv')
	df['dollars'] *= 70
	df = df[df['dollars'] != 0]
	df.dropna(inplace=True)


	# In[4]:


	df['slotNumber'] = df.apply(assign_slot, axis=1)


	# In[5]:


	slot_totals = df.groupby('slotNumber')['kwhTotal'].sum()

	# Print the total kwh for each slotNumber
	#print("Slot 1 Total kWh: ", slot_totals[1])
	#print("Slot 2 Total kWh: ", slot_totals[2])
	#print("Slot 3 Total kWh: ", slot_totals[3])
	#print("Slot 4 Total kWh: ", slot_totals[4])


	# In[6]:


	average_slot_total = slot_totals.mean()
	# Print the average slot total
	print("Average Slot Total: ", average_slot_total)
	print("Slot Total: ", slot_totals)


	# In[ ]:
	if slot_totals[int(slot)]>average_slot_total:
		#print("peak_hour")
		return 2
	else:
		#print("off_hour")
		return 1


def predict_price(vehicle_kwh,charge_time):
    df=pd.DataFrame({'kwhTotal':[vehicle_kwh],'chargeTimeHrs':[charge_time]})
    model=joblib.load("randomforest.model")
    predicts=model.predict(df)
    return predicts[0][0]



def distance(lat1, lon1, lat2, lon2):
    r = 6371 # radius of the Earth in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    
    a = math.sin(delta_phi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * \
        math.sin(delta_lambda / 2)**2
    res = r * (2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)))
    return res



def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')    
    
def reg(request):
    return render(request,'register.html') 
def user(request):    
    if request.method=="POST":
     name=request.POST.get("name")
     email=request.POST.get("email")
     phone=request.POST.get("phone")
     password=request.POST.get("password")
     row=register(name=name,email=email,phone=phone,password=password)
     row.save()     
    return render(request,'register.html')
    
    
    
    
def addfeed(request):    
    if request.method=="POST":
     feedbacks=request.POST.get("feedbacks")
     
     row=feedback(feedbacks=feedbacks,user_id=request.session['uid'])
     row.save()     
    return render(request,'feedback.html')
    
def addcomp(request):    
    if request.method=="POST":
     complaints=request.POST.get("complaints")
     
     row=complaint(complaints=complaints,user_id=request.session['uid'])
     row.save()     
    return render(request,'complaint.html')    


def statio(request):
    loc=location.objects.all()
    return render(request,'addstation.html',{'data':loc})      
    
def sta(request):    
    if request.method=="POST":
         name=request.POST.get("name")
         location=request.POST.get("location")
         longitude=request.POST.get("longitude")
         latitude=request.POST.get("latitude")
         slot=request.POST.get("slot")
         row=station(name=name,location=location,longitude=longitude,latitude=latitude,slot=slot)
         row.save()     
    return render(request,'addstation.html') 
    
def lo(request):
    return render(request,'addlocation.html') 
    
def loca(request):    
    if request.method=="POST":
         locations=request.POST.get("locations")
         row=location(locations=locations)
         row.save()     
    return render(request,'addlocation.html')     
    
def login(request):
    return render(request,'login.html')  
    
def login1(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    if email=="admin@gmail.com" and password=="admin":
        request.session['log']=email
        request.session['log1']=password
        request.session['admin']='admin'
        return render(request,"index.html") 
        
    elif register.objects.filter(email=email,password=password).exists():
        log2=register.objects.get(email=email,password=password)
        request.session['uid']=log2.id
        return render(request,"user_location.html")
    else:
        return render(request,"login.html")   
    
def user_loc(request):
    if request.method=="POST":
        latitude=request.POST.get('latitude')
        longitude=request.POST.get('longitude')
        #print(longitude,latitude)
        request.session['coordinates']=[latitude,longitude]
        return render(request,"index.html")

def logout(request):
    session_keys=list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)   
    
def feed(request):
    sel=feedback.objects.all()
    user3= register.objects.all()
    for i in sel:
        for j in user3:
            if str(i.user_id)==str(j.id):
                i.user_id=j.name    
    return render(request,'viewfeedback.html',{'res':sel})   
  
def compl(request):
    sel=complaint.objects.all()
    user3= register.objects.all()
    for i in sel:
        for j in user3:
            if str(i.user_id)==str(j.id):
                i.user_id=j.name    
    return render(request,'viewcomplaint.html',{'res':sel})     

def delete(request,id):
    dele=complaint.objects.get(id=id)
    dele.delete()
    return redirect(compl)

def delete1(request,id):
    dele=feedback.objects.get(id=id)
    dele.delete()
    return redirect(feed)   

    
def stat1(request):
    sel2=station.objects.all()
    return render(request,'viewstation.html',{'res':sel2})  
    
def stat2(request):
    sel3=station.objects.all().values()
    object_list = []
    lat1,lon1 = request.session['coordinates'][0],request.session['coordinates'][1]
    print("user_loc:",request.session['coordinates'])
    for i in sel3:
        dis=distance(float(lat1),float(lon1),float(i['latitude']),float(i['longitude']))
        i['distance']=dis
        object_list.append(i)
    print(object_list)
    object_list_new = sorted(object_list, key=lambda d: d['distance']) 
    print("sorted_list:",object_list_new)
    #sel3.sort(key=lambda x: x.distance,reverse=True)
    #object_list.append(sel3.station.order_by('distance').all())
    #print(object_list)
    return render(request,'viewstation2.html',{'res':object_list_new})    
    

def delete2(request,id):
    dele=station.objects.get(id=id)
    dele.delete()
    return redirect(stat1)    
"""
def update_feed(request,id):
    upd=feedback.objects.get(id=id)
    return render(request,'update.html',{'row':upd})     
    
def update(request,id):
    if request.method=="POST":
         user_id=request.POST.get("user_id")
         feedbacks=request.POST.get("feedbacks")
         row=feedback(user_id=user_id,feedbacks=feedbacks,id=id)
         row.save() 
    return redirect(feed) """


def update_comp(request,id):
    upda=station.objects.get(id=id)
    return render(request,'update1.html',{'row1':upda})     
    
def updatee(request,id):
    if request.method=="POST":
         name=request.POST.get("name")
         location=request.POST.get("location")
         slot=request.POST.get("slot")
         row=station.objects.get(id=id)
         row.slot=slot
         row.location=location
         row.name=name
         row.save() 
    return redirect(stat1) 

def book(request,id):
    sel2=station.objects.get(pk=id)
    time_slots=[i for i in range(1,25)]
    #print(time_slots)
    return render(request,'addbooking.html',{'res':sel2,'time_slots':time_slots})

def view_available_slots(request):
    if request.method=="POST":
        #print(list(request.POST.keys()))
        time_slots=[request.POST.get(i) for i in list(request.POST.keys())[5:]]
        charging_hours=len(time_slots)+10
        station_id=request.POST.get("station_id")
        station_name=request.POST.get("station_name")
        date=request.POST.get("date")
        vehicle_kwh=request.POST.get("vehicle_kwh")
        predicted_price=predict_price(int(vehicle_kwh),int(charging_hours))
        peak_rate=1
        print("time slots:",time_slots)
        for i in time_slots:
            if 0<int(i)<=6:
                sl=1
            elif 6<int(i)<=12:
                sl=2
            elif 12<int(i)<=18:
                sl=3
            elif 18<int(i)<=24:
                sl=4
            if peak_hour(sl)==2:
                peak_rate=2
                break
        predicted_price=predicted_price*peak_rate
        request.session['booking_details']={'station_id':station_id,'station_name':station_name,'date':date,'time_slot':str(time_slots),'predicted_price':predicted_price}
        sel1=station.objects.get(id=station_id)
        tot_slot=sel1.slot
        slots=[i for i in range(1,int(tot_slot)+1)]
        print("slots:",slots)
        sel2=booking.objects.filter(station_id=station_id,date=date)
        remove_slots=[]
        for i in sel2:
            book_time_slot=[int(i) for i in eval(i.time_slot)]
            print("booktime slot:",book_time_slot)
            for j in time_slots:
                print(j,book_time_slot)
                if int(j) in book_time_slot:
                    print(i.charging_slot)
                    remove_slots.append(int(i.charging_slot))
                    break
        print("slots to be removed:",remove_slots)
        for i in remove_slots:
            if i in slots:
                slots.remove(i)
        print("available:",slots)

        print("Total slots:",slots)
        return render(request,'view_available_slots.html',{'res':slots})

def view_price_pred(request,id):
    print("Booking Details:",type(request.session['booking_details']))
    request.session['booking_details']['charging_slot']=id
    request.session.save()
    #request.session['booking_details']=book_det.update({'charging_slot':id})
    print("Updated Booking Details:",request.session['booking_details'])
    """if request.method=="POST":
        
        station_id=request.POST.get("station_id")
        station_name=request.POST.get("station_name")
        date=request.POST.get("date")
        time_slot=request.POST.get("time_slot")
        vehicle_kwh=request.POST.get("vehicle_kwh")
        charging_hours=10
        predicted_price=predict_price(int(vehicle_kwh),int(charging_hours))
        request.session['booking_details']={'station_id':station_id,'station_name':station_name,'date':date,'time_slot':time_slot,'predicted_price':predicted_price}
        sel=booking.objects.filter(station_id=station_id,date=date,time_slot=time_slot)
        print(sel)
        booked_slot=len(sel)
        sel1=station.objects.get(id=station_id)
        tot_slot=sel1.slot
        available_slot=int(tot_slot)-booked_slot
        print("available slot:",available_slot)
        if available_slot<=0:
            return render(request,'viewpriceprediction.html',{'result':request.session['booking_details']})"""
    print("slot:",id)
    return render(request,'viewpriceprediction.html',{'res':request.session['booking_details']})

def addbooking(request):
    book_det=request.session['booking_details']
    print("booking details:",book_det)
    sel=booking(station_id=book_det['station_id'],charging_slot=book_det['charging_slot'],user_id=request.session['uid'],station_name=book_det['station_name'],date=book_det['date'],time_slot=book_det['time_slot'],price=book_det['predicted_price'],status="pending")
    sel.save()
    return redirect(stat2)       
                
def books(request,id):

    sel2=station.objects.get(pk=id)
    ins=booking(name=sel2.name,location=sel2.location,slot=sel2.slot,status="pending")
    ins.save()
    return redirect(stat2)    

    
    
def bookss(request):
    sel=booking.objects.all()
    return render(request,'viewbooking.html',{'res':sel})     
    
    
def useraccept(request,id):
    sel=booking.objects.get(id=id)
    sel.status='accepted'
    sel.save()  
    return redirect(bookss)
    
    
def userreject(request,id):
    sel=booking.objects.get(id=id)
    sel.status='rejected'
    sel.save()  
    return redirect(bookss)    
    

def acc(request):
    sel=booking.objects.all()
    return render(request,'viewbooking2.html',{'res':sel})


def pays(request,id):
    sel=booking.objects.get(id=id)
    return render(request,'payment.html',{'res':sel})

def cancelbooking(request,id):
    sel=booking.objects.get(id=id)
    sel.delete()
    sel1=booking.objects.all()
    return render(request,'viewbooking2.html',{'res':sel1})

def paymentss(request):
    if request.method=="POST":
        book_id=request.POST.get('book_id')
        phone=request.POST.get('phone')
        amount=request.POST.get('amount')
        location=request.POST.get('location')
        date=request.POST.get('date')
        payment_type=request.POST.get('payment_type')
        card_no=request.POST.get('card_no')
        cvv=request.POST.get('cvv')
        cardname=request.POST.get('cardname')
        slot=request.POST.get('slot')
        up=payment(month=phone,amount=amount,location=location,date=date,payment_type=payment_type,card_no=card_no,cvv=cvv,cardname=cardname,slot=slot,user_id=request.session['uid'])
        up.save()
        sel=booking.objects.get(id=book_id)
        sel.status="booked" 
        sel.save()
    return redirect(acc)


def viewpay(request):
    sel=payment.objects.all()
    user3= register.objects.all()
    for i in sel:
        for j in user3:
            if str(i.user_id)==str(j.id):
                i.user_id=j.name    
    return render(request,'viewpayment.html',{'result':sel})     
    
