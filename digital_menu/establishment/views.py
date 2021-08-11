from django.views.generic import DetailView

from digital_menu.establishment.models import Establishment


class EstablishmentHome(DetailView):
    login_required = True
    model = Establishment
    slug_field = "slug"
    template_name = "establishment/index.html"

    def get_queryset(self):
        return Establishment.objects.filter(user=self.request.user)
