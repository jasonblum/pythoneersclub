from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView, TemplateView

from .views import home

urlpatterns = [
	path('', home, name='home'),
    path('zulu/', admin.site.urls),
    path('trinket/', RedirectView.as_view(url='https://trinket.io/courses/join/JXnYU8')),
    path('chat/', RedirectView.as_view(url='http://discord.gg/2USePEX')),
]




