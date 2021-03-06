"""InstaJZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views 
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf #app level create a urls.py then use project-level to use app-level urls
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path # then we can use include

from Insta.views import SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    # add url , 原为 insta/
    path('', include('Insta.urls')),# go tp find app-level urls
    path('auth/', include('django.contrib.auth.urls')), #当有路径开头auth，交给django.contrib.auth下面的urls来处理
    path('auth/signup/', SignUp.as_view(), name = 'signup'),
    
]
