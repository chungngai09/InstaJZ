from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HelloWorld (TemplateView): #继承
    #use default attribute
    template_name = 'test.html'
    # done