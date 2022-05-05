from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('meetings/', views.meetings, name='meetings'),
    path('meetingsdetail/<int:id>', views.meetingdetail, name='detail'),
    path('resources/', views.resources, name='resources'),
]