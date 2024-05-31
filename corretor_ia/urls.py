from django.urls import path
from corretor_ia import views

urlpatterns = [
    path('', views.index, name='index'),
    path('corretor/', views.corretor, name='corretor-ia')
]
