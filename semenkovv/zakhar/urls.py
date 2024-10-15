
from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name = "index"),
    path('admin', admin.site.urls),
    path('name', views.name, name='name'),
    path('groupe', views.groupe, name='groupe'),
    path('age', views.age, name='age'),
    path('common', views.common, name='common'),
]