from django.http import HttpResponse

def getHi(request):
    return HttpResponse("Hello world!")

