from django.shortcuts import render
from django.http import JsonResponse
from .models import Chicken  # Replace 'Chicken' with your model name
def showchicken(request):
    chickens = Chicken.objects.all()
    data = {
        "chickens": list(chickens.values())  # Convert queryset to a list of dictionaries
    }
    return JsonResponse(data)