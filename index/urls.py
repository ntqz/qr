from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',index_views),
    url(r'^login/$',login_views),
]

urlpatterns += [
	url(r'^01_getTemp/$',getTemp_views),
	url(r'^02_getTemp/$',render_views),
	url(r'^03_var/$',var_views),
	url(r'^04_varExer/$',varExer_views),
	url(r'^05_varTemp/$',varTemp_views),
]
