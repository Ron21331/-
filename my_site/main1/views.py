from django.shortcuts import render

def pusto(request):
    return render (request, "main1/pusto.html")
def index(request):
    return render (request, "main1/glav.html")
def vhod(request):
    return render (request, "main1/vhod.html")
def carta(request):
    return render (request, "main1/carta.html")
def res(request):
    return render (request, "main1/res.html")
def Onas(request):
    return render (request, "main1/Onas.html")
def SV(request):
    return render (request, "main1/SV.html")