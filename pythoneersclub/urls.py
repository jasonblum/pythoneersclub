from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView, TemplateView

from .views import home

urlpatterns = [
	path('', home, name='home'),
    path('zulu/', admin.site.urls),

    path('chat/', RedirectView.as_view(url='http://discord.gg/2USePEX')),
    path('cheatsheet/', RedirectView.as_view(url='https://learnxinyminutes.com/docs/python/')),
    path('comics/', RedirectView.as_view(url='https://www.dropbox.com/sh/28ab0g5jags1xam/AAAYoFDBXk90V_-TSFjlb8O6a')),
    path('socratica/', RedirectView.as_view(url='https://www.youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-')),
    path('trinket/', RedirectView.as_view(url='https://trinket.io/courses/join/JXnYU8')),
	
]




