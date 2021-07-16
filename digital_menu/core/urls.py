from django.urls import path

from digital_menu.core.views import home

app_name = "core"
urlpatterns = [
    path("", view=home, name="home"),
]
