from django.contrib import admin
from django.urls import path
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name="index"),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('msg/<str:room_name>/<str:message>/',views.msg, name="msg")
]
