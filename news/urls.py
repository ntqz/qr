from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^show/$',show_views),
    url(r'^$',index_views),
]
