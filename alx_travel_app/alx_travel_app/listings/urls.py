from django.urls import path
from django.http import JsonResponse

def dummy_view(request):
    return JsonResponse({"message": "Hello from listings API!"})

urlpatterns = [
    path("", dummy_view, name="listings-home"),
]
