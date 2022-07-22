from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('tutors/', views.tutors, name='tutors'),
    path('tutor_requests/', views.tutor_requests, name='tutor_requests'),
    path('courses/', views.courses, name='courses'),
    path('course/<slug:slug>/', views.course, name='course'),
    path('', views.home, name='home'),
]
