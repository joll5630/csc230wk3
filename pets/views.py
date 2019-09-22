from django.http import HttpResponse
from .models import Pet

def index(request):
    pet_query = Pet.objects.order_by('-animal_type')
    pet_list = [(p.animal_type) for p in pet_query]
    output = ''.join(pet_list)
    return HttpResponse(output)
