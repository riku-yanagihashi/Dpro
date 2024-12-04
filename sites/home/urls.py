from django.urls import path
from . import views
from .views import example_view


urlpatterns = [
    path('', views.home, name='home'),
    path('form', views.form, name='form'),
    path('form/finish/', views.form_finish, name='form_finish'), 
    path('api/example/', example_view, name='example'),
]
