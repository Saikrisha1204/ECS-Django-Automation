from django.http import HttpResponse

def home(request):
    return HttpResponse("App3 working under /app2")
