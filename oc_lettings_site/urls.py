from django.contrib import admin
from django.urls import path, include

admin.autodiscover()
admin.site.enable_nav_sidebar = False

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('lettings', include('lettings.urls')),
    path('profiles', include('profiles.urls')),
]
