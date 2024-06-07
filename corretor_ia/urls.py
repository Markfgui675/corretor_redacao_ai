from django.urls import path
from corretor_ia import views

urlpatterns = [
    path('', views.index, name='index'),
    path('account/', views.my_account, name='account'),
    path('account/logout/', views.logout_view, name='account'),
    path('login/', views.login_view, name='login-view'),
    path('login/create/', views.login_create, name='login-create'),
    path('register/', views.register_view, name='register-view'),
    path('register/create', views.register_create, name='register-create'),
    path('corretor/', views.corretor, name='corretor-ia'),
    path('corretor/send-redacao/', views.sendRedacao, name='send-redacao'),
    path('corretor/avaliacao/<int:id>/', views.redacaoAvaliacao, name='avaliacao-redacao'),
    path('politica-de-privacidade/', views.politica, name='politica'),
]
