from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('memberlist/',views.memberlist,name="memberlist"),
    path('records/',views.records,name="records"),
    path('dashboard2/',views.dashboard2,name="dashboard2"),
    path('add/',views.add,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    path('memberlist/delete/<int:id>/',views.delete,name="delete"),
    path('memberlist/update/<int:id>/',views.update,name="update"),
    path('increment/<int:id>/', views.increment_click, name='increment_click'),
    path('present/<int:id>/', views.present, name='present'),
    path('absent/<int:id>/', views.absent, name='absent'),
    path('late/<int:id>/', views.late, name='late'),
    path('update/uprec/<int:id>/',views.uprec,name="uprec"),
    path('testing/',views.testing,name="testing")
]