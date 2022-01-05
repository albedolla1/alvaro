
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    # Url to access admin panel, for example - localhost:8000/admin
    path('admin/', admin.site.urls),
    # Including all the urls from home application
    path('', include('home.urls'))
]
