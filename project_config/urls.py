from django.urls import path
from django.contrib import admin
from people.views import PersonListView, PersonCreateView, PersonUpdateView
from django.urls import include, path

urlpatterns = [
    path('', include('people.urls')),
    path('', include('webpage.urls')),
    path('admin/', admin.site.urls),
]
