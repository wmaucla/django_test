# Create your views here.
from django.shortcuts import render

"""
You can see how the urls are calling the views, but here you see ways to redirect to other parts of your website. You can also redirect to other websites, etc. 
This CONTROLS what the users "view", not WHAT they view 
"""


def index(request):
    return render(request, 'webpage/index.html')


def fill_form(request):
    return render(request, 'webpage/registration.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        # form = RegistrationForm(), {'form': form}
        return render(request, 'webpage/name.html')
    else:
        return render(request, 'webpage/thanks.html')
