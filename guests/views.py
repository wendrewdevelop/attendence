from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404
)
from datetime import datetime
from django.views import View
from django.db.models import Q
from guests.models import Guest
from attendence.utils import remove_accent


class IndexView(View):
    template_name = 'layouts/index.html'

    def get(self, request):
        guests = Guest.objects.filter(
            confirmed=False,
            confirmed_at=None
        )
        search = request.GET.get('q')
        if search:
            # Divide os termos de busca separados por vírgula
            search_terms = [term.strip() for term in search.split(',')]
            search_terms_normalized = [remove_accent(term).lower() for term in search_terms]

            # Construir a consulta Q
            query = Q()
            for term in search_terms_normalized:
                query |= Q(name__icontains=term)

            guests = guests.filter(query)

        context = {
            "guests": guests
        }

        return render(request, self.template_name, context)
    
    def post(self, request):
        guest_id = request.POST.get('guest_id')
        confirmed = request.POST.get('confirmed') == 'True'

        guest = get_object_or_404(Guest, id=guest_id)
        guest.confirmed = confirmed
        guest.confirmed_at = datetime.today()
        guest.save()

        if confirmed:
            return redirect('success')
        else:
            return redirect('wontgo')
    

class SuccessView(View):
    template_name = 'layouts/success.html'

    def get(self, request):
        return render(request, self.template_name)
    

class WontGoView(View):
    template_name = 'layouts/wontgo.html'

    def get(self, request):
        return render(request, self.template_name)