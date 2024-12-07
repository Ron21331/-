from django.shortcuts import render


def index(request):
    return render (request, "main1/glav.html")
def carta(request):
    return render (request, "main1/carta.html")
def res(request):
    return render (request, "main1/res.html")
def Onas(request):
    return render (request, "main1/Onas.html")
def SV(request):
    return render (request, "main1/SV.html")