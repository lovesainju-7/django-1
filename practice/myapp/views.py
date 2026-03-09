from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django app is running!")

def about(request):
    return HttpResponse("This is the about page of the Django app.")
