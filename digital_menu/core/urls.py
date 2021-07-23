from django.urls import path, include
from django.views.generic import TemplateView

app_name = "core"
urlpatterns = [
    path("", TemplateView.as_view(template_name="core/index.html"),
         name="home"),
    path("sobre/", TemplateView.as_view(template_name="core/about.html"),
         name="about"),
    path("produtos/", TemplateView.as_view(template_name="core/products.html"),
         name="products"),
    path("loja/", TemplateView.as_view(template_name="core/store.html"),
         name="store"),
    path('estabelecimentos/', include("digital_menu.establishment.urls", namespace="establishment")),
]
