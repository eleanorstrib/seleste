"""seleste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from selestesearch.views import index
from django.views.generic import TemplateView
from django.conf.urls import patterns

urlpatterns = patterns('',
	url(r'^.*$', TemplateView.as_view(template_name='base.html')),
	url(r'^rendered-partials(?P<home>).*$', 'render_partial'),
	# url(r'', include('selestesearch.urls')),
 #    url(r'', include('selestereviews.urls')),
    url(r'^admin/', admin.site.urls),
)

# urlpatterns = [
#     url(r'', include('selestesearch.urls')),
#     url(r'', include('selestereviews.urls')),
#     url(r'^admin/', admin.site.urls),
# ]



