from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def inserttopic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('topic insertion is done successfully ') 
    return render(request,'inserttopic.html')
def insertwebpage(request):
    LTO=Topic.objects.all()
    d={'topic':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        WO.save()
        return HttpResponse('Webpage insertion is done successfully ') 
    return render(request,'insertwebpage.html',d)
def insertaccessrecords(request):
    LWO=Webpage.objects.all()
    d={'webpage':LWO}
    if request.method=='POST':
        
        na=request.POST['na']
        au=request.POST['au']
        da=request.POST['da']
        WO=Webpage.objects.get(name=na)
        
        AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=da)[0]
        AO.save()
        return HttpResponse('Accessrecords insertion is done successfully ') 
    return render(request,'insertaccessrecords.html',d)
def retrieve(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=Webpage.objects.none()

        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrieve.html',d)
def checkbox(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    return render(request,'checkbox.html',d)