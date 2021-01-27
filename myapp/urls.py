from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.testfn,name='test'),
    path('home',views.newfn,name='home'),
    path('page1',views.funhtml1,name='page1'),
    path('page2',views.funnhtml2,name='page2'),
    path('page3',views.funhtml3,name='page3')
]