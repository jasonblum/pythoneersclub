from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import RedirectView, TemplateView

from .views import home

urlpatterns = [
	path('', home, name='home'),
    path('zulu/', admin.site.urls),

    re_path(r'^(?i)chat/', RedirectView.as_view(url='http://discord.gg/2USePEX')),
    re_path(r'^(?i)cheatsheet/', RedirectView.as_view(url='https://learnxinyminutes.com/docs/python/')),
    re_path(r'^(?i)codeacademy/', RedirectView.as_view(url='https://www.codecademy.com/learn/learn-python-3')),
    re_path(r'^(?i)comics/', RedirectView.as_view(url='https://www.dropbox.com/sh/28ab0g5jags1xam/AAAYoFDBXk90V_-TSFjlb8O6a')),
    re_path(r'^(?i)huskies/', RedirectView.as_view(url='https://drive.google.com/drive/folders/1zIXnPedsIrg0uOK9oPx2dGUjC_D5mp8b?usp=sharing')),
    re_path(r'^(?i)socratica/', RedirectView.as_view(url='https://www.youtube.com/playlist?list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-')),
    re_path(r'^(?i)trinket/', RedirectView.as_view(url='https://trinket.io/courses/join/JXnYU8')),
	
]




