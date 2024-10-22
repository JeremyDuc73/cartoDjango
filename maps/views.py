from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import savedPlace
import json


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def save_place_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            label = data.get("label")
            address = data.get("address")
            if not label or not address:
                return JsonResponse({'status': 'error', 'message': 'Données manquantes'}, status=400)
            place = savedPlace(label=label, address=address)
            place.save()
            return JsonResponse({'status': 'success', 'message': 'lieu enregistré avec succès', 'id': place.id})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Erreur de format JSON'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'}, status=400)


def get_saved_places(request):
    if request.method == 'GET':
        places = savedPlace.objects.all().values('label', 'address')
        places_list = list(places)
        return JsonResponse({'places': places_list}, safe=False)
    return JsonResponse({'status': 'error', 'message': 'Méthode non autorisée'}, status=400)
