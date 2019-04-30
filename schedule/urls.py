try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url
    
from django.urls import path
from .views import *

urlpatterns = [
     
     url(r'^$',
        view=Home.as_view(),
        name='home'),

    url(r'^schedule/$',
        view=ScheduleView.as_view(),
        name='schedule'),

    url(r'^search/$', 
        view=search, 
        name='search'),

]