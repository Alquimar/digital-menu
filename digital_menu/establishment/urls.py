from django.urls import path
from digital_menu.establishment.views import EstablishmentHome

app_name = "establishment"
urlpatterns = [
    # path("", login_required(TemplateView.as_view(template_name="establishment/index.html")), name="establishment-home"),
    path("<slug:slug>/", EstablishmentHome.as_view(), name="establishment-home"),
]
