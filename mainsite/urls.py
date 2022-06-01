from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="index"),
    path('student/', views.student, name="student"),
    path('course/', views.course, name="course"),
    path('works/', views.works, name="works"),
    path('login/', views.userlogin, name="login"),
    path('vfx/', views.vfx, name="vfx"),
    path('arts/', views.arts, name="arts"),
    path('basic/', views.basic, name="basic"),
    path('graphics/', views.graphics, name="graphics"),
    path('editing/', views.editing, name="editing"),
    path('finance/', views.finance, name="finance"),
]
