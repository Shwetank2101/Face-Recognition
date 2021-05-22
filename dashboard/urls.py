from django.urls import path,include

from . import views
from django.conf.urls import url

urlpatterns = [
	url('^$',views.index,name='Homepage'),
    # path('face',views.make, name='make')
]