from django.contrib import admin
from django.urls import path, include

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('lettings', include('lettings.urls')),
    path('profiles', include('profiles.urls')),
]
