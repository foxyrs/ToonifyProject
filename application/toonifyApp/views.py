from django.http import HttpResponse


def index(request):
    return HttpResponse("Bonjour a tous l'équipe Toonification")