from django.urls import path
from . import views


app_name = 'demo'

urlpatterns = [
	path(route='', view=views.ZeroConfigurationDatatableView.as_view(), name='index'),
]