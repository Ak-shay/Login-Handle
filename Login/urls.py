from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('accounts/settings/',views.settings, name='settings'),
	path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.user_profile, name = 'profile'),
]
