from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("Hello there World, Open Tour!")
