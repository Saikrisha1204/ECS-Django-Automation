from django.http import HttpResponse

def home(request):
    return HttpResponse("App2 working under /app1")
