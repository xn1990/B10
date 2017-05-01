"""B10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main import views as main_views
from django.views.generic.base import RedirectView
from django.conf.urls import handler403,handler404, handler500


handler403 = main_views.permission_denied
handler404 = main_views.page_not_found
handler500 = main_views.page_error

favicon_view = RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^$', main_views.index,name='index'),
    url(r'^login$', main_views.login,name='login'),
    url(r'^logout$', main_views.logout,name='logout'),
    url(r'^profile$', main_views.profile,name='profile'),
    url(r'^iedit_profile$', main_views.icons,name='icons'),
    url(r'^icons$', main_views.icons,name='icons'),
    
    url(r'^form_validation$', main_views.form_validation,name='icons'),

    
    url(r'^favicon\.ico$', favicon_view),
    url(r'^admin/', admin.site.urls),
]
