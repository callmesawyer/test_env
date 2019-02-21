from django.urls import path

from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
	path('signup/', views.signup, name='signup'),
	path('login/', LoginView.as_view(template_name='login.html'),  name='login'),
	path('send/', views.TransactionView.as_view(), name='send'),
]