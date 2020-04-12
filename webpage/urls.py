from django.urls import path

from . import views

"""
What you see here is the mapping for the urls for this app.

The parent is webpage, i.e. localhost:8000/webpage

You see that the first item in the list is '', which means by default it's referring to localhost:8000/webpage/
The second item is name, i.e. that gets appended to the url: localhost:8000/webpage/name. What that actually refers to you'll see in views.py
"""


urlpatterns = [
    path('', views.index, name='index'),
    path('name', views.get_name, name='name'),
]