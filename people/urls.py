from django.urls import path
from django.contrib import admin
from people.views import PersonListView, PersonCreateView, PersonUpdateView, PersonSerializerView
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'my-people', PersonSerializerView, basename='Person')

urlpatterns = [
    path('', include(router.urls)),
    path('people/', PersonListView.as_view(), name='person_list'),
    path('add/', PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/edit/', PersonUpdateView.as_view(), name='person_edit'),
]
