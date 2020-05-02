from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView, TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html')),
    path('zulu/', admin.site.urls),
    path('trinket/', RedirectView.as_view(url='https://trinket.io/courses/join/jXnYU8')),
    path('chat/', RedirectView.as_view(url='http://discord.gg/2USePEX')),
]
