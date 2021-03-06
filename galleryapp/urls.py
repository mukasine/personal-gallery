from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.main_gallery,name = 'index'),
    url(r'^location/(\d+)',views.location,name = 'location'),
    url(r'^search/',views.search,name='search_category')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)