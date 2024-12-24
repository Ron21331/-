from django.shortcuts import render


def main(request):
    return render (request, "main1/main.html")
def map(request):
    return render (request, "main1/map.html")
def result(request):
    return render (request, "main1/result.html")
def about(request):
    return render (request, "main1/about.html")
def communication(request):
    return render (request, "main1/communication.html")