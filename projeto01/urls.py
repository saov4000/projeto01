
from django.contrib import admin
from django.urls import path
from projapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('galeria',views.galeria,name="galeria"),
    path('sobrenos',views.sobrenos,name="sobrenos"),
    path('contato',views.contato,name="contato")
]
