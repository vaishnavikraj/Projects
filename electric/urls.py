"""electric URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('',views.first),
     path('reg',views.reg),
     path('index',views.index),
     path('user',views.user),
     path('statio',views.statio),
     path('sta',views.sta),
     path('lo',views.lo),
     path('loca',views.loca),
     path('login',views.login),
     path('login1',views.login1),
     path('logout/',views.logout),
     path('addfeed',views.addfeed),
     path('addcomp',views.addcomp),
     path('stat1',views.stat1),
     path('feed',views.feed),
     path('stat1',views.stat1),
     path('stat2',views.stat2),
     path('compl',views.compl),
     path('books/<int:id>',views.books,name="books"),
     path('bookss',views.bookss),
     path('book/<int:id>',views.book,name="book"),
     path('book/view_price_pred/<int:id>',views.view_price_pred,name="view_price_pred"),
     path('book/view_price_pred/addbooking',views.addbooking,name="addbooking"),
     path('acc',views.acc),
     path('viewpay',views.viewpay),
     path('user_loc',views.user_loc),
     path('cancelbooking/<int:id>',views.cancelbooking),
     
     path('delete/<int:id>',views.delete),
     path('useraccept/<int:id>',views.useraccept,name='useraccept'),
     path('userreject/<int:id>',views.userreject,name='userreject'),
     path('pays/<int:id>',views.pays,name='pays'),
     path('pays/paymentss',views.paymentss,name='paymentss'),


     path('book/view_available_slots',views.view_available_slots,name='view_available_slots'),
    
     path('delete1/<int:id>',views.delete1),
     path('delete1/<int:id>',views.delete1),
     path('delete2/<int:id>',views.delete2),
    #path('update_feed/<int:id>',views.update_feed,name="update_feed"),
    #path('update_feed/update/<int:id>',views.update,name="update"),
     path('update_comp/<int:id>',views.update_comp,name="update_comp"),
     path('update_comp/updatee/<int:id>',views.updatee,name="updatee"),
]
