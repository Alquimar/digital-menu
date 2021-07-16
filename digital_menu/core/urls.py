from django.urls import path

from digital_menu.core.views import home, about

app_name = "core"
urlpatterns = [
    path("", view=home, name="home"),
    path("about/", view=about, name="about"),
]
