from django.contrib import admin
from django.urls import path, include
from . import views

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('lettings.urls')),
    path('', views.index, name='index'),
    # path('', include('profiles.urls')),
    path('lettings', include('lettings.urls')),
    path('profiles', include('profiles.urls')),
]
