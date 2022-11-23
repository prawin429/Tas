"""curriesportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 
from django.urls import re_path

handler404 = 'modules.views.error_404'
handler500 = 'modules.views.error_500'
handler403 = 'modules.views.error_403'
handler400 = 'modules.views.error_400'
# handler404 = 'account.views.error_404'
# handler500 = 'account.views.error_500'
# handler403 = 'account.views.error_403'
# handler400 = 'account.views.error_400'




urlpatterns = [
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
]
