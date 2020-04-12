from django.urls import path
from django.contrib import admin
from people.views import PersonListView, PersonCreateView, PersonUpdateView
from django.urls import include, path

urlpatterns = [
    path('people/', PersonListView.as_view(), name='person_list'),
    path('add/', PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/edit/', PersonUpdateView.as_view(), name='person_edit'),
    path('', include('webpage.urls')),
    path('admin/', admin.site.urls),
]
