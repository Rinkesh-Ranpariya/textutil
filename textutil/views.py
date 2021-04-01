# i have create this file - rinkesh

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutas.html')

def contact(request):
    return render(request, 'contact.html')

def analyzed(request):
    djt = request.GET.get('text', 'default')
    pun = request.GET.get('pun', 'off')
    uc = request.GET.get('uc', 'off')
    lc = request.GET.get('lc', 'off')

    if pun == 'on':
        internet_punctuation = """!@#$%^&*()"{}'[]/?,;:<.>-_+="""
        ana = ""
        for i in djt:
            if i not in internet_punctuation:
                ana = ana + i

        params = {'purpose': 'remove punctuation', 'analize': ana}
        djt = ana;
        # return render(request,"analized.html",params)

    if uc == 'on':
        upr = djt.upper()

        params = {'purpose': 'upper cashing', 'analize': upr}
        djt = upr;
        # return render(request,"analized.html",params)

    if lc == 'on':
        lpr = djt.lower()

        params = {'purpose': 'lower cashing', 'analize': lpr}
        # return render(request,"analized.html",params)

    if(pun != 'on' and uc != 'on' and lc != 'on'):
        return HttpResponse('''<h2>error !!! </h2> <h3>please enter your text or select any text editor option...</h3><h3>Try again...</h3>''')

    return render(request, "analized.html", params)
